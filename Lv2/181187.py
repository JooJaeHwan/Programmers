'''
연습문제
두 원 사이의 정수 쌍
https://school.programmers.co.kr/learn/courses/30/lessons/181187?language=python3
'''

def solution(r1, r2):
    # 1사분면에 있는 점의 갯수를 구하고 *4를 하는 방법
    answer = 0
    min_y, max_y = r1, r2
    for i in range(0, r2):
        
        # max_y를 줄여가며 범위를 줄인다
        while r2 ** 2 < max_y ** 2 + i ** 2:
            max_y -= 1
        # min_y를 줄여가며 범위를 줄인다
        # x축위에 있는 값들을 포함하게 되면 중복이 되기 때문에 제외 
        while min_y - 1 and r1 ** 2 <= (min_y - 1) ** 2 + i ** 2:
            min_y -= 1
        
        # 범위 사이에 있는 점들 더하기
        answer += max_y - min_y + 1
    # 총 4사분면 까지니깐 4를 곱해줌
    return answer * 4