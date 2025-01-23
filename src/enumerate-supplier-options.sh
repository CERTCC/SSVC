#!/bin/sh

#
# Copyright (c) 2025 Carnegie Mellon University and Contributors.
# - see Contributors.md for a full list of Contributors
# - see ContributionInstructions.md for information on how you can Contribute to this project
# Stakeholder Specific Vulnerability Categorization (SSVC) is
# licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
# with this Software or contact permission@sei.cmu.edu for full terms.
# Created, in part, with funding and support from the United States Government
# (see Acknowledgments file). This program may include and/or can make use of
# certain third party source code, object code, documentation and other files
# (“Third Party Software”). See LICENSE.md for more details.
# Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
# U.S. Patent and Trademark Office by Carnegie Mellon University
#

# row numbers make change discussion a lot easier
i=1

# default output file in the SSVC Github file structure
out="../data/csvs/supplier-options_v2.csv"

# refuse to clobber existing file
if [ -e "$out" ] 
  then echo "File $out exists. Will not clobber. Exiting."
  exit 1
fi

#header row
echo "row,Exploitation,Utility,Technical Impact,Public-Safety Impact,Priority(TODO)">$out

for Exploitation in none PoC active
  do for Utility in laborious efficient "super effective"
    do for Technical in partial total
      do for PublicSafety in minimal significant
          do echo $i,$Exploitation,$Utility,$Technical,$PublicSafety,>>$out 
             i=$(($i+1))
      done
    done
  done
done

