'''
연습문제
숫자의 표현
https://programmers.co.kr/learn/courses/30/lessons/12924?language=python3
'''

'''
a = n/k + (1-k)/2
'''

def solution(n):
    return len([i for i in range(1,n+1,2) if n % i == 0])

solution(15)
# result = 4