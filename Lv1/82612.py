'''
위클리 챌린지
부족한 금액 계산하기
https://programmers.co.kr/learn/courses/30/lessons/82612?language=python3
'''


def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        answer += price*i
    if answer < money:
        return 0
    return answer - money


solution(3, 20, 4)
# result = 10 