# Coordinator Publication Decision Tree

Suggested decision values for this decision are available in [CSV](../../data/csvs/ssvc_2_coord-publish.csv) and [PDF](../pdf/ssvc_2_coord-publish.pdf) formats.

<!-- 
<embed src="../../pdf/ssvc_2_coord-publish.pdf" alt="Suggested tree for a coordinator's publication decision" type="application/pdf"
style="width: 100%;"
height = "600" />
-->

```mermaid
---
title: Coordinator Publication Tree
---
flowchart LR
    si[Supplier<br/>Involvement]
    e1[Exploitation]
    e2[Exploitation]
    e3[Exploitation]
    si -->|fix ready| e1
    si -->|cooperative| e2
    si -->|uncooperative/<br/>unresponsive| e3
    va1[Value<br/>Added]
    va2[Value<br/>Added]
    va3[Value<br/>Added]
    e1 -->|none| va1
    e1 -->|PoC| va2
    e1 -->|active| va3
    va4[Value<br/>Added]
    va5[Value<br/>Added]
    va6[Value<br/>Added]
    e2 -->|none| va4
    e2 -->|PoC| va5
    e2 -->|active| va6
    va7[Value<br/>Added]
    va8[Value<br/>Added]
    va9[Value<br/>Added]
    e3 -->|none| va7
    e3 -->|PoC| va8
    e3 -->|active| va9
    
    p1[Publish]
    p2[Don't Publish]
    p3[Don't Publish]
    
    p4[Publish]
    p5[Don't Publish]
    p6[Don't Publish]
    
    p7[Publish]
    p8[Publish]
    p9[Don't Publish]
    
    p10[Publish]
    p11[Don't Publish]
    p12[Don't Publish]
    
    p13[Publish]
    p14[Don't Publish]
    p15[Don't Publish]
    
    p16[Publish]
    p17[Publish]
    p18[Don't Publish]
    
    p19[Publish]
    p20[Don't Publish]
    p21[Don't Publish]
    
    p22[Publish]
    p23[Publish]
    p24[Don't Publish]
    
    p25[Publish]
    p26[Publish]
    p27[Don't Publish]
        
    va1 -->|precedence| p1
    va1 -->|ampliative| p2
    va1 -->|limited| p3
    
    va2 -->|precedence| p4
    va2 -->|ampliative| p5
    va2 -->|limited| p6
    
    va3 -->|precedence| p7
    va3 -->|ampliative| p8
    va3 -->|limited| p9
    
    va4 -->|precedence| p10
    va4 -->|ampliative| p11
    va4 -->|limited| p12
    
    va5 -->|precedence| p13
    va5 -->|ampliative| p14
    va5 -->|limited| p15
    
    va6 -->|precedence| p16
    va6 -->|ampliative| p17
    va6 -->|limited| p18
    
    va7 -->|precedence| p19
    va7 -->|ampliative| p20
    va7 -->|limited| p21
    
    va8 -->|precedence| p22
    va8 -->|ampliative| p23
    va8 -->|limited| p24
    
    va9 -->|precedence| p25
    va9 -->|ampliative| p26
    va9 -->|limited| p27
    
        
        
    
    

```

## Table of Values

{{ read_csv('../../data/csvs/coord-publish-options.csv') }}

