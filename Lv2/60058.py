'''
2020 KAKAO BLIND RECRUITMENT
괄호 변환
https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
'''

def divide(p):      # 괄호의 처음과 끝을 찾아주는 함수
    open_p = 0
    close_p = 0
    
    for i in range(len(p)):
        if p[i] == "(":
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[: i+1] , p[i+1:]

def check(u):       # 맞는 괄호 확인하는 함수
    stack = []
    
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True
def solution(p):  
    # 과정 1
    if p == '':
        return p
    
    # 과정 2
    u, v = divide(p)
    
    # 과정 3
    if check(u):
        # 과정 3-1
        return u + solution(v)
    
    # 과정 4
    else:
        # 과정 4-1
        answer = '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'
        # 과정 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
        
        return answer


solution("(()())()")
# result = 	"(()())()"