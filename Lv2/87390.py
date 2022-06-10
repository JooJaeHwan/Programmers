'''
월간 코드 챌린지 시즌3
n^2 배열 자르기
https://programmers.co.kr/learn/courses/30/lessons/87390?language=python3
'''


def solution(n, left, right):
    return [max(divmod(i, n)) + 1 for i in range(left, right + 1)]


solution(3, 2, 5)
# result = [3, 2, 2, 3]