with open('Input_07_1.txt') as f:
    hands = [v.split() for v in f.read().splitlines()]

#print(hands)

for i in range(0, len(hands)):
    cards = hands[i][0]

    # calc hands point from 1 to 7
    dist_cards = set(cards)
    if len(dist_cards) == 1:
        hands[i].append(7)
    elif len(dist_cards) == 2:
        if cards.count(dist_cards.pop()) in (4,1):
            hands[i].append(6)
        else:
            hands[i].append(5)
    elif len(dist_cards)==3:
        if cards.count(dist_cards.pop()) == 3 or cards.count(dist_cards.pop()) == 3 or cards.count(dist_cards.pop()) == 3:
            hands[i].append(4)
        else:
            hands[i].append(3)
    elif len(dist_cards)==4:
        hands[i].append(2)
    else:
        hands[i].append(1)
    
    for c in cards:
        if c.isdigit():
            hands[i].append(int(c))
        else:
            match c:
                case "A": hands[i].append(14)
                case "K": hands[i].append(13)
                case "Q": hands[i].append(12)
                case "J": hands[i].append(11)
                case "T": hands[i].append(10)

#print(hands)

hands.sort(key=lambda x: (x[2],x[3],x[4],x[5],x[6],x[7]))

#print(hands)

tot = 0
for i in range(0, len(hands)):
    tot += (i+1)*int(hands[i][1])

print(tot)

        

    



