with open('Input_06_1.txt') as f:
    values = f.read().splitlines()

race_times = values[0][values[0].find(':')+1:].split()
race_records = values[1][values[1].find(':')+1:].split()

tot = 1

for i in range(0, len(race_times)):
    race_time = int(race_times[i])
    race_record = int(race_records[i])
    race_win = 0

    for press_time in range(1, race_time):
        x = (race_time - press_time) * press_time
        if x > race_record:
            race_win += 1

    tot *= race_win

print(tot)