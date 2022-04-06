#!/bin/sh

# row numbers make change discussion a lot easier
i=1

# default output file in the SSVC Github file structure
out="../data/csvs/coord-triage-options_v2.csv"

# refuse to clobber existing file
if [ -e "$out" ] 
  then echo "File $out exists. Will not clobber. Exiting."
  exit 1
fi

#header row
echo "row,Public,Contacted,Report_Credibility,Cardinality,Engagement,Utility,Public_Safety_Impact,Priority(TODO)">$out

for ReportCredibility in no yes
  do for Cardinality in one multiple
    do for Engagement in active unresponsive
      do for Utility in laborious efficient "super effective"
        do for PublicSafetyImpact in minor huge
          do echo $i,no,yes,$ReportCredibility,$Cardinality,$Engagement,$Utility,$PublicSafetyImpact, >>$out 
          # for this tree, there is not much variation unless the vul is not already
          # Public and the reported has already tried to contact the vendor/supplier 
             i=$(($i+1))
        done
      done
    done
  done
done

for Contacted in yes no
  do for ReportCredibility in no yes
    do for Engagement in active unresponsive
      do echo $i,yes,$Contacted,$ReportCredibility,multiple,$Engagement,super effective,huge,coordinate >>$out 
             i=$(($i+1))
    done
  done
done #exceptions to already public where will still coordinate
for Contacted in yes no
  do for ReportCredibility in no yes
    do for Engagement in active unresponsive
      do for Utility in laborious efficient
        do echo $i,yes,$Contacted,$ReportCredibility,one,$Engagement,$Utility,minor,decline >>$out 
             i=$(($i+1))
      done
    done
  done
done #Decline for other situations where vul is already public


for ReportCredibility in no yes
  do for Engagement in active unresponsive
    do echo $i,no,no,$ReportCredibility,multiple,$Engagement,super effective,huge,coordinate >>$out 
             i=$(($i+1))
  done
done #exceptions to supplier/vendor not contacted by reporter but will still coordinate
for ReportCredibility in no yes
  do for Engagement in active unresponsive
    do for Utility in laborious efficient
      do echo $i,no,no,$ReportCredibility,one,$Engagement,$Utility,minor,decline >>$out 
             i=$(($i+1))
    done
  done
done #Decline for other situations where supplier / vendor not contacted 
