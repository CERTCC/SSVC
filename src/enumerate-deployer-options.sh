#!/bin/sh

# row numbers make change discussion a lot easier
i=1

# default output file in the SSVC Github file structure
out="../data/csvs/deployer-options_v2_1.csv"

# refuse to clobber existing file
if [ -e "$out" ] 
  then echo "File $out exists. Will not clobber. Exiting."
  exit 1
fi

#header row
echo "row,Exploitation,Exposure,Automatable,HumanImpact,Priority(TODO)">$out

for Exploitation in none PoC active
  do for Exposure in small controlled open
    do for Automatable in no yes
      do for HumanImpact in low medium high "very high"
          do echo $i,$Exploitation,$Exposure,$Automatable,$HumanImpact,>>$out
             i=$(($i+1))
      done
    done
  done
done

