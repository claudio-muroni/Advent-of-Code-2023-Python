tot = 0
card_count = 0
cards = {}

with open('Input_04_1.txt','r') as file:
    for card in file:
        
        card_count += 1

        card_number = int(card[5:card.find(':')])
        winning_numbers = card[card.find(':')+1:card.find('|')].split()
        your_numbers = card[card.find('|')+1:].split()

        if card_number not in cards:
            cards[card_number] = 1
        else:
            cards[card_number] += 1

        qty = cards[card_number]

        c = 0

        for num in your_numbers:
            if num in winning_numbers:
                c += 1
        
        for i in range(1,c+1):
            if card_number+i not in cards:
                cards[card_number+i] = 1*qty
            else:
                cards[card_number+i] += 1*qty


for key in cards:
    if key > card_count: break
    tot += cards[key]

print(tot)