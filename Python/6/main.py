# read iu in file, store as long string

data = []
with open("./Python/6/input.txt") as f:
    for line in f.readlines():
        data.append(line.strip()) # remove white space

# go through string, from 4th character onwards
# if all 4 letters are different, return index
for elt in data:
    found = False
    for i, ch in enumerate(elt[3:]):
        # print(elt[i:i+4])
        if len(set(elt[i:i+4])) == 4 and not found:
            print(i+4)
            found = True

# part two
# same alg but offset of 14 instead of 4
for elt in data:
    found = False
    for i, ch in enumerate(elt[13:]):
        # print(elt[i:i+4])
        if len(set(elt[i:i+14])) == 14 and not found:
            print(i+14)
            found = True