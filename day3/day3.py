#!/usr/bin/env python3

INPUT = 'day3/test_input.txt'

def main():

    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    score = 0

    for line in Lines:
        # print (line)
        size = int((len(line) -1) /2)
        sack1 = set(line[0:size])
        sack2 = set(line[size:size*2])

        common = sack1.intersection(sack2)
        c_letter = common.pop()
        print (c_letter)
        print (ord(c_letter))

        if c_letter.isupper():
            score += (ord(c_letter) - 38)
        elif c_letter.islower():
            score += (ord(c_letter) - 96)
        else:
            print("ERROR!")
    print (score)

if __name__ == '__main__':
    main()
