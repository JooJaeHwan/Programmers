'''
연습문제
최대공약수와 최소공배수
https://programmers.co.kr/learn/courses/30/lessons/12940?language=python3
'''


def solution(n, m):
    '''
    유클리드 호제법
    '''
    c, d = max(n, m), min(n, m)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(n*m/c)]
    return answer


solution(3, 12)
# result = [3, 12]