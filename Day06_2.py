# there is a more efficient way to solve it for sure:
# the problem is a simple "parabola", we know its behaviour so it is not necessary to calculate each scenario
# (in this case brute force solves it in few seconds)

with open('Input_06_1.txt') as f:
    values = f.read().splitlines()

race_times = values[0][values[0].find(':')+1:].split()
race_records = values[1][values[1].find(':')+1:].split()

race_time = ''
race_record = ''
for i in range(0, len(race_times)):
    race_time += race_times[i]
    race_record += race_records[i]

race_time = int(race_time)
race_record = int(race_record)

race_win = 0
for press_time in range(1, race_time):
    x = (race_time - press_time) * press_time
    if x > race_record:
        race_win += 1

print(race_win)