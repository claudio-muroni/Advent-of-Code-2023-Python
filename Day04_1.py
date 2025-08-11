tot = 0

with open('Input_04_1.txt','r') as file:
    for card in file:
        winning_numbers = card[card.find(':')+1:card.find('|')].split()
        your_numbers = card[card.find('|')+1:].split()

        c = 0

        for num in your_numbers:
            if num in winning_numbers:
                c += 1
        
        if c > 0: tot += 2**(c-1)

print(tot)