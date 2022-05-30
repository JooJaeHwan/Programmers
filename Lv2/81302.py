'''
2021 카카오 채용연계형 인턴십
거리두기 확인하기
https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3
'''

from collections import deque

def bfs(p, idx):        # bfs 넓이우선탐색
    q = deque([idx])    # deque 구조 사용
    visited = [[False]*5 for _ in range(5)]     # 방문여부를 확인 할 수 있는 visited 리스트 만듦
    dic = {0: [0, -1], 1:[-1, 0], 2:[0, 1], 3:[1, 0]}   # 좌우상하 움직이는 딕셔너리 만들기
    
    while q:
        x, y, d = q.popleft()   # 맨 왼쪽 pop
        visited[x][y] = True    # 들어간 위치에 True로 설정
        
        for i in range(4):      # 상하좌우를 위해 4번 반복
            nx = x + dic[i][0]  
            ny = y + dic[i][1]
            nd = d + 1

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:     # nx와 ny 가 범위 내에 있고 방문 했던 곳이 아니라면
                visited[nx][ny] = True      # 이동한 위치에 True 설정
                
                if p[nx][ny] == 'P':        # 이동한 위치에 P라면
                    if nd <= 2:             # nd 2이하면 False 리턴
                        return False

                elif p[nx][ny] == 'O':      # 이동한 위치에 O이라면
                    if nd == 1:             # nd == 1 이라면 q에 현재 위치정보 추가
                        q.append([nx, ny, nd])

    return True
                    
def solution(places):
    answer = []
    
    for p in places:    # places 를 한줄씩 출력
        flag = 1        # flag를 1로 초기화
        
        for i in range(5):  
            for j in range(5):
                if p[i][j] == 'P': 
                    result = bfs(p, [i, j, 0])
                    if not result:  # result가 False 라면
                        flag = 0    # flag는 0으로 변경
                        
        answer.append(flag)         # answer에 flag 추가
        
    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
# result = [1, 0, 1, 1, 1]