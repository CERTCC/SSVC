#!/bin/sh

# row numbers make change discussion a lot easier
i=1

# default output file in the SSVC Github file structure
out="../data/csvs/deployer-options_v2.csv"

# refuse to clobber existing file
if [ -e "$out" ] 
  then echo "File $out exists. Will not clobber. Exiting."
  exit 1
fi

#header row
echo "row,Exploitation,Exposure,Utility,Well-being and Mission Impact,Priority(TODO)">$out

for Exploitation in none PoC active
  do for Exposure in small controlled open
    do for Utility in laborious efficient "super effective"
      do for WellnessMissionImpact in low medium high "very high"
          do echo $i,$Exploitation,$Exposure,$Utility,$WellnessMissionImpact,>>$out 
             i=$(($i+1))
      done
    done
  done
done

