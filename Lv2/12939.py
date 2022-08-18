'''
연습문제
최댓값과 최솟값
https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=python3
'''


def solution(s):
    answer = [int(i) for i in s.split(" ")]
    return " ".join([str(min(answer)), str(max(answer))])


solution("1 2 3 4 ")
# result = "1 4"