'''
위클리 챌린지
전력망을 둘로 나누기
https://programmers.co.kr/learn/courses/30/lessons/86971?language=python3
'''

from collections import deque
from collections import defaultdict

def bfs(start, visited, graph):
    q =  deque([start])
    result = 1
    visited[start] = True
    while q:
        now = q.popleft()

        for i in graph[now]:
            if visited[i] == False:
                result += 1
                q.append(i)
                visited[i] = True
    return result

def solution(n, wires):
    answer = n
    graph = defaultdict(list)

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for start, not_visit in wires:
        visited = [False] * (n+1)
        visited[not_visit] = True
        result =  bfs(start, visited, graph)
        if abs(result - (n-result)) < answer:
            answer =  abs(result - (n-result))
    return answer


solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])
# result = 3