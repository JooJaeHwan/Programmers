'''
연습문제
땅따먹기
https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3
'''


def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[len(land)-1])
        


solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])
# result = 16