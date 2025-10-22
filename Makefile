# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Default TYPE if not provided: both (build student + instructor)
ifeq ($(TYPE),)
TYPE := both
endif

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	rm -rf "$(BUILDDIR)"
ifeq ($(TYPE),student)
	@$(SPHINXBUILD) -M $@ "student-$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
else ifeq ($(TYPE),instructor)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
else ifeq ($(TYPE),both)
	@$(SPHINXBUILD) -M $@ "student-$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
else
	$(error Invalid TYPE='$(TYPE)'. Use TYPE=student, TYPE=instructor, or TYPE=both)
endif