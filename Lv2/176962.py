'''
연습문제
과제 진행하기
https://school.programmers.co.kr/learn/courses/30/lessons/176962
'''


def solution(plans):
    
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])
    answer = []
    while plans:
        x = plans.pop()
        for idx, val in enumerate(answer):
            if val[0] > x[1]:
                answer[idx][0] += x[2]
        answer.append([x[1] + x[2], x[0]])
    answer.sort()
    return list(map(lambda x: x[1], answer))