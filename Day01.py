tot = 0

with open('Input_01_1.txt', 'r') as file:

    for line in file:

        # WRONG: there are case in which letters are shared but you have to take the first usage
        line = line.replace("one","1")
        line = line.replace("two","2")
        line = line.replace("three","3")
        line = line.replace("four","4")
        line = line.replace("five","5")
        line = line.replace("six","6")
        line = line.replace("seven","7")
        line = line.replace("eight","8")
        line = line.replace("nine","9")

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
        print(num)
        tot = tot + int(num)

print(tot)   