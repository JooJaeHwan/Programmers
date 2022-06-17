'''
연습문제
다음 큰 숫자
https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3
'''


def solution(n):
    big_n = n+1
    while [*bin(n)[2:]].count("1") != [*bin(big_n)[2:]].count("1"):
        big_n += 1
    return big_n



solution(78)
# result = 83