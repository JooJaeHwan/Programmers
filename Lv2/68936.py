'''
월간 코드 챌린지 시즌1
쿼드압축 후 개수 세기
https://programmers.co.kr/learn/courses/30/lessons/68936?language=python3
'''


def solution(arr):
    answer = [0, 0]
    N = len(arr)
    def quad_comp(x, y, n):
        init = arr[x][y]        # 해당 네모값중 하나 값과 모두 같아야 통과임
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != init:        # 한번이라도 다르면 그 네모는 압축불가
                    div_n = n // 2
                    quad_comp(x, y, div_n)
                    quad_comp(x, y + div_n, div_n)
                    quad_comp(x + div_n, y, div_n)
                    quad_comp(x + div_n, y + div_n, div_n)
                    return
        # 무사히 다 통과했다면 압축가능
        answer[init] += 1
    quad_comp(0, 0, N)
    return answer


solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
# result = [4, 9]