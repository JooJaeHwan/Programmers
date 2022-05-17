'''
2018 KAKAO BLIND RECRUITMENT
[1차] 뉴스 클러스터링
https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3
'''

from collections import Counter
'''
Counter 받아온 값을 하나 하나 Dict에 넣어줌
'''

def solution(str1, str2):
    str1_low = str1.lower()     # 소문자로 전환
    str2_low = str2.lower()     # 소문자로 전환
    
    str1_list = []
    str2_list = []
    
    for i in range(len(str1_low)-1):    # len(str1_low)-1 길이 만큼 반봅
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():   # str1_low의 i 인덱스 값이 알파벳이고 i+1 인덱스 값이 알파벳이면
            str1_list.append(str1_low[i] + str1_low[i+1])       # str1_low[i] + str1_low[i+1] 값을 str1_list에 추가 
    for j in range(len(str2_low)-1):    # # len(str2_low)-1 길이 만큼 반봅
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():   # str2_low의 i 인덱스 값이 알파벳이고 i+1 인덱스 값이 알파벳이면
            str2_list.append(str2_low[j] + str2_low[j+1])       # str2_low[i] + str2_low[i+1] 값을 str2_list에 추가 
    
    counter1 = Counter(str1_list)   
    counter2 = Counter(str2_list)
    
    inter = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    
    if len(inter) == 0 and len(union) == 0:
        return 65536
    
    else: return int(len(inter) / len(union) * 65536)


solution('FRANCE', 'french')
# result = 16384