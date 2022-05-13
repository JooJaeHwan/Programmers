'''
2019 KAKAO BLIND RECRUITMENT
오픈채팅방
https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
'''

def solution(record):
    answer = []
    userdict = {}
    for mes in record:      # record를 하나씩 받아옴
        if mes.split(" ")[0] == "Enter" or mes.split(" ")[0] == "Change":           # 빈칸을 기준으로 split을 하고 첫번째가 Enter이나 Change 일 때
            userdict[mes.split(" ")[1]] = mes.split(" ")[2]                         # 두번째 값을 key에 세번째 값을 value 값에 추가
        
    for mes in record:      # record를 하나씩 받아옴
        if mes.split(" ")[0] == "Enter":                                            # 빈칸을 기준으로 split을 하고 첫번째가 Enter 이라면
            answer.append("{}님이 들어왔습니다.".format(userdict[mes.split(" ")[1]]))   # answer에 userdict에 mes.split(" ")[1] 겂 남이 들어왔습니다. 를 추가
        
        elif mes.split(" ")[0] == "Leave":                                          # 빈칸을 기준으로 split을 하고 첫번째가 Leave 이라면
            answer.append("{}님이 나갔습니다.".format(userdict[mes.split(" ")[1]]))     # answer에 userdict에 mes.split(" ")[1] 겂 남이 나갔습니다. 를 추가
        
        else: pass # 그외의 값이라면 pass
        
    
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
# result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]