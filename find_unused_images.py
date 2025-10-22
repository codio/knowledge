'''
python find_unused_images.py
python find_unused_images.py --delete
python find_unused_images.py --delete --yes
python find_unused_images.py --debug
'''

#!/usr/bin/env python3
import argparse
import csv
import os
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT_DIRS = [
    Path(r"source"),
    Path(r"student-source"),
]

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}

# Matches:
#   .. image:: /path.png
#   .. figure:: /path.png
#   .. |Alias| image:: /path.png
# And when the directive appears inline (e.g., inside a table cell).
# Accept plain, "quoted", or 'quoted' paths so we handle spaces.
DIRECTIVE_RE = re.compile(
    r"""
    \.\.\s+                                   # leading '.. '
    (?:\|[^|]+\|\s+)?                         # optional '|Alias| '
    (?:image|figure)::\s+                     # image:: or figure::
    (?P<path>"[^"]+"|'[^']+'|\S+)             # the path (quoted or non-space)
    """,
    re.IGNORECASE | re.VERBOSE,
)

SKIP_DIRS = {"_build", ".venv", "venv", "node_modules", ".git", "__pycache__"}

def is_url(s: str) -> bool:
    try:
        p = urlparse(s)
        return bool(p.scheme) and bool(p.netloc)
    except Exception:
        return False

def common_parent(paths: list[Path]) -> Path:
    parts = os.path.commonpath([str(p) for p in paths])
    return Path(parts)

def strip_quotes(s: str) -> str:
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    return s

def normalize_ref(s: str) -> str:
    # normalize backslashes, trim quotes, strip leading/trailing spaces
    s = strip_quotes(s.strip()).replace("\\", "/")
    return s

def rel_from_any_root(p: Path, roots_abs: list[Path]) -> tuple[Path, str] | None:
    """Return (root, relative_posix) if p is under any root; else None."""
    for r in roots_abs:
        try:
            rel = p.relative_to(r).as_posix()
            return r, rel
        except ValueError:
            continue
    return None

def list_image_files(roots_abs: list[Path], debug=False) -> set[tuple[Path, str]]:
    """
    Return a set of (root, rel_path) for all images under all roots.
    """
    found: set[tuple[Path, str]] = set()
    for root in roots_abs:
        for dirpath, dirnames, filenames in os.walk(str(root)):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                if Path(fn).suffix.lower() in IMAGE_EXTS:
                    full = (Path(dirpath) / fn).resolve()
                    try:
                        rel = full.relative_to(root).as_posix()
                        found.add((root, rel))
                    except ValueError:
                        if debug:
                            print(f"[skip-not-under-root] {full}")
                        continue
    if debug:
        print(f"[debug] Found {len(found)} images on disk across {len(roots_abs)} root(s).")
        for root, rel in list(sorted(found))[:10]:
            print(f"  - [{root.name}] {rel}")
    return found

def resolve_reference(rst_file: Path, ref: str, roots_abs: list[Path]) -> tuple[Path, str] | None:
    """
    Resolve an image/figure reference to (root, relative_posix) across multiple roots.
    Strategy:
      * Absolute (/img/foo.png): try each root/<rel>.
      * Relative (img/foo.png or ../img/foo.png): resolve against rst_file and then map to a root.
      * If file doesn't exist, still attempt to map path to a root by anchor (best-effort).
    """
    if is_url(ref):
        return None

    ref = normalize_ref(ref)

    # Absolute style (Sphinx-rooted): /img/foo.png
    if ref.startswith("/"):
        rel = ref.lstrip("/")
        # Prefer an existing file under any root; otherwise just bind to the rst's root
        for r in roots_abs:
            cand = (r / rel).resolve()
            if cand.exists():
                return r, rel
        # fallback: attach to the .rst file's own root anchor (even if missing)
        for r in roots_abs:
            try:
                rst_file.relative_to(r)
                return r, rel
            except ValueError:
                continue
        return None

    # Relative to the .rst file directory
    candidate = (rst_file.parent / ref)
    try:
        cand_abs = candidate.resolve()
    except FileNotFoundError:
        cand_abs = candidate.absolute()

    mapped = rel_from_any_root(cand_abs, roots_abs)
    if mapped:
        return mapped

    # If not under any root (odd), try binding to rst_file's root
    for r in roots_abs:
        try:
            rst_file.relative_to(r)
            # make rel w.r.t that root if possible
            try:
                rel = cand_abs.relative_to(r).as_posix()
                return r, rel
            except ValueError:
                # last resort: synthesize rel from string form
                return r, Path(ref).as_posix()
        except ValueError:
            continue
    return None

def parse_rst_image_refs(roots_abs: list[Path], debug=False) -> set[tuple[Path, str]]:
    """
    Parse all .rst files under all roots and collect referenced images as (root, rel_path).
    """
    refs: set[tuple[Path, str]] = set()
    for root in roots_abs:
        for dirpath, dirnames, filenames in os.walk(str(root)):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                if not fn.lower().endswith(".rst"):
                    continue
                rst_path = Path(dirpath) / fn
                try:
                    text = rst_path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    text = rst_path.read_text(encoding="latin-1")

                for m in DIRECTIVE_RE.finditer(text):
                    raw = m.group("path")
                    raw = normalize_ref(raw)
                    if not any(raw.lower().endswith(ext) for ext in IMAGE_EXTS):
                        continue
                    resolved = resolve_reference(rst_path.resolve(), raw, roots_abs)
                    if resolved is not None:
                        refs.add(resolved)
                    elif debug:
                        print(f"[warn] Could not resolve: {raw} in {rst_path}")

    if debug:
        print(f"[debug] Found {len(refs)} image/figure references across {len(roots_abs)} root(s).")
        for root, rel in list(sorted(refs))[:10]:
            print(f"  - [{root.name}] {rel}")
    return refs

def write_csv(unused: list[tuple[Path, str]], csv_path: Path):
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["root", "image_path"])  # which root + rel path
        for root, rel in unused:
            writer.writerow([str(root), rel])
    print(f"[info] CSV written: {csv_path}")

def delete_files(unused: list[tuple[Path, str]], yes=False):
    if not unused:
        print("[info] No unused images to delete.")
        return
    if not yes:
        confirm = input(f"⚠️  Delete {len(unused)} unused images across all roots? (y/N): ").strip().lower()
        if confirm != "y":
            print("[info] Deletion canceled.")
            return
    deleted = 0
    for root, rel in unused:
        try:
            (root / rel).unlink(missing_ok=True)
            deleted += 1
        except Exception as e:
            print(f"[error] Could not delete [{root.name}] {rel}: {e}")
    print(f"[info] Deleted {deleted} unused image(s).")

def main():
    parser = argparse.ArgumentParser(
        description="Find or delete unused images referenced via '.. image::', '.. figure::', or '.. |alias| image::' across multiple Sphinx roots."
    )
    parser.add_argument("--delete", action="store_true", help="Delete unused images instead of listing them")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation prompt when deleting")
    parser.add_argument("--debug", action="store_true", help="Show debug info")
    args = parser.parse_args()

    roots_abs = [p.resolve() for p in ROOT_DIRS]
    for r in roots_abs:
        print(f"[info] Root directory: {r}")

    # Gather images and references from all roots
    images_on_disk = list_image_files(roots_abs, debug=args.debug)         # set[(root, rel)]
    referenced = parse_rst_image_refs(roots_abs, debug=args.debug)         # set[(root, rel)]

    # Treat references as shared by RELATIVE PATH across roots:
    # if any root references 'img/foo.png', we consider that rel used everywhere,
    # so remove (root, rel) from unused for every root containing that rel.
    referenced_rels = {rel for (_root, rel) in referenced}
    unused = sorted([(root, rel) for (root, rel) in images_on_disk if rel not in referenced_rels],
                    key=lambda x: (str(x[0]), x[1]))

    print(f"[result] Found {len(unused)} unused image(s) across all roots).")

    # CSV goes to the common parent of all roots
    out_csv = common_parent(roots_abs) / "unused_images.csv"

    if args.delete:
        delete_files(unused, yes=args.yes)
    else:
        write_csv(unused, out_csv)
        if args.debug and unused:
            print("First few unused images:")
            for root, rel in unused[:10]:
                print(f"  - [{root.name}] {rel}")

if __name__ == "__main__":
    main()
