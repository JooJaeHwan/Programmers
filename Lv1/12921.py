'''
연습문제
소수찾기
https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3
'''


from math import sqrt
'''
에라토스테네스의 체(Sieve of Eratosthenes)
'''
def solution(n):
    num = set(range(2, n+1))
    for i in range(2, int(sqrt(n+1))+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)


solution(10)
# result = 4