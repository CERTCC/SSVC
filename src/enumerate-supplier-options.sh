#!/bin/sh

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

