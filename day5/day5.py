#!/usr/bin/env python3

INPUT = 'day5/test_input.txt'
# INPUT = 'day5/example.txt'

def main():
    stacks = parse_stacks(INPUT)
    instructions = parse_instructions(INPUT)
    print (stacks)
    # print (instructions)
    processed_stacks = process(stacks, instructions)
    print (processed_stacks)
    
    string = ''
    for stack in processed_stacks:
        string += (stack.pop())
    print (string)
    

def process(stacks, instructions):
    for line in instructions:
        for i in range(1,int(line[0])+1):
            start = int(line[1]) - 1
            end = int(line[2]) - 1
            stacks[end].append(stacks[start].pop())
    return stacks

def parse_instructions(input_file):
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    instructions = []
    for i in range (Lines.index("\n")+1, len(Lines)):
        line = Lines[i]
        count = line.split(" ")[1]
        start = line[-7]
        end = line[-2]
        # print (f"Count {count} {start} {end}")
        instructions.append([count, start, end])
    return instructions
    
def parse_stacks(input_file):
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    num_stacks = int(Lines[Lines.index("\n") - 1].split(" ")[-2])
    
    rows = []

    for i in range (Lines.index("\n") -2, -1, -1):
        stack = []
        for j in range (1, num_stacks*4, +4):
            # print (Lines[i][j])
            stack.append(Lines[i][j])
        # print (stack)
        rows.append(stack)
    # print (rows)

    stacks = [] * num_stacks
    for i in range (0, num_stacks):
        stacks.append([])

    for row in rows:
        for i in range(0,num_stacks):
            if (row[i] != ' '):
                stacks[i].append(row[i])

    return stacks



if __name__ == '__main__':
    main()
