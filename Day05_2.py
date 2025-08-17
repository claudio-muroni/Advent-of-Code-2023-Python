#wip

first_line = True

with open('Test_Input_05_1.txt','r') as file:
    for line in file:
        if first_line:
            old_seeds = list(map(int, line[line.find(':')+1:].split()))
            seeds = []
            for i in range(0, len(old_seeds)-1, 2):
                seeds.append((old_seeds[i],old_seeds[i]+old_seeds[i+1]-1))
            new_seeds = []
            rem_seeds = []
            first_line = False
            #print(seeds)

        #print("seeds: ", seeds)
        #print("rem_seeds: ", rem_seeds)
        #print("new_seeds: ", new_seeds)
        
        if line[0].isdigit():
            parameters = list(map(int, line.split()))

            for seed in seeds:

                #if seed[0] > parameters[1]+parameters[2]-1 or seed[1] < parameters[1]:
                    # no intersection
                
                if seed[0] >= parameters[1] and seed[1] <= parameters[1]+parameters[2]-1:
                    # subset
                    new_seed = ((parameters[0]+seed[0]-parameters[1]),(parameters[0]+seed[1]-parameters[1]))
                    
                    new_seeds.append(new_seed)
                    if seed not in rem_seeds: rem_seeds.append(seed)
                
                elif (parameters[1] <= seed[0] <= parameters[1]+parameters[2]-1):
                    # partial intersection 1
                    old_seed_part = (parameters[1]+parameters[2], seed[1])
                    new_seed_part = (seed[0], parameters[1]+parameters[2]-1)
                    new_seed = ((parameters[0]+new_seed_part[0]-parameters[1]),(parameters[0]+new_seed_part[1]-parameters[1]))

                    new_seeds.append(old_seed_part)
                    new_seeds.append(new_seed)
                    if seed not in rem_seeds: rem_seeds.append(seed)

                    

                elif (parameters[1] <= seed[1] <= parameters[1]+parameters[2]-1):
                    # partial intersection 2
                    old_seed_part = (seed[0], parameters[1]-1)
                    new_seed_part = (parameters[1], seed[1])
                    new_seed = ((parameters[0]+new_seed_part[0]-parameters[1]),(parameters[0]+new_seed_part[1]-parameters[1]))

                    new_seeds.append(old_seed_part)
                    new_seeds.append(new_seed)
                    if seed not in rem_seeds: rem_seeds.append(seed)

                    

                elif seed[0] < parameters[1] and seed[1] > parameters[1]+parameters[2]-1:
                    # superset
                    new_seed_part = (parameters[1], parameters[1]+parameters[2]-1)
                    new_seed = ((parameters[0]+new_seed_part[0]-parameters[1]),(parameters[0]+new_seed_part[1]-parameters[1]))
                    old_seed_part_low = (seed[0], parameters[1]-1)
                    old_seed_part_top = (parameters[1]+parameters[2], seed[1])

                    new_seeds.append(old_seed_part_low)
                    new_seeds.append(old_seed_part_top)
                    new_seeds.append(new_seed)
                    if seed not in rem_seeds: rem_seeds.append(seed)

                
            


        if not line[0].isdigit() and len(new_seeds) > 0:    
            
            for rem in rem_seeds:
                seeds.remove(rem)
            
            seeds.extend(new_seeds)
            rem_seeds = []
            new_seeds = []

for rem in rem_seeds:
    seeds.remove(rem)

seeds.extend(new_seeds)
rem_seeds = []
new_seeds = []

#print(len(seeds))
#print(seeds)

#print(seeds[0])

minimum = seeds[0][0]
#print(minimum)
for seed in seeds[1:]:
    if seed[0] < minimum:
        minimum = seed[0]
        print(minimum)

print(minimum)