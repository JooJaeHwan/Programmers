'''
연습문제
추억 점수
https://school.programmers.co.kr/learn/courses/30/lessons/176963
'''


def solution(name, yearning, photo):
    dic = {n : y for n, y in zip(name, yearning)}
    answer = []
    for p in photo:
        sum_yearning = 0
        for i in p:
            if i in dic:
                sum_yearning += dic[i]
        answer.append(sum_yearning)
    return answer

solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])

# result = [19, 15, 6]