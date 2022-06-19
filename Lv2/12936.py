'''
연습문제
줄 서는 방법
https://programmers.co.kr/learn/courses/30/lessons/12936?language=python3
'''

import math

def solution(n, k):
    k -= 1
    answer = []
    numbers = [*range(1, n+1)]

    for i in range(n, 0, -1):
        div, k = divmod(k, math.factorial(i-1))
        answer.append(numbers.pop(div))
    return answer

solution(3, 5)
# result = [3, 1, 2]
