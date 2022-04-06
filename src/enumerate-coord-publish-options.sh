#!/bin/sh

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

