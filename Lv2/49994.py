'''
Summer/Winter Coding(~2018)
방문 길이
https://programmers.co.kr/learn/courses/30/lessons/49994?language=python3
'''


def solution(dirs):
    x, y = 0, 0
    answer = set()
    for dir in [*dirs]:
        if dir == "U" and y < 5:
            answer.add(((x, y), (x, y + 1)))
            y += 1    
        elif dir == "D" and y > -5:
            answer.add(((x, y-1), (x, y)))
            y -= 1
        elif dir == "R" and x < 5:
            answer.add(((x, y), (x + 1, y)))
            x += 1
        elif dir == "L" and x > -5:
            answer.add(((x-1, y),(x, y)))
            x -= 1
    return len(answer)


solution("ULURRDLLU")
# result = 7