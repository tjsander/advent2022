#!/usr/bin/env python3
import numpy as np

# INPUT = 'input/day9example.txt'
INPUT = 'input/day9input.txt'

def parse_instructions(Lines):
    directions = []
    for line in Lines:
        ln = line.strip().split(" ")
        direction = ln[0]
        steps = int(ln[1])
        # print (f"Dir={direction} moving [{steps}] spaces")
        directions.append((direction, steps))
    
    visited = [(0,0)]
    head = (0,0)
    tail = (0,0)
    for direction in directions:
        for i in range (0, direction[1]):
            old_head = head
            head = head_one(head,direction[0])
            tail = tail_one(head,old_head,tail)
            visited.append(tail)
    print (visited)
    print (len(set(visited)))


def head_one(coordinate, direction):
    if direction == "U":
        return (coordinate[0], coordinate[1]+1)
    elif direction == "D":
        return (coordinate[0], coordinate[1]-1)
    elif direction == "L":
        return (coordinate[0]-1, coordinate[1])
    elif direction == "R":
        return (coordinate[0]+1, coordinate[1])
    else:
        print("ERROR")

def tail_one(head, old_head, tail):
    if head == tail:
        return tail
    if (within_one(head, tail)):
        return tail
    else:
        return old_head
    return -1

def within_one(head,tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return True
    return False

def main():

    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    score = 0
    score2 = 0

    parse_instructions((Lines))
    # for line in Lines:
    #     print (line)


if __name__ == '__main__':
    main()
