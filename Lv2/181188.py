'''
연습문제
요격 시스템
https://school.programmers.co.kr/learn/courses/30/lessons/181188?language=python3
'''


def solution(targets):
    answer = 0
    targets.sort(key = lambda x: [x[1], x[0]])
    
    e = 0
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]

    return answer 