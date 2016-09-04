#!/usr/bin/python

def convert_array(array, rows, cols):
    for i in range(0, rows):
        for j in range(0, cols):
            if array[i][j] == 'O':
                if i + 1 != rows and array[i + 1][j] == '.':
                    array[i + 1][j] = 'X'
                if i != 0 and array[i - 1][j] == '.':
                    array[i - 1][j] = 'X'
                if j + 1 != cols and array[i][j + 1] == '.':
                    array[i][j + 1] = 'X'
                if j != 0 and array[i][j - 1] == '.':
                    array[i][j - 1] = 'X'
    return array

def inverse_array(array, rows, cols):
    for i in range(0, rows):
        for j in range(0, cols):
            if array[i][j] == '.':
                if i + 1 != rows and array[i + 1][j] != '.':
                    array[i + 1][j] = 'x'
                if i != 0 and array[i - 1][j] != '.':
                    array[i - 1][j] = 'x'
                if j + 1 != cols and array[i][j + 1] != '.':
                    array[i][j + 1] = 'x'
                if j != 0 and array[i][j - 1] != '.':
                    array[i][j - 1] = 'x'
    return array

rows, cols, seconds = raw_input().strip().split(' ')
rows, cols, seconds = [int(rows), int(cols), int(seconds)]
array = []
for i in range(0,rows):
    array.append(list(raw_input().strip()))
if seconds == 1:
    for i in range(0, rows):
        print ''.join(array[i])
elif seconds % 2 == 0:
    for i in range(0, rows):
        print ''.join('O' for x in array[i])
elif seconds % 4 == 1:
    array = convert_array(array, rows, cols)
    array = inverse_array(array, rows, cols)
    for i in range(0, rows):
        print ''.join('O' if x == 'X' or x == 'O' else '.' for x in array[i])
elif seconds % 4 == 3:
    array = convert_array(array, rows, cols)
    for i in range(0, rows):
        print ''.join('.' if x == 'X' or x == 'O' else 'O' for x in array[i])
