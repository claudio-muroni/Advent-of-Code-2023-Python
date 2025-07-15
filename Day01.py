tot = 0
tot2 = 0
num_list = [("one","1"), ("two","2"), ("three","3"), ("four","4"), ("five","5"), ("six","6"), ("seven","7"), ("eight","8"), ("nine","9")]

with open('Input_01_1.txt', 'r') as file:

    for line in file:

        first_digit = ""
        last_digit = ""
        first_index = -1
        last_index = -1

        for i in range(len(line)):
            if line[i].isdigit():
                if first_digit == "":
                    first_digit = line[i]
                    first_index = i
                else:
                    last_digit = line[i]
                    last_index = i
        
        if last_digit == "":
            last_digit = first_digit
            last_index = first_index

        num = first_digit + last_digit
        tot = tot + int(num)

        for (x,y) in num_list:
            i_str = line.find(x)
            if i_str > -1 and i_str < first_index:
                first_digit = y
                first_index = i_str
        
        for (x,y) in num_list:
            i_str = line.rfind(x)
            if i_str > -1 and i_str > last_index:
                last_digit = y
                last_index = i_str

        num2 = first_digit + last_digit
        tot2 = tot2 + int(num2)

print(tot)
print(tot2) 