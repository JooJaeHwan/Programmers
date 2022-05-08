'''
2020 KAKAO BLIND RECRUITMENT
문자열 압축
https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
'''

def solution(s):
    result = []
    if len(s) == 1:     # s의 길이가 1이면 1을 반환 
        return 1
    for i in range(1, (len(s)//2) +1): # 1부터 s의 길이 // 2 +1 까지 반복 
        b = ''
        cnt = 1
        tmp = s[:i]     # tmp에 s[:i]을 할당
        
        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    b += str(cnt)+tmp
                else:
                    b += tmp
                tmp = s[j:i+j]
                cnt = 1
        if cnt != 1:
            b += str(cnt)+tmp
        else:
            b += tmp
        
        result.append(len(b))
    
            
    return min(result)