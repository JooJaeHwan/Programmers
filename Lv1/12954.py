'''
연습문제
x만큼 간격이 있는 n개의 숫자
https://programmers.co.kr/learn/courses/30/lessons/12954?language=python3
'''


def solution(x, n):
    return [x * i for i in range(1, n+1)]


solution(2, 5)
# result = [2, 4, 6, 8, 10]