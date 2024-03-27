## This is the script file for our final submission of project-1

# initialsing some required variables

## Temp │   M1[W] │   V-sweep │   V(drain) │   V(source) │   V(gate) │   V(body) │        I(Vd) │       I(Vg) │       I(Vs) │       I(Vb) │

temp = 0
wmin = 1
Valim = 2
Vd = 3
Vs = 4
Vg = 5
Vb = 6
Id = 7
Ig = 8
Is = 9
Ib = 10

def wToi(w):
    
    if(w==1):
        i=0
    elif(w==2):
        i=1
    elif(w==3):
        i=2
    elif(w==4):
        i=3
    elif(w==6):
        i=4
    elif(w==8):
        i=5
    return i

# this function is to extract the data from text file and convert into 2-d vector
def readFromText(path):
    
    # Initialize an empty list to store the 2D vector
    vector_2d = []

    # Open the input file
    with open(path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Skip empty lines
            if line.strip() == '':
                continue
            # Split the line by whitespace and convert each value to float
            values = [float(val) for val in line.split()]
            # Append the list of values to the 2D vector
            vector_2d.append(values)

    return vector_2d


def ISubN(voltage,width):

    if(voltage == 0):
        return 0

    v_round = round(voltage,2)
    v_round = abs(v_round)

    row = (v_round/0.01)-1 # because it takes to the corresponding row in 2-d vector based on the voltage
    row = int(round(row))

    val = 0
    if(width==1):
        val = W1nmos_off[row][Is]
    elif(width==2):
        val = W2nmos_off[row][Is]
    elif(width==3):
        val = W3nmos_off[row][Is]
    elif(width==4):
        val = W4nmos_off[row][Is]
    elif(width==6):
        val = W5nmos_off[row][Is]
    elif(width==8):
        val = W6nmos_off[row][Is]
    
    return val

def ISubP(voltage,width):

    if(voltage == 0):
        return 0

    v_round = round(voltage,2)
    v_round = abs(v_round)

    row = (v_round/0.01)-1# because it takes to the corresponding row in 2-d vector based on the voltage
    row = int(round(row))

    val = 0
    if(width==1):
        val = W1pmos_off[row][Is]
    elif(width==2):
        val = W2pmos_off[row][Is]
    elif(width==3):
        val = W3pmos_off[row][Is]
    elif(width==4):
        val = W4pmos_off[row][Is]
    elif(width==6):
        val = W5pmos_off[row][Is]
    elif(width==8):
        val = W6pmos_off[row][Is]
    
    return val

def IgateN_off(voltage,width):

    if(voltage == 0):
        return 0

    v_round = round(voltage,2)
    v_round = abs(v_round)

    row = (v_round/0.01)-1 # because it takes to the corresponding row in 2-d vector based on the voltage
    row = int(round(row))

    val = 0
    if(width==1):
        val = W1nmos_off[row][Ig]
    elif(width==2):
        val = W2nmos_off[row][Ig]
    elif(width==3):
        val = W3nmos_off[row][Ig]
    elif(width==4):
        val = W4nmos_off[row][Ig]
    elif(width==6):
        val = W5nmos_off[row][Ig]
    elif(width==8):
        val = W6nmos_off[row][Ig]
    
    return val

def IgateN_on(voltage,width):

    if(voltage == 0):
        return 0

    v_round = round(voltage,2)
    v_round = abs(v_round)

    row = (v_round/0.01)-1 # because it takes to the corresponding row in 2-d vector based on the voltage
    row = int(round(row))

    val = 0
    if(width==1):
        val = W1nmos_ON[row][Ig]
    elif(width==2):
        val = W2nmos_ON[row][Ig]
    elif(width==3):
        val = W3nmos_ON[row][Ig]
    elif(width==4):
        val = W4nmos_ON[row][Ig]
    elif(width==6):
        val = W5nmos_ON[row][Ig]
    elif(width==8):
        val = W6nmos_ON[row][Ig]
    
    return val


def IgateP_off(voltage,width):

    if(voltage == 0):
        return 0

    v_round = round(voltage,2)
    v_round = abs(v_round)

    row = (v_round/0.01)-1 # because it takes to the corresponding row in 2-d vector based on the voltage
    row = int(round(row))

    val = 0
    if(width==1):
        val = W1pmos_off[row][Ig]
    elif(width==2):
        val = W2pmos_off[row][Ig]
    elif(width==3):
        val = W3pmos_off[row][Ig]
    elif(width==4):
        val = W4pmos_off[row][Ig]
    elif(width==6):
        val = W5pmos_off[row][Ig]
    elif(width==8):
        val = W6pmos_off[row][Ig]
    
    return val

def IgateP_on(voltage,width):

    if(voltage == 0):
        return 0

    v_round = round(voltage,2)
    v_round = abs(v_round)

    row = (v_round/0.01)-1 # because it takes to the corresponding row in 2-d vector based on the voltage
    row = int(round(row))

    val = 0
    if(width==1):
        val = W1pmos_ON[row][Ig]
    elif(width==2):
        val = W2pmos_ON[row][Ig]
    elif(width==3):
        val = W3pmos_ON[row][Ig]
    elif(width==4):
        val = W4pmos_ON[row][Ig]
    elif(width==6):
        val = W5pmos_ON[row][Ig]
    elif(width==8):
        val = W6pmos_ON[row][Ig]
    
    return val

def IbodyN_off(voltage,width):

    if(voltage == 0):
        return 0

    v_round = round(voltage,2)
    v_round = abs(v_round)

    row = (v_round/0.01)-1 # because it takes to the corresponding row in 2-d vector based on the voltage
    row = int(round(row))

    val = 0
    if(width==1):
        val = W1nmos_off[row][Ib]
    elif(width==2):
        val = W2nmos_off[row][Ib]
    elif(width==3):
        val = W3nmos_off[row][Ib]
    elif(width==4):
        val = W4nmos_off[row][Ib]
    elif(width==6):
        val = W5nmos_off[row][Ib]
    elif(width==8):
        val = W6nmos_off[row][Ib]
    
    return val

def IbodyN_on(voltage,width):

    if(voltage == 0):
        return 0

    v_round = round(voltage,2)
    v_round = abs(v_round)

    row = (v_round/0.01)-1 # because it takes to the corresponding row in 2-d vector based on the voltage
    row = int(round(row))

    val = 0
    if(width==1):
        val = W1nmos_ON[row][Ib]
    elif(width==2):
        val = W2nmos_ON[row][Ib]
    elif(width==3):
        val = W3nmos_ON[row][Ib]
    elif(width==4):
        val = W4nmos_ON[row][Ib]
    elif(width==6):
        val = W5nmos_ON[row][Ib]
    elif(width==8):
        val = W6nmos_ON[row][Ib]
    
    return val


def IbodyP_off(voltage,width):

    if(voltage == 0):
        return 0

    v_round = round(voltage,2)
    v_round = abs(v_round)

    row = (v_round/0.01)-1 # because it takes to the corresponding row in 2-d vector based on the voltage
    row = int(round(row))

    val = 0
    if(width==1):
        val = W1pmos_off[row][Ib]
    elif(width==2):
        val = W2pmos_off[row][Ib]
    elif(width==3):
        val = W3pmos_off[row][Ib]
    elif(width==4):
        val = W4pmos_off[row][Ib]
    elif(width==6):
        val = W5pmos_off[row][Ib]
    elif(width==8):
        val = W6pmos_off[row][Ib]
    
    return val

def IbodyP_on(voltage,width):

    if(voltage == 0):
        return 0

    v_round = round(voltage,2)
    v_round = abs(v_round)

    row = (v_round/0.01)-1 # because it takes to the corresponding row in 2-d vector based on the voltage
    row = int(round(row))

    val = 0
    if(width==1):
        val = W1pmos_ON[row][Ib]
    elif(width==2):
        val = W2pmos_ON[row][Ib]
    elif(width==3):
        val = W3pmos_ON[row][Ib]
    elif(width==4):
        val = W4pmos_ON[row][Ib]
    elif(width==6):
        val = W5pmos_ON[row][Ib]
    elif(width==8):
        val = W6pmos_ON[row][Ib]
    
    return val

## get the 2-d vectors from all the stage-1 files

W1nmos_off = readFromText(r'W1nmos_off.txt')
W1nmos_ON  = readFromText(r'W1nmos_ON.txt')
W1pmos_off = readFromText(r'W1pmos_off.txt')
W1pmos_ON  = readFromText(r'W1pmos_ON.txt')

W2nmos_off = readFromText(r'W2nmos_off.txt')
W2nmos_ON  = readFromText(r'W2nmos_ON.txt')
W2pmos_off = readFromText(r'W2pmos_off.txt')
W2pmos_ON  = readFromText(r'W2pmos_ON.txt')

W3nmos_off = readFromText(r'W3nmos_off.txt')
W3nmos_ON  = readFromText(r'W3nmos_ON.txt')
W3pmos_off = readFromText(r'W3pmos_off.txt')
W3pmos_ON  = readFromText(r'W3pmos_ON.txt')

W4nmos_off = readFromText(r'W4nmos_off.txt')
W4nmos_ON  = readFromText(r'W4nmos_ON.txt')
W4pmos_off = readFromText(r'W4pmos_off.txt')
W4pmos_ON  = readFromText(r'W4pmos_ON.txt')

W5nmos_off = readFromText(r'W5nmos_off.txt')
W5nmos_ON  = readFromText(r'W5nmos_ON.txt')
W5pmos_off = readFromText(r'W5pmos_off.txt')
W5pmos_ON  = readFromText(r'W5pmos_ON.txt')

W6nmos_off = readFromText(r'W6nmos_off.txt')
W6nmos_ON  = readFromText(r'W6nmos_ON.txt')
W6pmos_off = readFromText(r'W6pmos_off.txt')
W6pmos_ON  = readFromText(r'W6pmos_ON.txt')

# vn00 = [0.133388,0.13336,0.133359,0.133359,0.133358,0.133358]
# vn01 = [2.07744E-05,2.19535E-05,2.33051E-05,2.39811E-05,2.46572E-05,2.49954E-05]
# vn10 = [0.666334,0.666317,0.666318,0.666319,0.666319,0.66632]
# vn11 = [2.86192E-08,3.91613E-08,4.15407E-08,4.27302E-08,4.39197E-08,4.45144E-08]

# vp00 = [0.8,0.8,0.8,0.8,0.8,0.8]
# vp01 = [0.799951,0.79995,0.799947,0.799946,0.799945,0.799944]
# vp10 = [0.146732,0.146738,0.146745,0.146748,0.146751,0.146753]
# vp11 = [0.653596,0.65359,0.653583,0.65368,0.653577,0.653576]

vn00 = [0.133388,0.13336,0.133359,0.133359,0.133358,0.133358]
vn01 = [2.07744E-05,2.19535E-05,2.33051E-05,2.39811E-05,2.46572E-05,2.49954E-05]
vn10 = [0.666334,0.666317,0.666318,0.666319,0.666319,0.66632]
vn11 = [2.86192E-08,3.91613E-08,4.15407E-08,4.27302E-08,4.39197E-08,4.45144E-08]

vp00 = [0.8,0.8,0.8,0.8,0.8,0.8]
vp01 = [0.799951,0.79995,0.799947,0.799946,0.799945,0.799944]
vp10 = [0.146732,0.146738,0.146745,0.146748,0.146751,0.146753]
vp11 = [0.653596,0.65359,0.653583,0.65358,0.653577,0.653576]


def nstack(A0,A1,width,vdd):
    leakage_sub =0
    leakage_body = 0
    leakage_gate = 0
    if((A0==0) and (A1==0)):
         leakage_sub = abs(ISubN(vn00[wToi(width)],width))
         leakage_body = 2*(abs(IbodyN_off(vn00[wToi(width)],width))+abs(IbodyN_off(vdd,width)) )
         leakage_gate = 2*(abs(IgateN_off(vn00[wToi(width)],width))+abs(IgateN_off(vdd,width)) )
    elif((A0==0) and (A1==1)):
         leakage_sub = abs(ISubN(vdd,width))
         leakage_body = abs(IbodyN_off(vdd,width))+abs(IbodyN_on(vdd,width))
         leakage_gate = abs(IgateN_off(vdd,width))+abs(IgateN_on(vdd,width))
    elif((A0==1) and (A1==0)):
         leakage_sub =abs(ISubN(vn10[wToi(width)],width))
         leakage_body = abs(IbodyN_off(vn10[wToi(width)],width))+abs(IbodyN_on(vdd-vn10[wToi(width)],width))
         leakage_gate = abs(IgateN_off(vn10[wToi(width)],width))+abs(IgateN_on(0.01,width))
    else:
         leakage_sub =0
         leakage_body = 2*abs(IbodyN_on(vdd,width))
         leakage_gate = 2*abs(IgateN_on(vdd,width))

    return leakage_sub,leakage_body,leakage_gate

def pstack(A0,A1,width,vdd):
    leakage_sub =0
    leakage_body = 0
    leakage_gate = 0
    if((A0==0) and (A1==0)):
         leakage_sub =0
         leakage_body = 2*abs(IbodyP_on(vdd,width))
         leakage_gate = 2*abs(IgateP_on(vdd,width))
    elif((A0==0) and (A1==1)):
         leakage_sub =abs(ISubP(0.01,width))
         leakage_body = 2*abs(ISubP(0.79,width))+abs(IbodyP_on(vdd-vp01[wToi(width)],width))
         leakage_gate = abs(IgateP_off(vp01[wToi(width)],width))+abs(IgateP_on(0.01,width))
    elif((A0==1) and (A1==0)):
         leakage_sub = abs(ISubP(vp10[wToi(width)],width))
         leakage_body = abs(IbodyP_off(vp10[wToi(width)],width))+abs(IbodyP_on(vdd-vp10[wToi(width)],width))
         leakage_gate = abs(IgateP_off(vp10[wToi(width)],width))+abs(IgateP_on(vdd-vp10[wToi(width)],width))
    else:
         leakage_sub = abs(ISubP(vp11[wToi(width)],width))
         leakage_body = 2*(abs(IbodyP_off(vp11[wToi(width)],width))+abs(IbodyP_off(vdd,width)) )
         leakage_gate = 2*(abs(IgateP_off(vp11[wToi(width)],width))+abs(IgateP_off(vdd,width)) )

    return leakage_sub,leakage_body,leakage_gate

def AND(A0,A1,width,vdd):
    leakage_sub =0
    leakage_body = 0
    leakage_gate = 0
    if((A0==0) and (A1==0)):
         leakage_sub = abs(ISubN(vn00[wToi(width)],width)) + abs(ISubP(vdd,width))  
         leakage_body = 2*(abs(IbodyN_off(vn00[wToi(width)],width))+abs(IbodyN_off(vdd,width)) ) + 2*abs(IbodyP_on(0.01,width))+ abs(IbodyN_on(vdd,width)) + abs(IbodyP_off(vdd,width))
         leakage_gate = 2*(abs(IgateN_off(vn00[wToi(width)],width))+abs(IgateN_off(vdd,width)) ) + 2*abs(IgateP_on(0.01,width))+ abs(IgateN_on(vdd,width)) + abs(IgateP_off(vdd,width))
    elif((A0==0) and (A1==1)):
         leakage_sub = abs(ISubN(vdd,width)) + abs(ISubP(vdd,width)) 
         leakage_body = abs(IbodyN_off(vdd,width))+abs(IbodyN_on(vdd,width))+abs(IbodyP_on(0.01,width))+ abs(IbodyN_on(vdd,width)) + 2*abs(IbodyP_off(vdd,width))
         leakage_gate = abs(IgateN_off(vdd,width))+abs(IgateN_on(vdd,width))+abs(IgateP_on(0.01,width))+ abs(IgateN_on(vdd,width)) + 2*abs(IgateP_off(vdd,width))
    elif((A0==1) and (A1==0)):
         leakage_sub =abs(ISubN(vn10[wToi(width)],width))+abs(ISubP(vdd,width)) 
         leakage_body = abs(IbodyN_off(vn10[wToi(width)],width))+abs(IbodyN_on(vdd-vn10[wToi(width)],width))+abs(IbodyP_on(0.01,width))+ abs(IbodyN_on(vdd,width)) + 2*abs(IbodyP_off(vdd,width))
         leakage_gate = abs(IgateN_off(vn10[wToi(width)],width))+abs(IgateN_on(0.01,width))+abs(IgateP_on(0.01,width))+ abs(IgateN_on(vdd,width)) + 2*abs(IgateP_off(vdd,width))
    else:
         leakage_sub =2*abs(ISubP(vdd,width))+abs(ISubN(vdd,width))
         leakage_body = 2*abs(IbodyN_on(vdd,width)) + 2*abs(IbodyP_off(vdd,width))+abs(IbodyP_on(0.01,width))+abs(IbodyN_off(vdd,width))
         leakage_gate = 2*abs(IgateN_on(vdd,width)) + 2*abs(IgateP_off(vdd,width))+abs(IgateP_on(0.01,width))+abs(IgateN_off(vdd,width))

    return leakage_sub,leakage_body,leakage_gate

# def OR(A0,A1,width,vdd):
#     leakage_sub =0
#     leakage_body = 0
#     leakage_gate = 0
#     if((A0==0) and (A1==0)):
#          leakage_sub = abs(ISubN(vn00[wToi(width)],width)) + abs(ISubP(vdd,width))  
#          leakage_body = 2*(abs(IbodyN_off(vn00[wToi(width)],width))+abs(IbodyN_off(vdd,width)) ) + 2*abs(IbodyP_on(0.01,width))+ abs(IbodyN_on(vdd,width)) + abs(IbodyP_off(vdd,width))
#          leakage_gate = 2*(abs(IgateN_off(vn00[wToi(width)],width))+abs(IgateN_off(vdd,width)) ) + 2*abs(IgateP_on(0.01,width))+ abs(IgateN_on(vdd,width)) + abs(IgateP_off(vdd,width))
#     elif((A0==0) and (A1==1)):
#          leakage_sub = abs(ISubN(vdd,width)) + abs(ISubP(vdd,width)) 
#          leakage_body = abs(IbodyN_off(vdd,width))+abs(IbodyN_on(vdd,width))+abs(IbodyP_on(0.01,width))+ abs(IbodyN_on(vdd,width)) + 2*abs(IbodyP_off(vdd,width))
#          leakage_gate = abs(IgateN_off(vdd,width))+abs(IgateN_on(vdd,width))+abs(IgateP_on(0.01,width))+ abs(IgateN_on(vdd,width)) + 2*abs(IgateP_off(vdd,width))
#     elif((A0==1) and (A1==0)):
#          leakage_sub =abs(ISubN(vn10[wToi(width)],width))+abs(ISubP(vdd,width)) 
#          leakage_body = abs(IbodyN_off(vn10[wToi(width)],width))+abs(IbodyN_on(vdd-vn10[wToi(width)],width))+abs(IbodyP_on(0.01,width))+ abs(IbodyN_on(vdd,width)) + 2*abs(IbodyP_off(vdd,width))
#          leakage_gate = abs(IgateN_off(vn10[wToi(width)],width))+abs(IgateN_on(0.01,width))+abs(IgateP_on(0.01,width))+ abs(IgateN_on(vdd,width)) + 2*abs(IgateP_off(vdd,width))
#     else:
#          leakage_sub =2*abs(ISubP(vdd,width))+abs(ISubN(vdd,width))
#          leakage_body = 2*abs(IbodyN_on(vdd,width)) + 2*abs(IbodyP_off(vdd,width))+abs(IbodyP_on(0.01,width))+abs(IbodyN_off(vdd,width))
#          leakage_gate = 2*abs(IgateN_on(vdd,width)) + 2*abs(IgateP_off(vdd,width))+abs(IgateP_on(0.01,width))+abs(IgateN_off(vdd,width))

#     return leakage_sub,leakage_body,leakage_gate

# def NOR(A0,A1,width,vdd):
#     leakage_sub =0
#     leakage_body = 0
#     leakage_gate = 0
#     if((A0==0) and (A1==0)):
#          leakage_sub = abs(ISubN(vn00[wToi(width)],width)) + abs(ISubP(vdd,width))  
#          leakage_body = 2*(abs(IbodyN_off(vn00[wToi(width)],width))+abs(IbodyN_off(vdd,width)) ) + 2*abs(IbodyP_on(0.01,width))+ abs(IbodyN_on(vdd,width)) + abs(IbodyP_off(vdd,width))
#          leakage_gate = 2*(abs(IgateN_off(vn00[wToi(width)],width))+abs(IgateN_off(vdd,width)) ) + 2*abs(IgateP_on(0.01,width))+ abs(IgateN_on(vdd,width)) + abs(IgateP_off(vdd,width))
#     elif((A0==0) and (A1==1)):
#          leakage_sub = abs(ISubN(vdd,width)) + abs(ISubP(vdd,width)) 
#          leakage_body = abs(IbodyN_off(vdd,width))+abs(IbodyN_on(vdd,width))+abs(IbodyP_on(0.01,width))+ abs(IbodyN_on(vdd,width)) + 2*abs(IbodyP_off(vdd,width))
#          leakage_gate = abs(IgateN_off(vdd,width))+abs(IgateN_on(vdd,width))+abs(IgateP_on(0.01,width))+ abs(IgateN_on(vdd,width)) + 2*abs(IgateP_off(vdd,width))
#     elif((A0==1) and (A1==0)):
#          leakage_sub =abs(ISubN(vn10[wToi(width)],width))+abs(ISubP(vdd,width)) 
#          leakage_body = abs(IbodyN_off(vn10[wToi(width)],width))+abs(IbodyN_on(vdd-vn10[wToi(width)],width))+abs(IbodyP_on(0.01,width))+ abs(IbodyN_on(vdd,width)) + 2*abs(IbodyP_off(vdd,width))
#          leakage_gate = abs(IgateN_off(vn10[wToi(width)],width))+abs(IgateN_on(0.01,width))+abs(IgateP_on(0.01,width))+ abs(IgateN_on(vdd,width)) + 2*abs(IgateP_off(vdd,width))
#     else:
#          leakage_sub =2*abs(ISubP(vdd,width))+abs(ISubN(vdd,width))
#          leakage_body = 2*abs(IbodyN_on(vdd,width)) + 2*abs(IbodyP_off(vdd,width))+abs(IbodyP_on(0.01,width))+abs(IbodyN_off(vdd,width))
#          leakage_gate = 2*abs(IgateN_on(vdd,width)) + 2*abs(IgateP_off(vdd,width))+abs(IgateP_on(0.01,width))+abs(IgateN_off(vdd,width))

#     return leakage_sub,leakage_body,leakage_gate
def NOT(A0,width,vdd):
    leakage_sub =0
    leakage_body = 0
    leakage_gate = 0
    if (A0==0):
         leakage_sub = abs(ISubN(vdd,width))
         leakage_body = abs(IbodyN_off(vdd,width))+abs(IbodyP_on(0.01,width))
         leakage_gate = abs(IgateN_off(vdd,width))+abs(IgateP_on(0.01,width))
    elif (A0==1):
         leakage_sub = abs(ISubP(vdd,width))
         leakage_body = abs(IbodyN_on(0.01,width))+abs(IbodyP_off(vdd,width))
         leakage_gate = abs(IgateP_off(vdd,width))+abs(IgateN_on(0.01,width))

    return leakage_sub,leakage_body,leakage_gate



def AND_use(A0,A1) :
    leakage_sub =0
    leakage_body = 0
    leakage_gate = 0
    if (A0==0) and (A1==0):
        leakage_sub = 4.285e-09
        leakage_body = 2.3314e-13
        leakage_gate = 9.6402e-12
    elif (A0==0) and (A1==1):
        leakage_sub = 8.2374e-09
        leakage_body = 4.128e-13
        leakage_gate = 2.35e-11
    elif (A0==1) and (A1==0):
        leakage_sub = 5.698e-09
        leakage_body = 4.28e-10
        leakage_gate = 6.321e-11
    else:
        leakage_sub = 1.4823e-08
        leakage_body = 3.489e-10
        leakage_gate = 3.734e-11
    return leakage_sub,leakage_body,leakage_gate

def OR_use(A0,A1) :
    leakage_sub =0
    leakage_body = 0
    leakage_gate = 0
    if (A0==0) and (A1==0):
        leakage_sub = 7.878e-09
        leakage_body = 3.576e-12
        leakage_gate = 9.959e-12
    elif (A0==0) and (A1==1):
        leakage_sub = 2.2206e-08
        leakage_body = 4.126e-10
        leakage_gate = 2.821e-11
    elif (A0==1) and (A1==0):
        leakage_sub = 7.256e-09
        leakage_body = 4.6301e-13
        leakage_gate = 5.026e-12
    else:
        leakage_sub = 1.941e-09
        leakage_body = 5.708e-13
        leakage_gate = 1.00525e-11
    return leakage_sub,leakage_body,leakage_gate

def NOR_use(A0,A1) :
    leakage_sub =0
    leakage_body = 0
    leakage_gate = 0
    if (A0==0) and (A1==0):
        leakage_sub = 3.645e-09
        leakage_body = 3.468e-12
        leakage_gate = 9.959e-12
    elif (A0==0) and (A1==1):
        leakage_sub = 2.0107e-08
        leakage_body = 8.954e-10
        leakage_gate = 7.6202e-11
    elif (A0==1) and (A1==0):
        leakage_sub = 5.4274e-09
        leakage_body = 1.0807e-13
        leakage_gate = 5.026e-12
    else:
        leakage_sub = 1.1533e-10
        leakage_body = 2.1552e-13
        leakage_gate = 1.005e-11
    return leakage_sub,leakage_body,leakage_gate

def NOT_use(A0) :
    leakage_sub =0
    leakage_body = 0
    leakage_gate = 0
    if (A0==0) :
        leakage_sub = 1.822e-09
        leakage_body = 3.552e-13
        leakage_gate = 3.604e-12
    else:
        leakage_sub = 4.2317e-09
        leakage_body = 1.078e-13
        leakage_gate = 5.026e-12
    return leakage_sub,leakage_body,leakage_gate



leakage_sub,leakage_body,leakage_gate = nstack(0,0,2,0.8)
print(leakage_sub)
print(leakage_body)
print(leakage_gate)

leakage_sub,leakage_body,leakage_gate = NOT(0,1,0.8)
print(leakage_sub)
print(leakage_body)
print(leakage_gate)

def Final_circuit(G0,G1,G2,G3,P0,P1,P2,P3,Cn) :
    leakage_sub =0
    leakage_body = 0
    leakage_gate = 0

    W1 = P0&G0
    W2 = ~Cn
    W3 = G0&W2
    Cnx = (~W1)&(~W3)

    W4 = P1&G1
    W5 = G1&W1
    W6 = W3&G1
    W7 = W4|W5
    Cny = (~W7)&(~W6)

    W8 = P2&G2
    W9 = W4&G2
    W10 = G1&G2
    W11 = W1&W10
    W12 = W3&W10
    W13 = W8|W9
    W14 = W11|W12
    Cnz = (~W13)&(W14)

    W15 = P3&G3
    W16 = W8&G3
    W17 = P1&G3
    W18 = W17&W10
    W19 = G0&G3
    W20 = W10&W19
    W21 = W15|W16
    W22 = W18|W20
    G = W21|W22

    W23 = P0|P1
    W24 = P2|P3
    P = W23|W24

    leakage_sub += AND_use(P0,G0)[0]
    leakage_sub += NOT_use(Cn)[0]
    leakage_sub += AND_use(G0,W2)[0]
    leakage_sub += NOR_use(W1,W3)[0]

    leakage_sub += AND_use(P1,G1)[0]
    leakage_sub += AND_use(G1,W1)[0]
    leakage_sub += AND_use(W3,G1)[0]
    leakage_sub += OR_use(W4,W5)[0]
    leakage_sub += NOR_use(W7,W6)[0]

    leakage_sub += AND_use(P2,G2)[0]
    leakage_sub += AND_use(W4,G2)[0]
    leakage_sub += AND_use(G1,G2)[0]
    leakage_sub += AND_use(W1,W10)[0]
    leakage_sub += AND_use(W3,W10)[0]
    leakage_sub += OR_use(W8,W9)[0]
    leakage_sub += OR_use(W11,W12)[0]
    leakage_sub += NOR_use(W13,W14)[0]

    leakage_sub += AND_use(P3,G3)[0]
    leakage_sub += AND_use(W8,G3)[0]
    leakage_sub += AND_use(P1,G3)[0]
    leakage_sub += AND_use(W17,W10)[0]
    leakage_sub += AND_use(G0,G3)[0]
    leakage_sub += AND_use(W10,W19)[0]
    leakage_sub += OR_use(W15,W16)[0]
    leakage_sub += OR_use(W18,W20)[0]
    leakage_sub += OR_use(W21,W22)[0]
    
    leakage_sub += OR_use(P0,P1)[0]
    leakage_sub += OR_use(P2,P3)[0]
    leakage_sub += OR_use(W23,W24)[0]

    leakage_body += AND_use(P0,G0)[1]
    leakage_body += NOT_use(Cn)[1]
    leakage_body += AND_use(G0,W2)[1]
    leakage_body += NOR_use(W1,W3)[1]

    leakage_body += AND_use(P1,G1)[1]
    leakage_body += AND_use(G1,W1)[1]
    leakage_body += AND_use(W3,G1)[1]
    leakage_body += OR_use(W4,W5)[1]
    leakage_body += NOR_use(W7,W6)[1]

    leakage_body += AND_use(P2,G2)[1]
    leakage_body += AND_use(W4,G2)[1]
    leakage_body += AND_use(G1,G2)[1]
    leakage_body += AND_use(W1,W10)[1]
    leakage_body += AND_use(W3,W10)[1]
    leakage_body += OR_use(W8,W9)[1]
    leakage_body += OR_use(W11,W12)[1]
    leakage_body += NOR_use(W13,W14)[1]

    leakage_body += AND_use(P3,G3)[1]
    leakage_body += AND_use(W8,G3)[1]
    leakage_body += AND_use(P1,G3)[1]
    leakage_body += AND_use(W17,W10)[1]
    leakage_body += AND_use(G0,G3)[1]
    leakage_body += AND_use(W10,W19)[1]
    leakage_body += OR_use(W15,W16)[1]
    leakage_body += OR_use(W18,W20)[1]
    leakage_body += OR_use(W21,W22)[1]
    
    leakage_body += OR_use(P0,P1)[1]
    leakage_body += OR_use(P2,P3)[1]
    leakage_body += OR_use(W23,W24)[1]


    return P,G,Cnx,Cny,Cnz,leakage_sub,leakage_body,leakage_gate

leakage_sub = Final_circuit(0,0,0,0,0,0,0,0,0)[5]
leakage_body = Final_circuit(0,0,0,0,0,0,0,0,0)[6]
print(leakage_sub,leakage_body)