tot=0

max_red = 12
max_green = 13
max_blue = 14

with open('Input_02_1.txt','r') as file:
    for game in file:
        possible = True

        game_id=game[5:game.find(':')]
        
        sets = game[game.find(':')+1:].split(';')
        
        for single_set in sets:
            cubes = single_set.split(',')
            for cube in cubes:
                cube_num = cube.split()[0]
                cube_color = cube.split()[1]

                match cube_color:
                    case "red": 
                        if int(cube_num) > max_red: possible = False
                    case "green": 
                        if int(cube_num) > max_green: possible = False
                    case "blue": 
                        if int(cube_num) > max_blue: possible = False
                
        if possible: tot = tot + int(game_id)

print(tot)