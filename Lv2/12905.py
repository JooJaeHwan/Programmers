'''
연습문제
가장 큰 정사각형 찾기
https://programmers.co.kr/learn/courses/30/lessons/12905?language=python3
'''


def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] >= 1:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
    return max([num for row in board for num in row]) ** 2


solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])
# result = 9