'''
월간 코드 챌린지 시즌1
이진 변환 반복하기
https://programmers.co.kr/learn/courses/30/lessons/70129?language=python3
'''


import re

def solution(s):
    cnt = 0
    zero_cnt = 0

    while s != "1":
        length = len(s)
        s = str(re.sub(r'[0]', '', s))
        cnt += 1
        zero_cnt += length - len(s)
        s = bin(len(s))[2:]

    return [cnt, zero_cnt]



solution("110010101001")
# result = [3, 8]