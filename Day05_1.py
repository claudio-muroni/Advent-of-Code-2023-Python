# it is not sustainable to save each mapping combination in a dict

n_line = 1
seed_map = {}

with open('Input_05_1.txt','r') as file:
    for line in file:
        if n_line == 1:
            seeds =  list(map(int, line[line.find(':')+1:].split()))
            print(seeds)
            
        
        if line[0].isdigit():
            parameters = list(map(int, line.split()))
            for i in range(0,parameters[2]):
                seed_map[parameters[1]+i]=parameters[0]+i

        if not line[0].isdigit() and len(seed_map) > 0:  
            
            for pos in range(0,len(seeds)):
                if seeds[pos] in seed_map:
                    seeds[pos] = seed_map[seeds[pos]]

            #print(seed_map)
            seed_map = {}
            print(seeds)
        
        n_line += 1


for pos in range(0,len(seeds)):
    if seeds[pos] in seed_map:
        seeds[pos] = seed_map[seeds[pos]]

#print(seed_map)
seed_map = {}
print(seeds)

print(min(seeds))