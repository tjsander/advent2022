#!/usr/bin/env python3

INPUT = 'day4/test_input.txt'
# INPUT = 'day4/example.txt'

def main():

    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    score = 0
    for line in Lines:
        out = line.strip().split(',')
        ass1 = out[0].split('-')
        ass2 = out[1].split('-')
        if (int(ass1[0]) >= int(ass2[0]) and int(ass1[1]) <= int(ass2[1])):
            score+=1
        elif (int(ass1[0]) <= int(ass2[0]) and int(ass1[1]) >= int(ass2[1])):
            score+=1

    print (score)

    score = len(Lines)
    for line in Lines:
        out = line.strip().split(',')
        ass1 = out[0].split('-')
        ass2 = out[1].split('-')
        if (int(ass1[0]) > int(ass2[1]) or int(ass2[0]) > int(ass1[1])):
            score-=1
        elif (int(ass2[1]) < int(ass1[0]) or int(ass2[1]) < int(ass1[0])):
            score-=1
    print (score)


if __name__ == '__main__':
    main()
