'''
연습문제
N개의 최소공배수
https://school.programmers.co.kr/learn/courses/30/lessons/12953
'''


from math import gcd

def solution(arr):
    answer = arr[0]
    for i in arr[1:]:
        answer = (answer*i) // gcd(answer, i)
    return answer


solution([2,6,8,14])
# result = 168