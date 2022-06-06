'''
연습문제
같은 숫자는 싫어
https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3
'''


def solution(arr):
    stack = []
    for a in arr:
        if len(stack) == 0:
            stack.append(a)
        if stack[-1] != a:
            stack.append(a)
    return stack


solution([1, 1, 3, 3, 0, 1, 1])
# result = [1, 3, 0, 1]