'''
연습문제
두 정수 사이의 합
https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3
'''


def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a, b+1):
            answer += i
    elif a > b:
        for i in range(b, a+1):
            answer += i
    else: return a
    return answer


solution(3, 5)
# result = 12