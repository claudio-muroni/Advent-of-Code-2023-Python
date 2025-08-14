# removed usage of dictionaries
# still inefficent, need to avoid useless attempts

n_line = 1

with open('Input_05_1.txt','r') as file:
    for line in file:
        if n_line == 1:
            seeds =  list(map(int, line[line.find(':')+1:].split()))
            new_seeds = []
            print(seeds)
            
        
        if line[0].isdigit():
            parameters = list(map(int, line.split()))
            for i in range(0,parameters[2]):

                if len(seeds) == 0: break

                if parameters[1]+i in seeds:
                    seeds.remove(parameters[1]+i)
                    new_seeds.append(parameters[0]+i)


        if not line[0].isdigit() and len(new_seeds) > 0:  
            
            seeds.extend(new_seeds)
            new_seeds = []

            #print(seeds)
        
        n_line += 1

seeds.extend(new_seeds)
new_seeds = []

#print(seeds)

print(min(seeds))