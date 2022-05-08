'''
2019 카카오 개발자 겨울 인턴십
크레인 인형뽑기 게임
https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
'''

def solution(board, moves):
    moved = []
    count = 0
    for x in moves:     # moves를 하나씩 받아옴
        for i in range(len(board)):     # board 길이 만큼 반복
            c = x-1     # 인덱스는 0부터 시작이므로 -1을 해줌
            if board[i][c] != 0:       # board[i][c]가 0이 아닐때
                got = board[i][c]      # got은 board[i][c]로 변경
                board[i][c] = 0        # board[i][c]는 0으로 병경
                if len(moved) == 0:    # moved 리스트에 길이가 0이라면 got을 추가
                    moved.append(got)
                elif len(moved) > 0 and got != moved[-1]:    # moved 리스트의 길이가 0보다 크고 moved 마지막 값이 got과 같지 않으면 
                    moved.append(got)  # moved에 got을 추가
                else:   # 그 외의 상황일 때 count는 1을 증가시켜주고 moved의 마지막 값을 제거
                    count += 1
                    del moved[-1]
                break # 처음 0이 아닌부분만 하고 반복문 빠져 나옴
    return  count*2 


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
# result = 4