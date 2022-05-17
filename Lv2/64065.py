'''
2019 카카오 개발자 겨울 인턴십
튜플
https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3
'''

def solution(s):
    answer = []
    s = s[2:-2]                   
    s = s.split("},{")                  # "},{" 를 기준으로 split
    s.sort(key = len)                   # 길이를 기준으로 정렬
    for i in s:
        for j in i.split(","):
            if int(j) not in answer:
                answer.append(int(j))
        
    return answer


solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
# result = [2, 1, 3, 4]