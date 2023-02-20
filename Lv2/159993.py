'''
연습문제
미로 탈출
https://school.programmers.co.kr/learn/courses/30/lessons/159993?language=python3
'''


from collections import deque

def bfs(maps, start, end):
    dist = {0 : [0, 1], 1 : [0, -1], 2 : [1, 0], 3 : [-1, 0]}
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque([])
    flag = False
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                q.append((i, j, 0))
                visited[i][j] = True
                flag = True; break
        
        if flag: break
            
    while q:
        y, x, cost = q.popleft()
        
        if maps[y][x] == end:
            return cost
            
    
        for i in range(4):
            nx = x + dist[i][0]
            ny = y + dist[i][1]

            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X' and not visited[ny][nx]:
                q.append((ny, nx, cost+1))
                visited[ny][nx] = True
    return -1
                
    
def solution(maps):
    start_to_lever = bfs(maps, 'S', 'L')	
    lever_to_end = bfs(maps, 'L', 'E') 
    

    if start_to_lever != -1 and lever_to_end != -1:
        return start_to_lever + lever_to_end
        
   	
    return -1