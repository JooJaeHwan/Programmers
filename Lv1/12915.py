'''
연습문제
문자열 내 마음대로 정렬하기
https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
'''


def solution(strings, n):
    return sorted(strings, key = lambda x : (x[n], x))


solution(["sun", "bed", "car"], 1)
# result = ["car", "bed", "sun"]