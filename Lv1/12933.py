'''
연습문제
정수 내림차순으로 배치하기
https://programmers.co.kr/learn/courses/30/lessons/12933?language=python3
'''


def solution(n):
    return int(''.join(sorted([str(n)[i] for i in range(len(str(n)))], reverse = True)))


solution(118372)
# result = 873211