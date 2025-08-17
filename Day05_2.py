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
        
        if line[0].isdigit():
            parameters = list(map(int, line.split()))

            for seed in seeds:

                if seed[0] > parameters[1]+parameters[2]-1 or seed[1] < parameters[1]:
                    # no intersection
                    print("no intersection")
                    
                
                if seed[0] >= parameters[1] and seed[1] <= parameters[1]+parameters[2]-1:
                    # subset
                    print("subset")
                    new_seed = ((parameters[0]+seed[0]-parameters[1]),(parameters[0]+seed[1]-parameters[1]))
                    print(parameters)
                    print(seed, new_seed)
                    break
                
                #if (parameters[1] <= seed[0] <= parameters[1]+parameters[2]-1):
                    # partial intersection

                #if (parameters[1] <= seed[1] <= parameters[1]+parameters[2]-1):
                    # partial intersection
          