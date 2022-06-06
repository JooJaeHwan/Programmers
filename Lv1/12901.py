'''
연습문제
2016년
https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3
'''


import datetime

def solution(a, b):
    answer = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return answer[datetime.datetime(2016, a, b).weekday()]


solution(5, 24)
# result = "TUE"