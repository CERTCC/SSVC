#!/bin/sh
src="./md_src_files"

pandoc --standalone --from=markdown_github+citations+yaml_metadata_block \
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
   $src/*md

# --from should use gfm, but gfm+citations is not supported
# so this method should perhaps be considered slightly unstable. 
# This citation syntax won't render on github
# but the @ citation syntax shouldn't interfere with @ mentions
# GFM only allows @ mentions in issues and pull requests
# https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown
# documentation for citation processing:
# https://pandoc.org/MANUAL.html#citations

