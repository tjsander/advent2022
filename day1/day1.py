#!/usr/bin/env python3

INPUT = 'day1/test_input.txt'

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    elves = []
    elves.append(0)
    for line in Lines:
        if (line == "\n"):
            # print ("ELF!" + str(count))
            elves.append(0)
            count += 1
        else:
            elves[count] += int(line)
    print (max(elves))


if __name__ == '__main__':
    main()
