'''
연습문제
하샤드 수
https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3
'''


def solution(x):
    return True if x % sum([int(str(x)[i]) for i in range(len(str(x)))]) == 0 else False


solution(10)
# result = True