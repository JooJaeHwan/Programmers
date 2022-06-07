'''
연습문제
자연수 뒤집어 배열로 만들기
https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3
'''


def solution(n):
    return [int(str(n)[-i]) for i in range(1,len(str(n))+1)]


solution(12345)
# result = [5, 4, 3, 2, 1]