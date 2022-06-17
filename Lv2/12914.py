'''
연습문제
멀리 뛰기
https://programmers.co.kr/learn/courses/30/lessons/12914?language=python3
'''


def solution(n):
    a, b = 1, 2
    if n == 1:
        return 1
    for i in range(2,n):
        a, b = b, a+b
        

solution(3)
# result = 3