'''
연습문제
핸드폰 번호 가리기
https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3
'''


def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]


solution("01033334444")
# result = "*******4444"