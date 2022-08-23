from collections import deque

def bfs(map, idx, visited):
    q = deque([idx])    # deque 구조 사용
    dic = {0: [0, -1], 1:[-1, 0], 2:[0, 1], 3:[1, 0]}   # 좌우상하 움직이는 딕셔너리 만들기
    answer = 0
    while q:
        cnt = 0
        x, y = q.popleft()   # 맨 왼쪽 pop
        visited[x][y] = True    # 들어간 위치에 True로 설정
        for i in range(4):      # 상하좌우를 위해 4번 반복
            nx = x + dic[i][0]  
            ny = y + dic[i][1]
            if 0 <= nx < len(map) and 0 <= ny < len(map[0]):     # nx와 ny 가 범위 내에 있고 방문 했던 곳이 아니라면 
                if map[nx][ny] == 1:       
                    cnt += 1
                    if visited[nx][ny] == False and [nx, ny] not in q:
                        q.append([nx, ny])
        answer += (4-cnt)
        
    return answer


def solution(maps):
    answer = []
    visited = [[False]*len(maps[0]) for _ in range(len(maps))] 
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 1:
                answer.append(bfs(maps, [i,j], visited))
    return max(answer)

print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 1], [0, 0, 1, 0, 1], [1, 1, 1, 0, 1]]))