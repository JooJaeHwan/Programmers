'''
연습문제
올바른 괄호
https://programmers.co.kr/learn/courses/30/lessons/12909?language=python3
'''

def solution(s):
    stack = []
    for i in [*s]:      # 문자열을 쪼개서 리스트에 넣어 하나씩 출력
        if i == '(':    # 만약 i가 '(' 라면 stack에 i 추가
            stack.append(i)
        else:           
            if stack == []:  # stack이 비어 있으면 False 반환
                return False
            else:
                if stack[-1] == '(':    # stack이 비어 있지 않고 stack에 마지막 값이 '('라면 stack.pop()
                    stack.pop()
    if stack != []:     # 반복문을 다돌고 나왔을 때 stack이 비어 있지 않으면
        return False    # False 반환
    return True       



solution("()()")
# result = True