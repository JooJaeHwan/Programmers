'''
위클리 챌린지
최소직사각형
https://programmers.co.kr/learn/courses/30/lessons/86491?language=python3
'''


def solution(sizes):
    answer1=[]
    answer2=[]
    for size in sizes:
        answer1 += [size[0] if size[0] > size[1] else size[1]]
        answer2 += [size[1] if size[0] > size[1] else size[0]]

    return max(answer1) * max(answer2)

solution([[60, 50], [30, 70], [60, 30], [80, 40]])
# result = 4000