# read in file
# save data in a list of tuple pairs
data = []
with open("./Python/2/input.txt") as f:
    for line in f.readlines():
        op, pl = line.split()
        data.append((op, pl))

total_points = 0

# win/loss/draw points
result = [6, 0, 3]

# moves
moves_dict = {
    'X': 0,
    'Y': 1,
    'Z': 2,
    'C': 0,
    'B': 1,
    'A': 2
}

# points for player choice
points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

# loop through each pair
for op, pl in data:
    # calculate win/draw/loss
    # A = X = Rock
    # B = Y = Paper
    # C = Z = Scissors

    # get corresponding move value from dict
    op_move_val = moves_dict[op]
    pl_move_val = moves_dict[pl]

    # add corrsponding result to total
    total_points += result[(op_move_val + pl_move_val) % 3]

    # calculate points
    total_points += points[pl]

print(f"Total points: {total_points}")

# part two:
# X = loss
# Y = draw
# Z = win

# define dicts for each result
win_dict = {
    'A': 2, # rock -> paper
    'B': 3, # paper -> scissors
    'C': 1, # scissors -> rock
}

draw_dict = {
    'A': 1, # rock -> rock
    'B': 2, # paper -> paper
    'C': 3, # scissors -> scissors
}

loss_dict = {
    'A': 3, # rock -> scissors
    'B': 1, # paper -> rock
    'C': 2, # scissors -> paper
}

total_points_2 = 0

for op, res in data:
    if res == 'X': # loss
        total_points_2 += loss_dict[op]
    elif res == 'Y': # draw
        total_points_2 += draw_dict[op]
    elif res == 'Z': # win
        total_points_2 += win_dict[op]
    total_points_2 += 6 if res == 'Z' else 3 if res == 'Y' else 0

print(f"Total points (part 2): {total_points_2}")