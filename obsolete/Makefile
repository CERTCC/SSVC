# Makefile

SHELL=/bin/bash
#
# Converts Markdown to other formats (HTML, PDF, DOCX, RTF, ODT, EPUB) using Pandoc
# based on https://gist.github.com/kristopherjohnson/7466917
# <http://johnmacfarlane.net/pandoc/>
#
# Run "make" (or "make all") to convert to all other formats
#
# Run "make clean" to delete converted files

# versioning
# need a better way of automatically updating version numbers
MAJOR=2
MINOR=1
# these have the common meanings from semantic versioning
# major should be incremented with content changes that introduce incompatibilities
# minor should be incremented for meaningful changes that do not break compatibility
# fix is based on git commit
FIX=`git rev-parse --short HEAD`

#versioning across different content is a bit complicated.
# The PDF major.minor should match any schema, tree, or other supporting document version
# This means if the major.minor version changes, the schemas need a numbering change
# The fix version for the schema and the PDF document may mismatch

HOME:=$(shell pwd)
OUTDIR=$(HOME)/../draft
SRC=./md_src_files


TITLE:="Prioritizing Vulnerability Response: A Stakeholder-Specific Vulnerability Categorization (SSVC version $(MAJOR).$(MINOR).$(FIX))"
TITLE_PREFIX:="SSVC"
COMPILE_DATE:="Compiled `date -u`"
PDF_STYLING:=pdf-styling.yaml
BIBLIOGRAPHY:=$(SRC)/sources_ssvc.bib

PDF_OUT:=$(OUTDIR)/ssvc.pdf
HTML_OUT:=$(OUTDIR)/ssvc.html

EMOJI_REPLACEMENTS:=$(HOME)/emoji-replacements.sed

# we need
GFX=graphics
GFX_LINK=../$(GFX)

# Convert all files in this directory that have a .md suffix
SOURCE_DOCS := $(wildcard $(SRC)/*.md)

EXPORTED_DOCS=$(PDF_OUT) $(HTML_OUT)

# where to find things
RM:=/bin/rm
SED:=sed
PANDOC:=`which pandoc`

# HTML can handle emojis and not LaTeX commands, so the markdown files have emoji
# However, it is really hard to embed emoji into PDFs in a platform-independent way
# Apple Emoji font and Noto Emoji font are the two options, basically, and as of Apr 2022
# most devices seem to have one or the other.
# In general, LaTeX is bad at emojis, but the twemojis package might make it OK.
# However, twemojis is not a default package yet, so avoiding that for now.
# So the best available option is to temporarily replace them with LaTeX commands
# Pandoc will read from stdin if no input files are provided, so sed works inline.
REPLACE_EMOJI=$(SED) -f $(EMOJI_REPLACEMENTS) $(SOURCE_DOCS)



PANDOC_OPTIONS=--standalone \
	--citeproc \
	--bibliography=$(BIBLIOGRAPHY) \
	--metadata=title:$(TITLE) \
	--title-prefix=$(TITLE_PREFIX) \
  	--metadata=date:$(COMPILE_DATE) \
  	--metadata-file=$(PDF_STYLING) \

# --from should use gfm, but gfm+citations is not supported
# so this method should perhaps be considered slightly unstable.
# This citation syntax won't render on github
# but the @ citation syntax shouldn't interfere with @ mentions
# GFM only allows @ mentions in issues and pull requests
# https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown
# documentation for citation processing:
# https://pandoc.org/MANUAL.html#citations


PANDOC_PDF_OPTIONS=--to=pdf  \
	--from=markdown_github+citations+yaml_metadata_block+tex_math_dollars \
	--pdf-engine=xelatex \
	--table-of-contents \
  	-o $(PDF_OUT)

PANDOC_HTML_OPTIONS=--to=html \
	--self-contained \
	--from=markdown_github+citations+table_captions+implicit_figures+link_attributes  \
	-o $(HTML_OUT)


# Pattern-matching Rules

pdf : $(SOURCE_DOCS)
	@echo "Create temporary link so pandoc can find graphics"
	pushd .. && ln -s $(HOME)/$(GFX) $(GFX) && popd
	@echo "Replace emoji with text and convert to PDF"
	$(REPLACE_EMOJI) | $(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_PDF_OPTIONS)
	@echo "Remove temporary link to graphics"
	- $(RM) $(GFX_LINK)

html: $(SOURCE_DOCS)
	@echo "Create temporary link so pandoc can find graphics"
	pushd .. && ln -s $(HOME)/$(GFX) $(GFX) && popd
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_HTML_OPTIONS) $(SOURCE_DOCS)
	@echo "Remove temporary link to graphics"
	- $(RM) $(GFX_LINK)

# Targets and dependencies

.PHONY: all clean

all : pdf html

clean:
	- $(RM) $(EXPORTED_DOCS)