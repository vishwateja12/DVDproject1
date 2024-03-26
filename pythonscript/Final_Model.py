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

def nstack(A0,A1,width,vdd):
    leakage_sub =0
    leakage_body = 0
    leakage_gate = 0
    if((A0==0) and (A1==0)):
         leakage_sub = abs(ISubN(vn00[5],width))
         leakage_body = 2*(abs(IbodyN_off(vn00[5],width))+abs(IbodyN_off(vdd,width)) )
         leakage_gate = 2*(abs(IgateN_off(vn00[5],width))+abs(IgateN_off(vdd,width)) )
    elif((A0==0) and (A1==1)):
         leakage =0
    elif((A0==1) and (A1==0)):
         leakage =0
    else:
         leakage =0

    return leakage_sub,leakage_body,leakage_gate

def pstack(A0,A1,width,vdd):
    leakage =0
    if((A0==0) and (A1==0)):
         leakage = 0
    elif((A0==0) and (A1==1)):
         leakage =0
    elif((A0==1) and (A1==0)):
         leakage =0
    else:
         leakage =0

    return leakage

def AND(A0,A1,width,vdd):
    leakage =0
    if((A0==0) and (A1==0)):
         leakage = 0
    elif((A0==0) and (A1==1)):
         leakage =0
    elif((A0==1) and (A1==0)):
         leakage =0
    else:
         leakage =0

    return leakage

def OR(A0,A1,width,vdd):
    leakage =0
    if((A0==0) and (A1==0)):
         leakage = 0
    elif((A0==0) and (A1==1)):
         leakage =0
    elif((A0==1) and (A1==0)):
         leakage =0
    else:
         leakage =0

    return leakage

def NOR(A0,A1,width,vdd):
    leakage =0
    if((A0==0) and (A1==0)):
         leakage = 0
    elif((A0==0) and (A1==1)):
         leakage =0
    elif((A0==1) and (A1==0)):
         leakage =0
    else:
         leakage =0

    return leakage

def NOT(A0,width,vdd):
    leakage =0
    if (A0==0):
         leakage = 0
    elif (A0==1):
         leakage =0

    return leakage

leakage_sub,leakage_body,leakage_gate = nstack(0,0,8,0.8,)
print(leakage_sub)
print(leakage_body)
print(leakage_gate)


leakage_sub = abs(ISubN(vn00[5],8))
leakage_body = 2*(abs(IbodyN_off(vn00[5],8))+abs(IbodyN_off(0.8,8)) )
leakage_gate = 2*(abs(IgateN_off(vn00[5],8))+abs(IgateN_off(0.8,8)) )



