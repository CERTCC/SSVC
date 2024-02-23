# Bootstrapping SSVC Summary

Using SSVC to prioritize vulnerability response requires a few steps. The steps are:

{% include-markdown "howto/bootstrap/_steps_table.md" %}

We covered each of these in the previous sections, see the links in the table above for more information.

The diagram below shows the complete process of using SSVC.


```mermaid
flowchart TD
start([Start])
subgraph prep [Prepare to use SSVC]
	dcd{{Choose Decision to Model}}
	d[/Decision/]
    l4((1))
	subgraph outcomes [Define Outcomes]
		oc1[/Use available<br/>outcome sets?\]
		dos{{Define Outcome Sets}}
		oss[\Outcome Sets/]
		cos{{Choose Outcome Set}}
		os[/Outcome Set/]
	end
    l5((1))
	subgraph decisionpoints [Define Inputs]
		dp1[/Use available<br/>decision points?\]
		ddp{{Define Decision Points}}
		dpt[\Decision Points/]
		cdp{{Choose Decision Points}}
		dps[/Decision Point Set/]
	end
    l6((1))
	subgraph dataeng [Data Mapping]
		dd1[/Use existing data?\]
		dpm[/Data Map/]
		dp2d{{Map Decision Points to Data}}
		dd{{Define Data}}
		ddf[/Data Definition/]
	end
    l7((1))
	subgraph policy [Policy Development]
		dfp{{Define Policy}}
		p[/Policy/]
	end
    subgraph gov [Governance]
        eg{{Establish Governance Process}}
        gp[[Governance Process]]
    end
    l3((1))

end
subgraph dataops [Data Operations]
	cd[Collect Data]
	vd[/Vulnerability Data/]
	ed[/Environment Data/]
    dt[\Available Data/]

end
subgraph runtime [Use SSVC]
	mdp[[Apply Decision Point Mapping to Data]]
	dp[/Decision Point Values/]
	ap[[Apply Policy]]
	oc[/Outcome/]
end
r[Vulnerability Response]
start --> dcd
start --> eg
eg --> gp
gp -->|ongoing| gp
gp --> l3

dcd --> d
l4 --> oc1
d --> oc1
dps --> dd1
oc1 -->|y| oss
oc1 -->|n| dos
dp1 -->|y| dpt
dp1 -->|n| ddp
dd1 -->|y| ddf
dd1 -->|n| dd
ddp --> dpt
dos --> oss
dpt --> cdp
cdp --> dps
cos --> os
oss --> cos
l7 --> dfp
os --> dfp
os --> dp1
l5 --> dp1
d --> dp1
dps --> dp2d
dp2d --> dpm
dps --> dfp
dpm --> mdp
dd --> ddf
ddf --> dp2d
ddf --> cd
cd --> cd
cd --> vd
cd --> ed
vd --> dt
ed --> dt
dt --> mdp
mdp --> dp
dfp --> p
p --> ap
dp --> ap
ap --> oc
oc --> r
r --> l1((2))
l2((2)) --> cd
l6 --> dd1
```

