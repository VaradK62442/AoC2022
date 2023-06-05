def find_prio_val(common_letter):
    # 'A' = 65
    # 'a' = 97
    if common_letter.isupper():
        val = ord(common_letter) - 64 + 26
    else:
        val = ord(common_letter) - 96

    return val
        

# read in data
# save in list
data = []
with open("./Python/3/input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())

priority_sum = 0
# find shared values
for backpack in data:
    # split string in half
    one, two = backpack[:int(len(backpack)/2)], backpack[int(len(backpack)/2):]

    # convert to set
    one, two = set(one), set(two)

    # perform set intersection
    common_letter = str(one.intersection(two))[2] # {'X'} -> string -> middle letter is target

    # find priority value
    priority_sum += find_prio_val(common_letter)
    

print(f"Sum of priority values: {priority_sum}")

# part two:

data_2 = []
# group data in groups of three
for i, backpack in enumerate(data):
    if i % 3 == 0:
        data_2.append([])
    data_2[-1].append(backpack)

priority_sum_2 = 0
for group in data_2:
    # convert all backpacks to sets
    # perform set intersection on all of them
    one, two, three = group
    one, two, three = set(one), set(two), set(three)

    common_letter = str(one.intersection(two.intersection(three)))[2]

    # add priority value
    priority_sum_2 += find_prio_val(common_letter)

print(f"Sum of priority values (part 2): {priority_sum_2}")