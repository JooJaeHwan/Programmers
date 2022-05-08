'''
2019 KAKAO BLIND RECRUITMENT
실패율
https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
'''
from collections import defaultdict

def solution(N, stages):
    answer = defaultdict(int)
    long = len(stages)      # stages의 길이를 long
    for i in range(1,N+1):  # 1에서부터 N+1 까지 반복
        if long != 0:       # long이 0이 아닐떼
            count = stages.count(i)     # 숫자 개수합을 하니씩 count에 저장
            answer[i] = count / long    # answer 딕셔너리 i key에 count / long value 값을 추가
            long -= count   # long에 count를 뺀 값으로 변경
        else:               
            answer[i] = 0   # long이 0 이면 answer i key에 0 value 값을 추가
        
    return sorted(answer, key=lambda x : answer[x], reverse = True) # answer 값을 answer[x] key로 내림차순으로 정렬

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
# result = [3, 4, 2, 1, 5]