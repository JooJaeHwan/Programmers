'''
연습문제
행렬의 곱셈
https://school.programmers.co.kr/learn/courses/30/lessons/12949
'''


def solution(arr1, arr2):
    return [[sum(a*b for a, b in zip(arr1_row,arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1]


solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
# result = 	[[15, 15], [15, 15], [15, 15]]