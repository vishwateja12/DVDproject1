# DVD PROJECT 1



## Leakage Estimation Using Single Mosfet Leakages



   - BANALA VISHWA TEJA REDDY - 2020102058
     - NetList and VLSI part leakages
   - KETHU SESHA SARATH REDDY - 2020102028
     - NetList and VLSI part leakages
   - SANGEETHAM DEEPAK - 2020102063
     - Python scripting part
   - MERUGU NANDITHA - 2020102061
     - python scripting part





 ###                           STAGE 1 :- Single Transistor Leakages



#### AIM : NMOS_ON,PMOS_ON,NMOS_OFF,PMOS_OFF Leakages

##### Below Shown are the leakges for the NMOS,PMOS

![Maximum gate oxide and subthreshold leakage current states in nMOS and... |  Download Scientific Diagram](https://www.researchgate.net/publication/3338083/figure/fig3/AS:671509282553869@1537111697394/Maximum-gate-oxide-and-subthreshold-leakage-current-states-in-nMOS-and-pMOS-transistors.png)

In A Both the NMOS and PMOS are in ON stage and the major leakages are the gate and body leakages. where in B Both the PMOS and NMOS are in OFF stage the major leakage we can see are sub threshold leakage with a less gate and body leakages.

Now we code these in the NGSpice to look up on what are the values of the single transistor leakages 

###### CODE SNIPPET :

.include 22nm_HP.pm
.option GMIN=1e-020 ABSTOL=1e-18 temp=25

.param Lmin=22n
.param Wmin=22n
.param Ldiff=44n

M1 drain gate source body nmos W={Wmin} L={Lmin} AS={Wmin*Ldiff} AD={Wmin*Ldiff} PS={2*(Ldiff+Wmin)} PD={2*(Ldiff+Wmin)}
Vd 	drain	  0     0
Vg 	gate	  alim	0
Vs 	source	0		  0
Vb 	body	  0		  0

Vdd alim	  0

.control
echo "" > W1nmos_ON_simulation_results.txt
let voltage=0
let Vddbasic=0.8
while voltage le Vddbasic
  let voltage = voltage + 0.01
  alter Vdd = voltage
  dc TEMP 25 50 60
  print @M1[W] abs(V(alim)) V(drain) V(gate) V(source) V(body) I(Vd) I(Vg) I(Vs) I(Vb)
  let i = @M1[W]
  echo "25" "$&i" "$&voltage" "$&V(drain)" "$&V(source)" "$&V(gate)" "$&V(body)" "$&I(Vd)" "$&I(Vg)" "$&I(Vs)" "$&I(Vb)" >> W1nmos_ON_simulation_results.txt
end
.endc
.end



The above shown case is for nmos on and we saved all these values into text file using echo command and saved them in matrix format using python script.

Eg : Text file

25 2.2E-08 0.01 0 0 0.01 0 1.26392E-15 -2.52592E-15 1.26392E-15 1.44925E-18
25 2.2E-08 0.02 0 0 0.02 0 2.31438E-15 -4.6367E-15 2.31438E-15 3.00352E-18
25 2.2E-08 0.03 0 0 0.03 0 3.16264E-15 -6.31001E-15 3.16264E-15 4.6677E-18
25 2.2E-08 0.04 0 0 0.04 0 3.81955E-15 -7.61279E-15 3.81955E-15 6.44683E-18
25 2.2E-08 0.05 0 0 0.05 0 4.29559E-15 -8.65119E-15 4.29559E-15 8.34614E-18
25 2.2E-08 0.06 0 0 0.06 0 4.60089E-15 -9.26206E-15 4.60089E-15 1.0371E-17
25 2.2E-08 0.07 0 0 0.07 0 4.74528E-15 -9.47315E-15 4.74528E-15 1.25271E-17
25 2.2E-08 0.08 0 0 0.08 0 4.7383E-15 -9.44423E-15 4.7383E-15 1.48202E-17
25 2.2E-08 0.09 0 0 0.09 0 4.58937E-15 -9.16329E-15 4.58937E-15 1.72563E-17
25 2.2E-08 0.1 0 0 0.1 0 4.3079E-15 -8.69784E-15 4.3079E-15 1.98415E-17
25 2.2E-08 0.11 0 0 0.11 0 3.90367E-15 -7.86936E-15 3.90367E-15 2.25825E-17
25 2.2E-08 0.12 0 0 0.12 0 3.38763E-15 -6.85038E-15 3.38763E-15 2.54858E-17
25 2.2E-08 0.13 0 0 0.13 0 2.77419E-15 -5.70839E-15 2.77419E-15 2.85585E-17
25 2.2E-08 0.14 0 0 0.14 0 2.08882E-15 -4.19737E-15 2.08882E-15 3.18077E-17
25 2.2E-08 0.15 0 0 0.15 0 1.40278E-15 -2.68636E-15 1.40278E-15 3.52411E-17
25 2.2E-08 0.16 0 0 0.16 0 1.0132E-15 -2.0364E-15 1.0132E-15 3.88664E-17



just run the net file inside single transitor and the pmos off and on or nmos off and on by changing the widths and saving it in respective text files. the text files are saved inside the folders and we can look up into them while using it in expectations.

![Screenshot from 2024-03-27 21-25-47](/home/vishwa/Pictures/Screenshot from 2024-03-27 21-25-47.png)

These files are filled with netlists and the respective text files



###                  STAGE 2 : NStack and PStack Intermediate Voltages



#### AIM : NStack,PStack Intermediate Voltages to estimate the leakages in stacks



​           For Nstack and Pstack there will be 4 different inputs as 00,01,10,11 and the intermediate voltages are saved in the text files with leakages

**CODE :**

.include 22nm_HP.pm
.options GMIN=1e-020 ABSTOL=1e-18

.param Lmin=22n
.param Wmin=22n
.param Ldiff=44n

M1 D1 G1 S1 B1 nmos W={Wmin} L={Lmin} AS={Wmin*Ldiff} AD={Wmin*Ldiff} PS={2*(Ldiff+Wmin)} PD={2*(Ldiff+Wmin)}
M2 S1 G2 S2 B2 nmos W={Wmin} L={Lmin} AS={Wmin*Ldiff} AD={Wmin*Ldiff} PS={2*(Ldiff+Wmin)} PD={2*(Ldiff+Wmin)}
Vd 	D1	  0     0.8
Vg1 	G1	  0	0
Vg2 	G2	  0	0
Vs 	S2	0		  0
Vb1 	B1	  S1		  0
Vb2 	B2	  S2		  0


.control
echo "" > nmos_00.txt
foreach Win 22n 44n 66n 88n 132n 176n
    alter M1 W {$Win}
	alter M1 AS {$Win* L} 
	alter M1 AD {$Win* L}
	alter M1 PS {2*($Win + L)}
	alter M1 PD {2*($Win + L)}

	alter M2 W {$Win} 
	alter M2 AS {$Win* L} 
	alter M2 AD {$Win* L}
	alter M2 PS {2*($Win + L)}
	alter M2 PD {2*($Win + L)}
	
	dc TEMP 25 50 60
	let i1 = @M1[W]
	let i2 = @M2[W]
	let leakage_body = abs(I(vb1))+abs(I(vb2))
	let leakage_gate = abs(I(vg1))+abs(I(vg2))
	let leakage_sub = abs(I(vs))
	print @M1[W] @M2[W] V(D1) V(S1) V(G1) V(G2) V(S2) V(B1) V(B2) I(Vd) I(Vg1) I(Vg2) I(Vs) I(Vb1) I(Vb2) leakage_body leakage_gate leakage_sub
	echo "25" "$&i1" "$&V(D1)" "$&V(S1)" "$&V(G1)" "$&V(B1)" "$&i2" "$&V(S1)" "$&V(S2)" "$&V(G2)" "$&V(B2)" >> nmos_00.txt
end
.endc
.end

Above is an example code for the stack of nmos with 00 input. In 00 and 01 and 10 cases there is no channel so the vdd is kept at the top and gnd at the bottom source of nmos and for the case of 11 both the ends are kept at gnd as there is a channel simillar way for 00 case in pmos stack both the ends at vdd and in other cases vds is kept at negative vdd and will look for the leakages and printed in text files

As in the case of atleast 1 transistor is off then the other transister intermediate voltage is updated to make the sub threshold leakage unchanged.

**Below is the example text file for nstack with intermediate voltages :**

**vn00 = [0.133388,0.13336,0.133359,0.133359,0.133358,0.133358]**
**vn01 = [2.07744E-05,2.19535E-05,2.33051E-05,2.39811E-05,2.46572E-05,2.49954E-05]**
**vn10 = [0.666334,0.666317,0.666318,0.666319,0.666319,0.66632]**
**vn11 = [2.86192E-08,3.91613E-08,4.15407E-08,4.27302E-08,4.39197E-08,4.45144E-08]**

As this concludes we manually checked the leakages of each gate body and subthreshold and verified with the printed values from netlist.



###        STAGE 3 : Estimation of the leakages of FA circuit of **74182** 





![img](https://web.eecs.umich.edu/~jhayes/iscas.restore/74182gates.gif)

We go through the stage in 3 parts Verifying each of the gates as OR,NOR,AND,NOT gates leakages with the expected values in python.

* PART-1 : Each gates verification
* PART-2 : design the FA circuit as netlist and get the leakages
* PART-3 : FInal look up into the FA leakage estimation



####                                                                         PART-1 



#### AND GATE :



CODE :

.SUBCKT AND A0 A1 out vddrail gndrail

    Mp1 D1 A0 vddrail vddrail pmos W={Wmin} L={Lmin} AS={Wmin*Ldiff} AD={Wmin*Ldiff} PS={2*(Ldiff+Wmin)} PD={2*(Ldiff+Wmin)}
    Mp2 D1 A1 vddrail vddrail pmos W={Wmin} L={Lmin} AS={Wmin*Ldiff} AD={Wmin*Ldiff} PS={2*(Ldiff+Wmin)} PD={2*(Ldiff+Wmin)}
    Mp3 out D1 vddrail vddrail pmos W={2*Wmin} L={Lmin} AS={2*Wmin*Ldiff} AD={2*Wmin*Ldiff} PS={2*(Ldiff+2*Wmin)} PD={2*(Ldiff+2*Wmin)}
    
    Mn1 D1 A0 S1 S1 nmos W={2*Wmin} L={Lmin} AS={2*Wmin*Ldiff} AD={2*Wmin*Ldiff} PS={2*(Ldiff+2*Wmin)} PD={2*(Ldiff+2*Wmin)}
    Mn2 S1 A1 gndrail gndrail nmos W={2*Wmin} L={Lmin} AS={2*Wmin*Ldiff} AD={2*Wmin*Ldiff} PS={2*(Ldiff+2*Wmin)} PD={2*(Ldiff+2*Wmin)}
    Mn3 out D1 gndrail gndrail nmos W={Wmin} L={Lmin} AS={Wmin*Ldiff} AD={Wmin*Ldiff} PS={2*(Ldiff+Wmin)} PD={2*(Ldiff+Wmin)}


.ENDS



The W/L values are optimised to make sure that the transistors are accomodated to give the current that flows as sub treshold currents as we make same at vdd and vss to be same and the making pmos/nmos ratio to be approximately 2 making this there is no need of external leakages from gates to match up with the sub treshold.

![Screenshot from 2024-03-27 21-49-58](/home/vishwa/Pictures/Screenshot from 2024-03-27 21-49-58.png)

Like the above image all the leakages are matched using the python code expectations.

#### NOT GATE :



CODE :



.SUBCKT NOT A0 out vddrail gndrail

    Mp1 out A0 vddrail vddrail pmos W={2*Wmin} L={Lmin} AS={2*Wmin*Ldiff} AD={2*Wmin*Ldiff} PS={2*(Ldiff+2*Wmin)} PD={2*(Ldiff+2*Wmin)}
    Mn1 out A0 gndrail gndrail nmos W={Wmin} L={Lmin} AS={Wmin*Ldiff} AD={Wmin*Ldiff} PS={2*(Ldiff+Wmin)} PD={2*(Ldiff+Wmin)}

.ENDS



The W/L values are optimised to make sure that the transistors are accomodated to give the current that flows as sub treshold currents as we make same at vdd and vss to be same and the making pmos/nmos ratio to be approximately 2 making this there is no need of external leakages from gates to match up with the sub treshold.

#### NOR GATE :



CODE :



.SUBCKT NOR A0 A1 out vddrail gndrail
    
    Mp1 Dp1 A0 vddrail vddrail pmos W={8*Wmin} L={Lmin} AS={8*Wmin*Ldiff} AD={8*Wmin*Ldiff} PS={2*(Ldiff+8*Wmin)} PD={2*(Ldiff+8*Wmin)}
    Mp2 out A1 Dp1 Dp1 pmos W={8*Wmin} L={Lmin} AS={8*Wmin*Ldiff} AD={8*Wmin*Ldiff} PS={2*(Ldiff+8*Wmin)} PD={2*(Ldiff+8*Wmin)}
    
    Mn1 out A0 gndrail gndrail  nmos W={Wmin} L={Lmin} AS={Wmin*Ldiff} AD={Wmin*Ldiff} PS={2*(Ldiff+Wmin)} PD={2*(Ldiff+Wmin)}
    Mn2 out A1 gndrail gndrail  nmos W={Wmin} L={Lmin} AS={Wmin*Ldiff} AD={Wmin*Ldiff} PS={2*(Ldiff+Wmin)} PD={2*(Ldiff+Wmin)}

.ENDS



The W/L values are optimised to make sure that the transistors are accomodated to give the current that flows as sub treshold currents as we make same at vdd and vss to be same and the making pmos/nmos ratio to be approximately 2 making this there is no need of external leakages from gates to match up with the sub treshold.

#### OR GATE :



CODE :



.SUBCKT OR A0 A1 out vddrail gndrail

    Mp1 Dp1 A0 vddrail vddrail pmos W={8*Wmin} L={Lmin} AS={8*Wmin*Ldiff} AD={8*Wmin*Ldiff} PS={2*(Ldiff+8*Wmin)} PD={2*(Ldiff+8*Wmin)}
    Mp2 D1 A1 Dp1 Dp1 pmos W={8*Wmin} L={Lmin} AS={8*Wmin*Ldiff} AD={8*Wmin*Ldiff} PS={2*(Ldiff+8*Wmin)} PD={2*(Ldiff+8*Wmin)}
    Mp3 out D1 vddrail vddrail pmos W={2*Wmin} L={Lmin} AS={2*Wmin*Ldiff} AD={2*Wmin*Ldiff} PS={2*(Ldiff+2*Wmin)} PD={2*(Ldiff+2*Wmin)}
    
    Mn1 D1 A0 gndrail gndrail  nmos W={Wmin} L={Lmin} AS={Wmin*Ldiff} AD={Wmin*Ldiff} PS={2*(Ldiff+Wmin)} PD={2*(Ldiff+Wmin)}
    Mn2 D1 A1 gndrail gndrail  nmos W={Wmin} L={Lmin} AS={Wmin*Ldiff} AD={Wmin*Ldiff} PS={2*(Ldiff+Wmin)} PD={2*(Ldiff+Wmin)}
    Mn3 out D1 gndrail gndrail nmos W={Wmin} L={Lmin} AS={Wmin*Ldiff} AD={Wmin*Ldiff} PS={2*(Ldiff+Wmin)} PD={2*(Ldiff+Wmin)}

.ENDS



The W/L values are optimised to make sure that the transistors are accomodated to give the current that flows as sub treshold currents as we make same at vdd and vss to be same and the making pmos/nmos ratio to be approximately 2 making this there is no need of external leakages from gates to match up with the sub treshold.





####   PART-2 FA CIrcuit and the leakages



The Circuit we used to create Full FA Circuit run the netlist to print the leakages and outputs



XAND1 P0 G0 w1 vddrail gndrail AND
XNOT1 Cn w2 vddrail gndrail NOT
XAND2 G0 w2 w3 vddrail gndrail AND
XNOR1 w1 w3 cnx vddrail gndrail NOR

XAND3 P1 G1 w4 vddrail gndrail AND
XAND4 w1 G1 w5 vddrail gndrail AND
XAND5 w3 G1 w6 vddrail gndrail AND
XOR1 w4 w5 w7 vddrail gndrail OR
XNOR2 w7 w6 cny vddrail gndrail NOR

XAND6 P2 G2 w8 vddrail gndrail AND
XAND7 w4 G2 w9 vddrail gndrail AND
XAND8 G1 G2 w10 vddrail gndrail AND
XAND9 w1 w10 w11 vddrail gndrail AND
XAND10 w3 w10 w12 vddrail gndrail AND
XOR3 w8 w9 w13 vddrail gndrail OR
XOR4 w11 w12 w14 vddrail gndrail OR
XNOR3 w13 w14 cnz vddrail gndrail OR

XAND11 P3 G3 w15 vddrail gndrail AND
XAND12 w8 G3 w16 vddrail gndrail AND
XAND13 P1 G3 w17 vddrail gndrail AND
XAND14 w17 w10 w18 vddrail gndrail AND
XAND15 G0 G3 w19 vddrail gndrail AND
XAND16 w10 w19 w20 vddrail gndrail AND
XOR5 w15 w16 w21 vddrail gndrail OR
XOR6 w18 w20 w22 vddrail gndrail OR
XOR7 w21 w22 G vddrail gndrail OR

XOR8 P0 P1 w23 vddrail gndrail OR
XOR9 P2 P3 w24 vddrail gndrail OR
XOR10 w23 w24 P vddrail gndrail OR



The leakages we got after running the netlist file is given below

![Screenshot from 2024-03-27 21-58-56](/home/vishwa/Pictures/Screenshot from 2024-03-27 21-58-56.png)

The right one shows the python output of the leakage in the estimation stage

### PYTHON CODE RUNNING 

![Screenshot from 2024-03-27 22-08-36](/home/vishwa/Pictures/Screenshot from 2024-03-27 22-08-36.png)

With the above function that determined we can find the Final leakage of the the FA circuit above 0's shown are the inputs of the Final Circuit.



###                                                          HOW TO RUN THE CODES



1. FInd the FInal_circuit.net inside zip and give inputs as you wish at the voltage sources
2. Go to Final_model.py and give the same inputs that you gave in the Final_circuit.net and compare the leakages from both of them.

### GIT HUB REPO :- https://github.com/vishwateja12/DVDproject1.git

 







