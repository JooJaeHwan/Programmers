'''
연습문제
정수 제곱근 판별
https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3
'''


def solution(n):
    sqrt = n ** 0.5
    if sqrt % 1 == 0:
        return (sqrt+1) ** 2
    return -1


solution(121)
# result = 144