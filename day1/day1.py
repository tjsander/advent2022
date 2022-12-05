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
            elves.append(0)
            count += 1
        else:
            elves[count] += int(line)
    print (max(elves))

    elves.sort(reverse=True)
    print (elves[0])
    print (elves[1])
    print (elves[2])
    print (elves[0] + elves[1] +elves[2])

if __name__ == '__main__':
    main()
