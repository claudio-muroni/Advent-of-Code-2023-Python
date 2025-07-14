with open('Input_01_1.txt', 'r') as file:

    tot = 0

    for line in file:

        first_digit = ""
        last_digit = ""

        for c in line:
            if c.isdigit():
                if first_digit == "":
                    first_digit = c
                else:
                    last_digit = c
        
        if last_digit == "":
            last_digit = first_digit

        num = first_digit + last_digit
        tot = tot + int(num)

print(tot)   