'''
위클리 챌린지
모음사전
https://programmers.co.kr/learn/courses/30/lessons/84512?language=python3
'''


from itertools import product
'''
product 중복 순열
'''
def solution(word):
    return sorted([''.join(list(c)) for i in range(1, 6) for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i)]).index(word) + 1


solution("AAAAE")
# result = 6

