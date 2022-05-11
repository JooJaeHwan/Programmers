'''
2020 KAKAO BLIND RECRUITMENT
문자열 압축
https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
'''

def solution(s):
    result = []
    if len(s) == 1:     # s의 길이가 0일 경우 1을 출력
        return 1
    for i in range(1, (len(s)//2) +1):      # 1에서 s의 길이 //2+1 만큼 반복
        b = ''      # b에 빈 str 할당
        cnt = 1     # cnt에 1을 할당
        tmp = s[:i] # tmp는 s[:i]을 할당
        
        for j in range(i, len(s), i):       # i에서 s의 길이 만큼 i 스탭만큼 반복
            if tmp == s[j:i+j]:             # 만약 tmp가 s[j:i+j]와 같다면
                cnt += 1                    # cnt를 1씩 증가
            else:                           # 그 이외라면
                if cnt != 1:                # cnt가 1이 아니라면 b에 cnt+tmp 문자열을 추가
                    b += str(cnt)+tmp   
                else:                       # cnt가 1이라면 그냥 tmp를 b에 추가
                    b += tmp
                tmp = s[j:i+j]              # tmp를 s[j:i+j]로 변경
                cnt = 1                     # cnt는 1로 다시 변경
        if cnt != 1:                        # cnt가 1이 아니라면 b에 cnt+tmp 문자열을 추가
            b += str(cnt)+tmp
        else:                               # cnt가 1이라면 그냥 tmp를 b에 추가
            b += tmp
        
        result.append(len(b))               # result에 b의 길이를 추가
    
            
    return min(result)                      # result에서 최소값 리턴