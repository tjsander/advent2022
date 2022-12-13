#!/usr/bin/env python3
import pytest
import parse
import flatdict
from pprint import pprint

INPUT = 'day7/test_input.txt'
# INPUT = 'day7/example.txt'

def main():

    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    
    import collections
    # print([item for item, count in collections.Counter(Lines).items() if count > 1])
    # dirs = parse_dirs(Lines, '/', 0)
    dirs = parse_dirs_new(Lines)
    print (dirs)
    dirs = dirs.reset_head()
    print (dirs)
    list = dirs.flatten()
    print (list)
    free_space(list)
    # total_sizes(list)
    
def total_sizes(list):
    total = 0
    list.sort()
    for size in list:
        if (size <= 100000):
            total += size
    print (f"Puzzle anser is {total}")
    
def free_space(list):
    disk_size = 70000000
    print(f"Disk size    = {disk_size}")
    list.sort()
    space_used = list.pop()
    print(f"Space used   = {space_used}")
    space_left = disk_size - space_used
    print(f"Space left   = {space_left}")

    needed_space = 30000000
    print(f"Update space needed = {needed_space}")

    needed_space -= space_left
    print(f"Update space 2free  = {needed_space}")
    
    

    print (list)
    for size in list:
        if size > needed_space:
            print (size)
            break
    2143088
    2042410
    
def flatten_sizes(Dirs):
    size_list = []
    if type(Dirs) is dict:
        for key in Dirs:
            if key == "size":
                print (Dirs["size"])
                size_list.append(int(Dirs["size"]))
            else:
                size_list.extend(flatten_sizes(Dirs[key]))
    else:
        if (len(Dirs) > 0):
            for item in Dirs:
                size_list.extend(flatten_sizes(item))
    return size_list

def parse_dirs(Lines, start_dir, idx):
    dirs = []
    log = False
    size = 0
    for i in range (idx, len(Lines)):
        line = Lines[i].strip()
        if (line.startswith("$ cd " + start_dir)):
            for j in range (i+2, len(Lines)):
                newline = Lines[j].strip()
                if (newline.startswith("$ ")):
                    break
                if (newline.startswith("dir ")):
                    new_dir = parse_dirs(Lines, newline.split(" ")[1], j)
                    dirs.append(new_dir)
                    size += new_dir["size"]
                else:
                    size += int(newline.split(" ")[0])
            break
    return {start_dir: dirs, "size": size}

class Directory():
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.files = {}
        self.size = 0
        if self.parent == None:
            self.parent = self
            
    def reset_head(self):
        while self.name != "/":
            self = self.get_parent()
            print (self)
        return self

    def flatten(self):
        size_arr = [self.size]
        for filename in self.files:
            size_arr.extend(self.files[filename].flatten())
        return size_arr

    def __str__(self):
        string = self.name
        return string
    
    def add_dir(self, Name):
        self.files[Name] = Directory(self,Name)
        
    def add_file(self, size):
        self.size += size
        if self.name != '/':
            self.parent.add_file(size)

    def get_child(self, Name):
        if Name in self.files:
            return self.files[Name]
        else:
            print (f"WARN {Name} not in filesystem")
            return self
    
    def get_parent(self):
        return self.parent

def parse_dirs_new(Lines):
    head = Directory(None, "/")
    dpth = -1
    for line in Lines:
        line = line.strip()
        if (line.startswith("$ cd ..")):
            head = head.get_parent()
            dpth -= 1
        elif (line.startswith("$ cd")):
            dpth +=1
            dirnm = line.split(" ")[2]
            head = head.get_child(dirnm)
        elif (line.startswith("$ ls")):
            continue
        elif (line.startswith("dir ")):
            dirnm = line.split(" ")[1]
            head.add_dir(dirnm)
            continue
        else:
            size = line.split(" ")[0]
            head.add_file(int(size))
            print ((dpth+1)*" " + line)
    return head
    

if __name__ == '__main__':
    main()
    



### PYTEST ###

def test_process():
    assert True
    # assert process("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    # assert process("nppdvjthqldpwncqszvftbrmjlhg") == 6
    # assert process("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    # assert process("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

