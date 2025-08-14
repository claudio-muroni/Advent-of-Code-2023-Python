first_line = True

with open('Input_05_1.txt','r') as file:
    for line in file:
        if first_line:
            seeds =  list(map(int, line[line.find(':')+1:].split()))
            new_seeds = []
            rem_seeds = []
            first_line = False
            #print(seeds)
            
        
        if line[0].isdigit():
            parameters = list(map(int, line.split()))

            for seed in seeds:
                if seed >= parameters[1] and seed < parameters[1]+parameters[2]:
                    rem_seeds.append(seed)
                    new_seeds.append(parameters[0]+(seed-parameters[1]))


        if not line[0].isdigit() and len(new_seeds) > 0:  
            
            for rem in rem_seeds:
                seeds.remove(rem)

            seeds.extend(new_seeds)
            rem_seeds = []
            new_seeds = []

            #print(seeds)

for rem in rem_seeds:
    seeds.remove(rem)

seeds.extend(new_seeds)
rem_seeds = []
new_seeds = []

#print(seeds)

print(min(seeds))