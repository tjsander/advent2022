#!/usr/bin/env python3

INPUT = 'day2/test_input.txt'

# 0 loss, 3 draw, 6 win
# (1 for Rock, 2 for Paper, and 3 for Scissors)

def main():
# A Y rock, paper
# B X paper, rock
# C Z scissors, scissors

    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    score = 0
    score2 = 0

    for line in Lines:
        # print (line[0])
        # print (line[2])
        you = line[0]
        me = line[2]

        if (you == "A"):
            if (me == "X"):
                score += 3
            elif (me == "Y"):
                score += 6
            elif (me == "Z"):
                score += 0

        if (you == "B"):
            if (me == "X"):
                score += 0
            elif (me == "Y"):
                score += 3
            elif (me == "Z"):
                score += 6

        if (you == "C"):
            if (me == "X"):
                score += 6
            elif (me == "Y"):
                score += 0
            elif (me == "Z"):
                score += 3


        if (me == "Y"):
            score += 2
        elif (me == "X"):
            score += 1
        elif (me == "Z"):
            score += 3


        if (me == "X"):
            score2 += 0
            if (you == "A"):
                score2 += 3
            elif (you == "B"):
                score2 += 1
            elif (you == "C"):
                score2 += 2
        elif (me == "Y"):
            score2 += 3
            if (you == "A"):
                score2 += 1
            elif (you == "B"):
                score2 += 2
            elif (you == "C"):
                score2 += 3
        elif (me == "Z"):
            score2 += 6
            if (you == "A"):
                score2 += 2
            elif (you == "B"):
                score2 += 3
            elif (you == "C"):
                score2 += 1

    print (score)
    print (score2)

if __name__ == '__main__':
    main()
