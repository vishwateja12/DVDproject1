import ast
import pandas as pd
import numpy as np
from tabulate import tabulate

def generate_output(input_filename, output_filename):
    
    
    # Read the input file
    with open(input_filename, 'r') as file:
        data = file.readlines()

    # Create a list to store the processed data
    processed_data = []

    # Extract the relevant data from each line in the input file
    
    size = len(data)
    for i in range(1,size):
        
        line = data[i]
        s = line.split()
        temp = str([s[0]]*9)
        temp = [int(x) for x in ast.literal_eval(temp)]
        
        width = str([s[1]]*9)
        width = [int(x) for x in ast.literal_eval(width)]
        
        v_gate = str(s[2:11])
        v_gate = v_gate.replace('"','')
        v_gate = [float(x) for x in ast.literal_eval(v_gate)]
        
        
        i_vd = str(s[11:20])
        i_vd = i_vd.replace('"','')
        i_vd = [float(x) for x in ast.literal_eval(i_vd)]
        
        
        i_vg = str(s[20:29])
        i_vg = i_vg.replace('"','')
        i_vg = [float(x) for x in ast.literal_eval(i_vg)]
        
        i_vs = str(s[29:38])
        i_vs = i_vs.replace('"','')
        i_vs = [float(x) for x in ast.literal_eval(i_vs)]
        
        i_vb = str(s[38:])
        i_vb = i_vb.replace('"','')
        i_vb = [float(x) for x in ast.literal_eval(i_vb)]
        
        # i_vb_list = list(i_vb)
        # i_vd_list = list(i_vd)
        # i_vs_list = list(i_vs)
        # i_vg_list = list(i_vg)
        
        
        
        # temp, m1, v_gate, i_vd, i_vg, i_vs, i_vb = line.split()

        # Convert the string representations of currents to a list of floats
        # i_vd_list = list(map(float, i_vd.strip('"').split()))
        # i_vg_list = list(map(float, i_vg.strip('"').split()))
        # i_vs_list = list(map(float, i_vs.strip('"').split()))
        # i_vb_list = list(map(float, i_vb.strip('"').split()))

        # Append the processed data to the list
        processed_data.append((temp, width, v_gate, i_vd, i_vg, i_vs, i_vb))
    
    for i in range(8) :
        outl = processed_data[i]
        outl = np.transpose(outl)
        table = tabulate(outl, headers=["temp", "width", "v_gate", "i_vd", "i_vg","i_vs","i_vb"], tablefmt="pretty")
        print(table)
    

    

    # Create the output file
    with open(output_filename, 'w') as f:
        # Write the header row
        i = 0
        # Iterate over each sublist and write the rows to the file
        for item in processed_data:
            # Unpack the sublist into the required variables
            temp, width, gate, vd, vg, vs, vb = item
            
            if(i < 4):
                f.write('Temp\tWidth\t\tV(gate)\t\tI(Vd)\t\t\t\tI(Vg)\t\t\t\tI(Vs)\t\t\t\t\tI(Vb)\n')
            
            else:
                f.write('Temp\tWidth\t\t\tV(gate)\t\tI(Vd)\t\t\t\tI(Vg)\t\t\t\tI(Vs)\t\t\t\t\tI(Vb)\n')
            # Iterate over the items in the lists simultaneously using zip
            for t, w, g, d, g2, s, b in zip(temp, width, gate, vd, vg, vs, vb):
                # Format the data as a tab-separated string
                row = f" {t}\t\t {w}\t\t\t {g} \t\t{d}\t\t{g2}\t\t{s}\t\t\t\t{b}\n"
                # Write the row to the file
                f.write(row)
                
                # to generate the output file
            f.write('\n')
            i = i+1
input_filename = 'nmos_simulation_results.txt'
output_filename = 'nmos_output.txt'
generate_output(input_filename, output_filename)

input_filename = 'pmos_simulation_results.txt'
output_filename = 'pmos_output.txt'
generate_output(input_filename, output_filename)


