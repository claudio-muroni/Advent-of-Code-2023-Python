def check_part_number(num, schematic):

    return False



with open('Input_03_1.txt') as f:
    schematic = f.read().splitlines()

y_max = len(schematic)-1
x_max = len(schematic[0])-1

tot = 0

y = 0
while y <= y_max:
    x = 0
    while x <= x_max:
        c = schematic[y][x]
        
        if c.isdigit():
            part_number = False
            num = c

            while (x < x_max and schematic[y][x+1].isdigit()):
                x = x + 1
                c = schematic[y][x]
                num = num + c

            for y2 in range(-1,2):
                if (y + y2 >= 0 and y + y2 <= y_max):
                    for x2 in range(-len(num),2):
                        if (x + x2 >= 0 and x + x2 <= x_max):
                            symbol = schematic[y+y2][x+x2]
                            if (symbol != '.' and not symbol.isdigit()): part_number = True
            
            #print(part_number, num)
            if part_number: tot = tot + int(num)

        x = x + 1

    y = y + 1

print(tot)
