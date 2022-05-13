'''
2021 KAKAO BLIND RECRUITMENT
메뉴 리뉴얼
https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3
'''

from itertools import combinations
from collections import Counter

'''
combinations 조합
'''

def solution(orders, course):
    answer = []
    for c in course:    # course에서 값을 하나씩 받아옴
        temp = []       
        for order in orders:    # order의 값을 하나씩 받아옴
            combi = combinations(sorted(order), c)      # combinations 함수를 이용해서 order를 정렬한 것을 c개씩 묶은 조합을 combi에 할당
            temp += combi   # temp에 combi를 추가
        counter = Counter(temp) # Counter 함수를 이용해서 counter에 개수를 카운트
        if len(counter) != 0 and max(counter.values()) != 1:    # counter의 길이가 0이 아니고 counter의 value 값의 최대값이 1이 아닐경우
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]  

    return sorted(answer)



solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
# result = ["AC", "ACDE", "BCFG", "CDE"]