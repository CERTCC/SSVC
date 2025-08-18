# Title


```mermaid
graph LR
n1(( ))
subgraph s1["ssvc:SINV:1.0.0"]
FR_L0([FR])
C_L0([C])
UU_L0([UU])
end
subgraph s2["ssvc:E:1.1.0"]
FR_N_L1([N])
C_N_L1([N])
FR_P_L1([P])
UU_N_L1([N])
C_P_L1([P])
FR_A_L1([A])
UU_P_L1([P])
C_A_L1([A])
UU_A_L1([A])
end
subgraph s3["ssvc:PVA:1.0.0"]
FR_N_L_L2([L])
C_N_L_L2([L])
FR_P_L_L2([L])
FR_N_A_L2([A])
UU_N_L_L2([L])
C_P_L_L2([L])
FR_A_L_L2([L])
C_N_A_L2([A])
FR_P_A_L2([A])
FR_N_P_L2([P])
UU_P_L_L2([L])
C_A_L_L2([L])
UU_N_A_L2([A])
C_P_A_L2([A])
FR_A_A_L2([A])
C_N_P_L2([P])
FR_P_P_L2([P])
UU_A_L_L2([L])
UU_P_A_L2([A])
C_A_A_L2([A])
UU_N_P_L2([P])
C_P_P_L2([P])
FR_A_P_L2([P])
UU_A_A_L2([A])
UU_P_P_L2([P])
C_A_P_L2([P])
UU_A_P_L2([P])
end
subgraph s4["ssvc:PUBLISH:1.0.0"]
FR_N_L_N_L3([N])
C_N_L_N_L3([N])
FR_P_L_N_L3([N])
FR_N_A_N_L3([N])
UU_N_L_N_L3([N])
C_P_L_N_L3([N])
FR_A_L_N_L3([N])
C_N_A_N_L3([N])
FR_P_A_N_L3([N])
FR_N_P_P_L3([P])
UU_P_L_N_L3([N])
C_A_L_N_L3([N])
UU_N_A_N_L3([N])
C_P_A_N_L3([N])
FR_A_A_P_L3([P])
C_N_P_P_L3([P])
FR_P_P_P_L3([P])
UU_A_L_P_L3([P])
UU_P_A_P_L3([P])
C_A_A_P_L3([P])
UU_N_P_P_L3([P])
C_P_P_P_L3([P])
FR_A_P_P_L3([P])
UU_A_A_P_L3([P])
UU_P_P_P_L3([P])
C_A_P_P_L3([P])
UU_A_P_P_L3([P])
end
n1 --- FR_L0
n1 --- C_L0
n1 --- UU_L0
FR_L0 --- FR_N_L1
FR_N_L1 --- FR_N_L_L2
FR_N_L_L2 --- FR_N_L_N_L3
C_L0 --- C_N_L1
C_N_L1 --- C_N_L_L2
C_N_L_L2 --- C_N_L_N_L3
FR_L0 --- FR_P_L1
FR_P_L1 --- FR_P_L_L2
FR_P_L_L2 --- FR_P_L_N_L3
FR_N_L1 --- FR_N_A_L2
FR_N_A_L2 --- FR_N_A_N_L3
UU_L0 --- UU_N_L1
UU_N_L1 --- UU_N_L_L2
UU_N_L_L2 --- UU_N_L_N_L3
C_L0 --- C_P_L1
C_P_L1 --- C_P_L_L2
C_P_L_L2 --- C_P_L_N_L3
FR_L0 --- FR_A_L1
FR_A_L1 --- FR_A_L_L2
FR_A_L_L2 --- FR_A_L_N_L3
C_N_L1 --- C_N_A_L2
C_N_A_L2 --- C_N_A_N_L3
FR_P_L1 --- FR_P_A_L2
FR_P_A_L2 --- FR_P_A_N_L3
FR_N_L1 --- FR_N_P_L2
FR_N_P_L2 --- FR_N_P_P_L3
UU_L0 --- UU_P_L1
UU_P_L1 --- UU_P_L_L2
UU_P_L_L2 --- UU_P_L_N_L3
C_L0 --- C_A_L1
C_A_L1 --- C_A_L_L2
C_A_L_L2 --- C_A_L_N_L3
UU_N_L1 --- UU_N_A_L2
UU_N_A_L2 --- UU_N_A_N_L3
C_P_L1 --- C_P_A_L2
C_P_A_L2 --- C_P_A_N_L3
FR_A_L1 --- FR_A_A_L2
FR_A_A_L2 --- FR_A_A_P_L3
C_N_L1 --- C_N_P_L2
C_N_P_L2 --- C_N_P_P_L3
FR_P_L1 --- FR_P_P_L2
FR_P_P_L2 --- FR_P_P_P_L3
UU_L0 --- UU_A_L1
UU_A_L1 --- UU_A_L_L2
UU_A_L_L2 --- UU_A_L_P_L3
UU_P_L1 --- UU_P_A_L2
UU_P_A_L2 --- UU_P_A_P_L3
C_A_L1 --- C_A_A_L2
C_A_A_L2 --- C_A_A_P_L3
UU_N_L1 --- UU_N_P_L2
UU_N_P_L2 --- UU_N_P_P_L3
C_P_L1 --- C_P_P_L2
C_P_P_L2 --- C_P_P_P_L3
FR_A_L1 --- FR_A_P_L2
FR_A_P_L2 --- FR_A_P_P_L3
UU_A_L1 --- UU_A_A_L2
UU_A_A_L2 --- UU_A_A_P_L3
UU_P_L1 --- UU_P_P_L2
UU_P_P_L2 --- UU_P_P_P_L3
C_A_L1 --- C_A_P_L2
C_A_P_L2 --- C_A_P_P_L3
UU_A_L1 --- UU_A_P_L2
UU_A_P_L2 --- UU_A_P_P_L3
```