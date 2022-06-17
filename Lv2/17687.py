'''
2018 KAKAO BLIND RECRUITMENT
[3차] n진수 게임
https://programmers.co.kr/learn/courses/30/lessons/17687?language=python3
'''


def solution(n, t, m, p):

    def convert(n, base):                       # n진수로 바꿔주는 함수(재귀 사용)
        arr = '0123456789ABCDEF'
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]
    
    answer = '' 
    candidate = []

    for i in range(t*m):            # t*m 만큼 반복
        conv = convert(i, n)        # i를 n진수로 변경
        for c in conv:              # n진수로 변경한 값을 한 단어씩 candidate에 추가
            candidate.append(c)
    
    for i in range(p-1, t*m, m):    # p-1에서 t*m 까지 m 스탭으로 반복
        answer += candidate[i]      # answer에 candidate i번째 인덱스 값 더하기

    return answer


solution(2, 4, 2, 1)
# result = "0111"