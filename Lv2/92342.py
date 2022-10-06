'''
2022 KAKAO BLIND RECRUITMENT
양궁대회
https://school.programmers.co.kr/learn/courses/30/lessons/92342
'''


from collections import deque

def bfs(n, info):    
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                    res.clear()
                res.append(arrow)  # 최대점수차를 내는 화살상황 저장
        
        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏜 경우
            continue
        
        elif focus == 10:  # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        
        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1 
            q.append((focus+1, tmp))  # 어피치보다 1발 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))  # 0발 쏘기
    return res

def solution(n, info):
    winList = bfs(n, info)
    
    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]

"============================================================"

from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_gap = -1 # 점수차이
    
    for combi in combinations_with_replacement(range(11), n):
        info2 = [0] * 11
        
        for i in combi:
            info2[10-i] += 1
        apeach, lion = 0, 0
        for idx in range(11):
            if info[idx] == info2[idx] == 0:  # 라이언과 어피치 모두 한번도 화살을 맞히지 못한 경우
                continue
            elif info[idx] >= info2[idx]:  # 어피치가 라이언이 쏜 화살의 수 이상을 맞힌 경우
                apeach += 10 - idx
            else:  # 라이언이 어피치보다 많은 수의 화살을 맞힌 경우
                lion += 10 - idx
        if lion > apeach:  # 라이언이 점수가 더 높은 경우
            gap = lion - apeach  # 점수 차
            if gap > max_gap:  # 기존보다 더 큰 점수 차인 경우
                max_gap = gap
                answer = info2
    return answer


solution(5, [2,1,1,1,0,0,0,0,0,0,0])
# result = [0,2,2,0,1,0,0,0,0,0,0]