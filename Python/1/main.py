# read in file
# calculate highest
elves = [[]]
totals = []
maximum = -1
total = 0
with open ("./Python/1/input.txt") as f:
    for line in f.readlines():
        if line == '\n':
            elves.append([])
            totals.append(total)
            if total > maximum:
                maximum = total
            total = 0
        else:
            elves[-1].append(int(line))
            total += int(line)

# display result
print("number of elves: ", len(elves))
print("maximum: ", maximum)

# for part two, find sum of three highest amounts
totals.sort()
print("top 3 elves: ", totals[-3:])
print("total of top 3: ", sum(totals[-3:]))