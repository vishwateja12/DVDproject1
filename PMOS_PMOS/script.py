import pandas as pd
from tabulate import tabulate

file_name = 'W1pmos_off_simulation_results.txt'

with open(file_name, 'r') as file:
    # Read data line by line and split each line
    data = [line.split() for line in file]

# Display the data in tabulated form
headers = ["Temp", "M1[W]", "V-sweep", "V(D1)", "V(S1)", "V(G1)", "V(G2)","V(S2)","V(B1)","V(B2)","I(Vd)", "I(Vg1)", "I(Vg2)", "I(Vs)", "I(Vb1)", "I(Vb2)"]
table = tabulate(data,headers, tablefmt="fancy_grid")
print(table)

output_file = 'W1_off.txt'
with open(output_file, 'w') as output:
    print(table, file=output)