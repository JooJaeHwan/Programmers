'''
2022 KAKAO BLIND RECRUITMENT
k진수에서 소수 개수 구하기
https://programmers.co.kr/learn/courses/30/lessons/92335?language=python3
'''


def convert(n, k):          # k 진수로 바꿔주는 함수
    result = ''
    q, r = divmod(n, k)
    if q == 0:
        return str(r)
    else:
        result += str(r)
        return convert(q, k) + result
def is_prime(num):          # 소수 인지 확인하는 함수
    if num == 1: return False
    for i in range(2, int(num**0.5)+1):
        if num % i  == 0:
            return False
    return True
def solution(n, k):         
    answer = convert(n, k)
    total = 0
    for num in answer.split('0'):
        if num.isdigit():
            if is_prime(int(num)):
                total += 1

    return total

solution(437674, 3)
# result = 3