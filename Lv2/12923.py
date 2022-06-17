'''
연습문제
숫자 블록
https://programmers.co.kr/learn/courses/30/lessons/12923?language=python3
'''


def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        k = int(i != 1)                 # i가 1이면 0, 1이 아니면 1을 대입
        for j in range(2, int(i**0.5)+1):
            if i%j == 0 and i//j <= 10000000:
                k = i//j
                break
        answer.append(k)

    return answer

solution(1, 10)
# result = [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]