'''
연습문제
수박수박수박수박수박수?
https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3
'''


def solution(n):
    return ''.join(["수박"[i%2] for i in range(n)])

solution(3)
# result = "수박수"