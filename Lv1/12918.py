'''
연습문제
문자열 다루기 기본
https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3
'''


def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isnumeric()


solution("a234")
# result = False