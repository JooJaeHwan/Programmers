'''
2018 KAKAO BLIND RECRUITMENT
[1차] 캐시
https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3
'''


from collections import deque

def solution(cacheSize, cities):
    answer = 0
    buffer = deque()

    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()

        if city in buffer :         # buffer 안에 city가 있다면 answer를 1씩 증가
            answer += 1 
        else : answer += 5          # 없으면 answer를 5씩 증가

        if city in buffer :         # buffer 안에 city가 있다면 buffer에서 city 제거
            buffer.remove(city)
        else:
            if len(buffer) >= cacheSize: # buffer의 길이가 cacheSize 보다 크거나 같으면 맨 왼족 데이터 pop
                buffer.popleft()

        buffer.append(city)         # buffer에 city 추가

    return answer

    
solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
# result = 50

