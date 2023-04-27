#!/bin/sh
src="./md_src_files"

# HTML can handle emojis and not LaTeX commands, so the markdown files have emoji
# However, it is really hard to embed emoji into PDFs in a platform-independent way
# Apple Emoji font and Noto Emoji font are the two options, basically, and as of Apr 2022
# most devices seem to have one or the other. 
# In general, LaTeX is bad at emojis, but the twemojis package might make it OK. 
# However, twemojis is not a default package yet, so avoiding that for now.
# So the best available option is to temporarily replace them with LaTeX commands
# Pandoc will read from stdin if no input files are provided, so sed works inline.

# versioning
# need a better way of automatically updating version numbers
major="2"
minor="0"
# these have the common meanings from semantic versioning
# major should be incremented with content changes that introduce incompatibilities
# minor should be incremented for meaningful changes that do not break compatibility
fix="5"
# fix version needs to be incremented with every commit

#versioning across different content is a bit complicated.
# The PDF major.minor should match any schema, tree, or other supporting document version
# This means if the major.minor version changes, the schemas need a numbering change
# The fix version for the schema and the PDF document may mismatch

sed -f emoji-replacements.sed $src/*md | \
pandoc --standalone \
  --from=markdown_github+citations+yaml_metadata_block+tex_math_dollars \
  --to=pdf \
  --citeproc \
  --pdf-engine=xelatex \
  --bibliography="$src/sources_ssvc.bib" \
  --table-of-contents \
  -M title="Prioritizing Vulnerability Response: A Stakeholder-Specific Vulnerability Categorization (SSVC version $major.$minor.$fix)" \
  -T "SSVC" \
  -M date="Compiled `date -u`" \
  --metadata-file=pdf-styling.yaml \
  -o "ssvc_$major-$minor-$fix.pdf" \

# --from should use gfm, but gfm+citations is not supported
# so this method should perhaps be considered slightly unstable. 
# This citation syntax won't render on github
# but the @ citation syntax shouldn't interfere with @ mentions
# GFM only allows @ mentions in issues and pull requests
# https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown
# documentation for citation processing:
# https://pandoc.org/MANUAL.html#citations

