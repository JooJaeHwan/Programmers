'''
2020 카카오 인턴십
수식 최대화
https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3
'''

from itertools import permutations
'''
permutations 순열
'''
def solution(expression):
    operators = ["+","-","*"]       # 연산자 기호 리스트 생성
    answer = []
    for oper in permutations(operators, 3):     # 연산자의 조합을 하나씩 불러옴
        a, b = oper[0], oper[1]
        tmp_list = []
        for i in expression.split(a):           # 첫번째 연산자를 기준으로 split 
            tmp = [f"({j})" for j in i.split(b)]    
            tmp_list.append(f"({b.join(tmp)})")
        answer.append(abs(eval(a.join(tmp_list))))
    return max(answer)
    
solution("100-200*300-500+20")
# result = 60420