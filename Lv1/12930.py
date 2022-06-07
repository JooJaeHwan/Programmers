'''
연습문제
이상한 문자 만들기
https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3
'''


def solution(s):
    answer = ''
    for a in s.split(" "):
        for i in range(len(a)):
            if i % 2 == 0:
                answer += a[i].upper()
            else:
                answer += a[i].lower()
        answer += ' '        
    return answer[:-1]


solution("try hello world")
# result = "TrY HeLlO WoRlD"