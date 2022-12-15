#!/usr/bin/env python3

INPUT = 'day8/test_input.txt'
# INPUT = 'day8/example.txt'

def build_tree_arr(Lines):
    arr_y = []
    for line in Lines:
        line = line.strip()
        arr_x = []
        for char in line:
            arr_x.append(int(char))
        arr_y.append(arr_x)
    return arr_y
    
def size_of(tree_arr):
    x = len(tree_arr)
    y = len(tree_arr[0])
    return (f"x={x}, y={y}")

def is_visible(x, y, tree_arr):
    arr_size = len(tree_arr)
    if x==0 or y==0 or x==arr_size-1 or y==arr_size-1:
        return 1
    tree_height = int(tree_arr[y][x])

    if (tree_height > max(tree_arr[y][x+1:arr_size])):
        # print (f"Found! {x},{y}")
        return 1
    if (tree_height > max(tree_arr[y][0:x])):
        # print (f"Found! {x},{y}")
        return 1

    arr_y = []
    for i in range (0,arr_size):
        arr_y.append(tree_arr[i][x])
    if (tree_height > max(arr_y[y+1:arr_size])):
        return 1
    if (tree_height > max(arr_y[0:y])):
        return 1
    return 0

def count_visible(tree_arr):
    visible = 0
    for y in range(0, len(tree_arr)):
        for x in range(0, len(tree_arr)):
            visible += is_visible(x, y, tree_arr)
    return visible

def scenic_score(x, y, tree_arr):
    score = 0
    arr_size = len(tree_arr)
    tree_height = int(tree_arr[y][x])
    
    # if x==0 or y==0 or x==arr_size-1 or y==arr_size-1:
    #     return 1

    n = 0
    for i in range(x+1, arr_size):
        n += 1
        if (tree_arr[y][i] >= tree_height):
            break
        
    s = 0
    for i in range(x-1, -1, -1):
        s += 1
        if (tree_arr[y][i] >= tree_height):
            break

    arr_y = []
    for i in range (0,arr_size):
        arr_y.append(tree_arr[i][x])

    e = 0
    for i in range(y+1,arr_size):
        e += 1
        if (arr_y[i] >= tree_height):
            break

    w = 0
    for i in range(y-1, -1, -1):
        w += 1
        if (arr_y[i] >= tree_height):
            break
        
    score = n * s * e * w

    return score

def max_scenic_score(tree_arr):
    max_score = 0
    for y in range(0, len(tree_arr)):
        for x in range(0, len(tree_arr)):
            score = scenic_score(x, y, tree_arr)
            if score > max_score:
                max_score = score
    return max_score

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    score = 0
    score2 = 0
    
    for i in range(10, 0, -1):
        print(i)


    for line in Lines:
        line = line.strip()
        print (line)
    
    tree_arr = build_tree_arr(Lines)
    # print (tree_arr)
    # print (tree_arr[4][2])
    # tree_arr[y][x]
    print (size_of(tree_arr))
    
    print (count_visible(tree_arr))
    print (max_scenic_score(tree_arr))

if __name__ == '__main__':
    main()
