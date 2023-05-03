#!/bin/sh
pandoc --standalone --from=markdown_github+citations  --to=html \
  --filter pandoc-citeproc \
  --bibliography="version_1/sources_ssvc.bib" \
  -M title="Prioritizing vulnerability response: A stakeholder-specific vulnerability categorization (version 1.1)" \
  -T "SSVC" \
  -M author="Jonathan M. Spring; Eric Hatleback; Allen Householder; Art Manion; Deana Shick" \
  -M date="Published 2020-06-25; compiled `date -u`" \
  -M reference-section-title="References" \
  -M link-citations="true" \
  -o ssvc_v1-1.html \
   version_1/*md

# --from should use gfm, but gfm+citations is not supported
# so this method should perhaps be considered slightly unstable. 
# This citation syntax won't render on github
# but the @ citation syntax shouldn't interfere with @ mentions
# GFM only allows @ mentions in issues and pull requests
# https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown
# documentation for citation processing:
# https://pandoc.org/MANUAL.html#citations

