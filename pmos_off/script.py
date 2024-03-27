import pandas as pd
from tabulate import tabulate

file_name = 'W6pmos_off_simulation_results.txt'

with open(file_name, 'r') as file:
    # Read data line by line and split each line
    data = [line.split() for line in file]

# Display the data in tabulated form
headers = ["Temp", "M1[W]", "V-sweep", "V(drain)", "V(source)", "V(gate)", "V(body)", "I(Vd)", "I(Vg)", "I(Vs)", "I(Vb)"]
table = tabulate(data,headers, tablefmt="fancy_grid")
print(table)

output_file = 'W6.txt'
with open(output_file, 'w') as output:
    print(table, file=output)