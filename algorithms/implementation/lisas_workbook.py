#!/usr/bin/python
n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
array = raw_input().strip().split(' ')
for i in range(0, n):
    array[i] = int(array[i])

special_problems = 0
total_page_count = 0
for c in array:
    page_count = (c / k) + (c % k > 0)
    chapter_problem_count = 0
    for i in range(total_page_count + 1, page_count + total_page_count + 1):
        page_problem_count = 0
        while page_problem_count < k and chapter_problem_count < c:
            if chapter_problem_count + 1 == i:
                special_problems += 1
            chapter_problem_count += 1
            page_problem_count += 1
        total_page_count += 1
print special_problems
