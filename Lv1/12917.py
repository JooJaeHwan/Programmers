'''
연습문제
문자열 내림차순으로 배치하기
https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3
'''


def solution(s):
    return ''.join(sorted(s,reverse=True))


solution("Zbcdefg")
# result = "gfedcbZ"