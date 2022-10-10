'''
연습문제
최고의 집합
https://school.programmers.co.kr/learn/courses/30/lessons/12938
'''


def solution(n, s):
    answer = []
    
    if s < n:
        return [-1]
    
    for _ in range(n):
        answer.append(s // n)

    idx = len(answer) - 1
    
    for _ in range(s - sum(answer)):
        answer[idx] += 1
        idx -= 1
        
    return answer



solution(2, 9)
# result = [4, 5]