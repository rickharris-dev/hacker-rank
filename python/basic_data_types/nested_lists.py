#!/usr/bin/python

n = int(raw_input().strip())
students = [None] * n

for i in range(n):
    student = raw_input().strip()
    grade = float(raw_input().strip())
    # Sorts lists by grade and student name
    if i == 0:
        students[i] = [student, grade]
    c = 0
    temp = [student, grade]
    while c <= i:
        if c == i:
            students[i] = temp
        elif students[c][1] > temp[1]:
            students[c], temp = temp, students[c]
        elif students[c][1] == temp[1] and students[c][0] > temp[0]:
            students[c], temp = temp, students[c]
        c = c + 1

lowest = students[0][1]
second_lowest = None
for i in range(1,n):
    if not second_lowest and students[i][1] != lowest:
        second_lowest = students[i][1]
        print students[i][0]
    elif second_lowest and students[i][1] == second_lowest:
        print students[i][0]
    elif second_lowest:
        break
