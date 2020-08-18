#!/bin/sh
pandoc --standalone --from=gfm --to=html \
  -M title="Prioritizing vulnerability response: A stakeholder-specific vulnerability categorization (version 1.1)" \
  -T "SSVC" \
  -M author="Jonathan M. Spring; Eric Hatleback; Allen Householder; Art Manion; Deana Shick" \
  -M date="Published 2020-06-25; compiled `date -u`" \
  -o ssvc_v1-1.html version_1/*md


