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

sed -f emoji-replacements.sed $src/*md | \
pandoc --standalone \
  --from=markdown_github+citations+yaml_metadata_block+tex_math_dollars \
  --to=pdf \
  --citeproc \
  --pdf-engine=xelatex \
  --bibliography="$src/sources_ssvc.bib" \
  --table-of-contents \
  -M title="Prioritizing vulnerability response: A stakeholder-specific vulnerability categorization (Version 2.0)" \
  -T "SSVC" \
  -M date="Compiled `date -u`" \
  --metadata-file=pdf-styling.yaml \
  -o "ssvc_v2-0_`date -u +"%Y-%m-%d"`.pdf" \

# --from should use gfm, but gfm+citations is not supported
# so this method should perhaps be considered slightly unstable. 
# This citation syntax won't render on github
# but the @ citation syntax shouldn't interfere with @ mentions
# GFM only allows @ mentions in issues and pull requests
# https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown
# documentation for citation processing:
# https://pandoc.org/MANUAL.html#citations

