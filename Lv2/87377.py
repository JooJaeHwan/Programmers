'''
위클리 챌린지
교점에 별 만들기
https://programmers.co.kr/learn/courses/30/lessons/87377?language=python3
'''


def solution(line):
    star_list = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a*d - b*c != 0:
                x, y = (b*f - e*d) / (a*d - b*c), (e*c - a*f) / (a*d - b*c) # 행렬 연립 방정식 푸는 공식
                if x.is_integer() and y.is_integer():   # 정수판별
                    x, y = int(x), int(y)
                    if (x, y) not in star_list:         # star_list 내에 존재 여부 없으면 추가 
                        star_list.append((x,y))
    x_min, x_max, y_min, y_max = min(star_list)[0], max(star_list)[0], min(star_list,key = lambda x: x[1])[1], max(star_list,key = lambda x: x[1])[1]   # x, y 최대값과 최소값 할당
    star = [['.'] * (abs(x_max - x_min) + 1) for _ in range((abs(y_max - y_min))+1)]    # 제일 큰 x, y를 기준으로 "."로 채워진 배열 만들기
    for s in star_list: 
        a, b = s
        x, y = abs(y_max - b), abs(x_min - a)
        star[x][y] = "*"
    for i, v in enumerate(star):
        star[i] = ''.join(v)
    return star              