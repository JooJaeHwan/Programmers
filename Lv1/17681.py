'''
2018 KAKAO BLIND RECRUITMENT
[1차] 비밀지도
https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
'''

def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    '''
    bin 0b가 붙은 이진변환
    '''
    for i in range(n):
        arr1_bin.append(bin(arr1[i])[2:])       # 0b를 제거하고 이진변환 값만 추가
        arr2_bin.append(bin(arr2[i])[2:])       # 0b를 제거하고 이진변환 값만 추가
        arr1_bin[i] = ('0' * (n-len(arr1_bin[i]))) + arr1_bin[i]    # 비어있는 앞부분에 0을 추가
        arr2_bin[i] = ('0' * (n-len(arr2_bin[i]))) + arr2_bin[i]    # 비어있는 앞부분에 0을 추가
    
        tmp = ''
        for p in range(n):
            if arr1_bin[i][p] == '1' or arr2_bin[i][p] == '1':      # arr1_bin or arr2_bin에 1이 있으면 tmp에 '#'을 추가
                tmp += '#'
            elif arr1_bin[i][p] == '0' and arr2_bin[i][p] == '0':   # 둘다 0일 때 " "을 추가
                tmp += ' '
        answer.append(tmp)
    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
# result = 	["#####","# # #", "### #", "# ##", "#####"]