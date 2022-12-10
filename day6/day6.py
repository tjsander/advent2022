#!/usr/bin/env python3
import pytest

INPUT = 'day6/test_input.txt'
# INPUT = 'day6/example.txt'

def main():

    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()

    for line in Lines:
        print (process(line.strip()))
        
def process(inline):
    for i in range (14, len(inline)):
        setme = [*set(inline[i-14:i])]
        print (setme)
        if (len(setme) == 14):
            return i
        
        
if __name__ == '__main__':
    main()


### PYTEST ###

def test_process():
    assert process("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert process("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert process("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert process("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

