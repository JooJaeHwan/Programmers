'''
2018 KAKAO BLIND RECRUITMENT
[3차] 압축
https://programmers.co.kr/learn/courses/30/lessons/17684?language=python3
'''

def solution(msg):
    answer = []
    d = {chr(c):c - ord('A') + 1 for c in range(ord('A'), ord('Z') + 1)}    # A-Z까지 1~27 키와 벨류를 d로 할당 
    idx = 27        # Z 다음 27
    start, end = 0, 1  

    while end < len(msg) + 1:   # end가 msg 길이 +1 을 넘어서면 종료
        s = msg[start:end]      # msg의 start에서 end index까지의 값
        if s in d:              # d에 만약 있는 단어라면
            end += 1            # end에 1을 더함
        else:                   
            answer.append(d[s[:-1]])    # s값중 맨 마지막 스펠링을 뺀 값을 키로 하는 벨류를 answer에 저장
            d[s] = idx                  # s를 키 idx를 value로 가지는 값 추가
            idx += 1                    # idx 값을 1 더함
            start = end - 1             # start를 end - 1값으로 변경 
    answer.append(d[s])                 # 반복문 종료 후 s를 키 idx를 value로 가지는 값 추가
    return answer


solution('KAKAO')
# result = [11, 1, 27, 15]        