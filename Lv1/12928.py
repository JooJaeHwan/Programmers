'''
연습문제
약수의 합
https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3
'''


def solution(n):
    return sum([i for i in range(1, n+1) if n % i == 0])


solution(12)
# result = 28