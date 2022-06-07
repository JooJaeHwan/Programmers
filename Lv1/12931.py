'''
연습문제
자릿수 더하기
https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3
'''


def solution(n):
    return sum([int(str(n)[i]) for i in range(len(str(n)))])


solution(123)
# result = 6