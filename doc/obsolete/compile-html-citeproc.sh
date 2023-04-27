#!/bin/sh
src="./md_src_files"

pandoc --self-contained \
  --from=markdown_github+citations+table_captions+implicit_figures+link_attributes  \
  --to=html \
  --citeproc \
  --bibliography="$src/sources_ssvc.bib" \
  -M title="Prioritizing vulnerability response: A stakeholder-specific vulnerability categorization (DRAFT version 2.0)" \
  -T "SSVC" \
  -M author="Jonathan M. Spring; Eric Hatleback; Allen D. Householder; Art Manion; Madison Oliver; Vijay Sarvapalli; Deana Shick; Laurie Tyzenhaus" \
  -M date="Compiled `date -u`" \
  -o ssvc_v2-0.html \
   $src/*md

# --from should use gfm, but gfm+citations is not supported
# so this method should perhaps be considered slightly unstable. 
# This citation syntax won't render on github
# but the @ citation syntax shouldn't interfere with @ mentions
# GFM only allows @ mentions in issues and pull requests
# https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown
# documentation for citation processing:
# https://pandoc.org/MANUAL.html#citations

