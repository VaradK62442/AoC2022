# read in file
data = []
with open("./Python/4/input.txt") as f:
    for line in f.readlines():
        # split line on comma
        data.append(line.strip().split(","))

count = 0
count_2 = 0
# check if one of the pair is contained within the other
for a, b in data:
    a_from, a_to = a.split("-")
    b_from, b_to = b.split("-")

    # convert number range to list
    a_range = set(range(int(a_from), int(a_to)+1))
    b_range = set(range(int(b_from), int(b_to)+1))

    # part 1
    # check if one is contained within the other
    if a_range.issubset(b_range) or b_range.issubset(a_range):
        count += 1

    # part two
    # check if there is any overlap
    if a_range.intersection(b_range) != set():
        count_2 += 1

print(count)
print(count_2)

