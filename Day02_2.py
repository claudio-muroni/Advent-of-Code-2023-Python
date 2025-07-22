tot=0

with open('Input_02_1.txt','r') as file:
    for game in file:

        min_red = 0
        min_green = 0
        min_blue = 0

        game_id=game[5:game.find(':')]
        
        sets = game[game.find(':')+1:].split(';')
        
        for single_set in sets:
            cubes = single_set.split(',')
            for cube in cubes:
                cube_num = cube.split()[0]
                cube_color = cube.split()[1]

                match cube_color:
                    case "red": 
                        if int(cube_num) > min_red: min_red = int(cube_num)
                    case "green": 
                        if int(cube_num) > min_green: min_green = int(cube_num)
                    case "blue": 
                        if int(cube_num) > min_blue: min_blue = int(cube_num)
                        
        tot = tot + (min_red*min_green*min_blue)
                

print(tot)