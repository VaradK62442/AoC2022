from copy import deepcopy


class Stack:
    def __init__(self, crates):
        self.crates = crates

    def __str__(self):
        return str(self.crates)

    def push(self, item):
        self.crates.append(item)

    def pop(self):
        item = self.crates[-1]
        self.crates = self.crates[:-1]
        return item
    
    def add(self, ls):
        # add given crates
        self.crates += ls
    
    def remove(self, n):
        # return which n crates to move from top
        to_move = self.crates[-n:]
        self.crates = self.crates[:-n]
        return to_move


def read_file(fname):
    # read in the file, store data
    instructions = []

    with open(fname) as f:
        for line in f.readlines():
            # find each instruction number, 
            # store number in instructions list
            words = line.split()
            instructions.append([int(words[1]), int(words[3]), int(words[5])])

    return instructions


def part1(data, instructions):
    data = deepcopy(data)
    # loop through instructions, carrying them out
    for instr in instructions:
        # instr[0] = number to move
        # instr[1] = which stack to move from
        # instr[2] = which stack to move to
        for _ in range(instr[0]):
            elt = data[instr[1]-1].pop()
            data[instr[2]-1].push(elt)

    return data


def part2(data, instructions):
    data = deepcopy(data)
    # loop through instructions, carrying them out
    for instr in instructions:
        # instr[0] = number to move
        # instr[1] = which stack to move from
        # instr[2] = which stack to move to
        ls = data[instr[1]-1].remove(instr[0])
        data[instr[2]-1].add(ls)

    return data


def print_top_crates(data):
    res = ''
    for i, stack in enumerate(data):
        print(f"Stack {i+1}: {stack.crates[-1]}")
        res += stack.crates[-1]

    return res


def main():
    # initialise data

    #     [D]    
    # [N] [C]    
    # [Z] [M] [P]
    #  1   2   3 

    test_data = [
        Stack(['Z', 'N']), # stack 1
        Stack(['M', 'C', 'D']), # stack 2
        Stack(['P']), # stack 3
    ]

    # [N]     [Q]         [N]            
    # [R]     [F] [Q]     [G] [M]        
    # [J]     [Z] [T]     [R] [H] [J]    
    # [T] [H] [G] [R]     [B] [N] [T]    
    # [Z] [J] [J] [G] [F] [Z] [S] [M]    
    # [B] [N] [N] [N] [Q] [W] [L] [Q] [S]
    # [D] [S] [R] [V] [T] [C] [C] [N] [G]
    # [F] [R] [C] [F] [L] [Q] [F] [D] [P]
    #  1   2   3   4   5   6   7   8   9 

    input_data = [
        Stack(['F', 'D', 'B', 'Z', 'T', 'J', 'R', 'N']),
        Stack(['R', 'S', 'N', 'J', 'H']),
        Stack(['C', 'R', 'N', 'J', 'G', 'Z', 'F', 'Q']),
        Stack(['F', 'V', 'N', 'G', 'R', 'T', 'Q']),
        Stack(['L', 'T', 'Q', 'F']),
        Stack(['Q', 'C', 'W', 'Z', 'B', 'R', 'G', 'N']),
        Stack(['F', 'C', 'L', 'S', 'N', 'H', 'M']),
        Stack(['D', 'N', 'Q', 'M', 'T', 'J']),
        Stack(['P', 'G', 'S']),
    ]

    test_instr = read_file("./Python/5/test.txt")
    input_instr = read_file("./Python/5/input.txt")

    data1 = part1(input_data, input_instr)
    data2 = part2(input_data, input_instr)

    print(print_top_crates(data1))
    print()
    print(print_top_crates(data2))


main()