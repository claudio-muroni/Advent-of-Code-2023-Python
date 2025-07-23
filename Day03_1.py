
symbols_list = []

with open('Test_Input_03_1.txt','r') as file:
    y = 0
    for line in file:
        y = y + 1
        x = 0
        for c in line:
            x = x + 1
            
            if (c not in ('.','\n') and not c.isdigit()): print(f"{y},{x}")