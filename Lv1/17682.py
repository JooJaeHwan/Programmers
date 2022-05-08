'''
2018 KAKAO BLIND RECRUITMENT
[1차] 다트 게임
https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3
'''

def solution(dartResult):
    n = ''
    score = []
    for i in dartResult:    # dartResult를 하나씩 받아옴
        if i.isnumeric():   # i가 숫자라면 n에 i 를 추가
            n += i
        elif i == 'S':      # i가 S라면 앞에 받아온 숫자를 1제곱을 하고 score에 추가함
            n = int(n)**1
            score.append(n)
            n = ''          # n을 초기화
        elif i == 'D':      # i가 D라면 앞에 받아온 숫자를 2제곱을 하고 score에 추가함
            n = int(n)**2   
            score.append(n)
            n = ''          # n을 초기화
        elif i == 'T':      # i가 T라면 앞에 받아온 숫자를 3제곱을 하고 score에 추가함
            n = int(n)**3
            score.append(n)
            n = ''          # n을 초기화
        elif i == '*':      # i가 *이라면 
            if len(score) > 1:  # score의 길이가 1보다 크면 전전까지 점수 2배
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:               
                score[-1] = score[-1] * 2
        elif i == '#':          # i가 # 이라면 가장 최근 score의 값을 -1배 해줌
            score[-1] = score[-1] * -1
        
    return sum(score)       # score을 모두 더해줌


solution('1S2D*3T')
# result = 37