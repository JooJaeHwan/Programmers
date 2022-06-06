'''
연습문제
나누어 떨어지는 숫자 배열
https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3
'''


def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    if answer == []:
        return [-1]
    return sorted(answer)


solution([5, 9, 7, 10], 5)
# result = [5, 10]