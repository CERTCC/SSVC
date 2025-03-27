#!/bin/sh

#
# Copyright (c) 2025 Carnegie Mellon University.
# NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
# ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
# CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
# NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
# MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
# OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
# ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
# PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
# Licensed under a MIT (SEI)-style license, please see LICENSE or contact
# permission@sei.cmu.edu for full terms.
# [DISTRIBUTION STATEMENT A] This material has been approved for
# public release and unlimited distribution. Please see Copyright notice
# for non-US Government use and distribution.
# This Software includes and/or makes use of Third-Party Software each
# subject to its own license.
# DM24-0278
#

# row numbers make change discussion a lot easier
i=1

# default output file in the SSVC Github file structure
out="../data/csvs/coord-publish-options_v2.csv"

# refuse to clobber existing file
if [ -e "$out" ] 
  then echo "File $out exists. Will not clobber. Exiting."
  exit 1
fi

#header row
echo "row,Supplier involvement,Exploitation,Value added,Priority(TODO)">$out

for SupplierInvolvement in "fix ready" cooperative "uncoop/unresponsive"
  do for Exploitation in none PoC active
    do for ValueAdded in precedence ampliative limited
        do echo $i,$SupplierInvolvement,$Exploitation,$ValueAdded,>>$out 
           i=$(($i+1))
    done
  done
done

