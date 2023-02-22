'''
연습문제
숫자 변환하기
https://school.programmers.co.kr/learn/courses/30/lessons/154538
'''


from collections import deque

def solution(x, y, n):
    dis = [0 for _ in range(y + 1)]
    q = deque([x])
    if x == y:
        return 0
    
    while q:
        val = q.popleft()
        for i in range(3):
            if i == 0:
                cur_val = val * 2
            if i == 1:
                cur_val = val * 3
            if i == 2:
                cur_val = val + n
            if cur_val > y or dis[cur_val]:
                continue
            if cur_val == y:
                return dis[val] + 1
            q.append(cur_val)
            dis[cur_val] = dis[val] + 1
    
    return -1