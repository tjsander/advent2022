#!/usr/bin/env python3

INPUT = 'day1/test_input.txt'

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    for line in Lines:
        if (line == "\n"):
            print ("ELF!" + str(count))
            count += 1

if __name__ == '__main__':
    main()
