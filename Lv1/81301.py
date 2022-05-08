'''
2021 카카오 채용연계형 인턴십
숫자 문자열과 영단어
https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3
'''

def solution(s):
    # 0부터 9까지 영어 단어 딕셔너리 준비
    number = {'zero':'0','one':'1','two':'2', 'three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    stack = []
    answer = []
    for word in s: # s 값을 하나씩 받아옴
        if word.isalpha() == True: # 알파벳인 경우 stack 리스트에 word 추가
            stack.append(word)
            if ''.join(stack) in number: # stack에 쌓인 단어들이 number 안에 있는 key라면 value 값을 answer에 추가
                answer += number[''.join(stack)]
                stack = []
        elif word.isalnum() == True: # 숫자인 경우 answer에 바로 추가
            answer += word
        else: continue # 그 이외의 경우 넘어감
    
    return int(''.join(answer)) # 값들을 합쳐주고 정수화 

solution("one4seveneight")
# result = 1478