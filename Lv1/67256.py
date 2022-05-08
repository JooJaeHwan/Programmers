'''
2020 카카오 인턴십
키패드 누르기
https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3
'''

def solution(numbers, hand):
    answer = []
    lastL, lastR = 10, 12    # #과 * 시작점
    for i in numbers:    # numbers 값을 하나씩 받아옴
        if i in [1,4,7]:    # 1, 4, 7 일 때는 L을 answer에 추가 lastL을 i로 변경
            answer.append("L")
            lastL = i
        elif i in [3,6,9]:     # 3, 6, 9 일 때는 R을 answer에 추가 lastR을 i로 변경
            answer.append("R")
            lastR = i
        else: # 그리고 나머지 번호 일 때
            i = 11 if i==0 else i   # i가 0 일때는 11로 변경 나머지는 그대로
            
            absL = abs(i-lastL)     # 거리를 재기위해 절대값  
            absR = abs(i-lastR)     # 거리를 재기위해 절대값
            '''
            divmod 몫과 나머지를 튜플 형식으로 출력
            '''
            # 몫은 상, 하 나머지는 좌, 우
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):     # 거리가 오른쪽이 짧으면 R을 answer에 추가
                answer.append("R")
                lastR = i
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):   # 거리가 오른쪽이 짧으면 L을 answer에 추가
                answer.append("L")
                lastL = i
            else: # 만약 거리가 같다면 주손을 answer에 추가
                if hand == "right": 
                    answer.append("R")
                    lastR = i
                else:
                    answer.append("L")
                    lastL = i
    return ''.join(answer) # 모든 값을 join으로 합침

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
# result = "LRLLLRLLRRL"