'''
Summer/Winter Coding(~2018)
스킬트리
https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3
'''


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_list = [*skill]           # skill을 한 단어씩 풀어주는 과정
        for s in skill_tree:
            if s in skill:
                if  s != skill_list.pop(0):
                    break
        else:       # 반복문이 정상적으로 돌아 갔다면 작동
            answer += 1       
    return answer


solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
# result = 2