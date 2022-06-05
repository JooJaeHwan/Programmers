'''
월간 코드 챌린지 시즌3
나머지가 1이 되는 수 찾기
https://programmers.co.kr/learn/courses/30/lessons/87389?language=python3
'''


def solution(n):
    for i in range(1,n+1):
        if n % i == 1:
            return i
        else: continue


solution(10)
# result = 3