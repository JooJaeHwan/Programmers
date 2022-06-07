'''
해시
위장
https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3
'''


from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    return reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
# result = 5