# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
BUILDDIRSTU   = build
BUILDTARGET    = -M

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Default TYPE if not provided: both (build student + instructor)
ifeq ($(TYPE),)
TYPE := both
endif

ifeq ($(PWD),/home/codio/workspace)
BUILDTARGET := -b
BUILDDIR := build/html/source
BUILDDIRSTU := build/html/student-source
endif

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	rm -rf "$(BUILDDIR)"
	rm -rf "$(BUILDDIRSTU)"
ifeq ($(TYPE),student)
	@$(SPHINXBUILD) "$(BUILDTARGET)" $@ "student-$(SOURCEDIR)" "$(BUILDDIRSTU)" $(SPHINXOPTS) $(O)
else ifeq ($(TYPE),instructor)
	@$(SPHINXBUILD) "$(BUILDTARGET)" $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
else ifeq ($(TYPE),both)
	@$(SPHINXBUILD) "$(BUILDTARGET)" $@ "student-$(SOURCEDIR)" "$(BUILDDIRSTU)" $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD) "$(BUILDTARGET)" $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
else
	$(error Invalid TYPE='$(TYPE)'. Use TYPE=student, TYPE=instructor, or TYPE=both)
endif