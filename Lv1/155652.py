'''
연습문제
둘만의 암호
https://school.programmers.co.kr/learn/courses/30/lessons/155652
'''


def solution(s, skip, index):
    answer = ''
    for i in s:
        a = ord(i)
        cnt = 0
        while cnt != index:
            a += 1
            if a > 122:
                a = 97
            if chr(a) not in skip:
                cnt += 1
        answer += chr(a)

                
    return answer