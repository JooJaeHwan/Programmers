'''
2022 KAKAO BLIND RECRUITMENT
주차 요금 계산
https://programmers.co.kr/learn/courses/30/lessons/92341?language=python3
'''

import math

def changeToMinute(first, second):
    h1, m1 = map(int, first.split(":"))
    h2, m2 = map(int, second.split(":"))
    total1, total2 = h1 * 60 + m1, h2 * 60 + m2

    return total2 - total1

def solution(fees, records):
    basic_time, basic_fee, part_time, part_fee = fees
    check = {}
    check_time = {}

    for record in records:
        time, car_number, inout = record.split()
        if inout == "IN":
            check[car_number] = time
        else:
            if car_number not in check_time:
                check_time[car_number] = changeToMinute(check[car_number], time)
            else:
                check_time[car_number] += changeToMinute(check[car_number], time)
            check[car_number] = "0"

    
    for key, value in check.items():
        if value != "0":
            if key in check_time:
                check_time[key] += changeToMinute(value, "23:59")
            else:
                check_time[key] = changeToMinute(value, "23:59")

    check_time = sorted(check_time.items())

    answer = []
    for car_number, time in check_time:
        if time <= basic_time:
            answer.append(basic_fee)
        else:
            answer.append(basic_fee + math.ceil((time - basic_time) / part_time) * part_fee)
        
    return answer


solution([180, 5000, 10, 600],
         ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
# result = [14600, 34400, 5000]