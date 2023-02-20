'''
연습문제
뒤에 있는 큰 수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/154539
'''


def solution(numbers):
    stack = []
    answer = [0] * len(numbers)
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    while stack:
        answer[stack.pop()] = -1
    
    return answer
