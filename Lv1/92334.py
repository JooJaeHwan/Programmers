'''
2022 KAKAO BLIND RECRUITMENT 
신고 결과 받기
https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3
'''


from collections import defaultdict 
'''
defaultdict 클래스의 생성자로 기본값을 생성해주는 함수를 넘기면, 
모든 키에 대해서 값이 없는 경우 자동으로 생성자의 인자로 넘어온 함수를 호출하여 그 결과값으로 설정
'''

def solution(id_list, report, k):
    answer = [0] * len(id_list) # 미리 id_list 길이 만큼의 answer에 0을 추가 
    
    report = set(report) # 중복 제거
    
    reporter = defaultdict(set) 
    cnt = defaultdict(int)
    suspended = []
    
    for r in report: # report 값을 하나씩 받아옴
        do_report, be_report = r.split() # 그 값을 split으로 do_report와 be_report로 나눠줌
        
        cnt[be_report] += 1 # cnt 딕셔너리에 be_report key에 value를 1씩 더해줌
        reporter[do_report].add(be_report) # reporter 딕셔너리에 do_report key에 be_report를 추가함
        
        if cnt[be_report] == k: # 정지 기준인 신고 횟수가 k번과 같아지면 suspended 리스트에 be_report를 추가 
            suspended.append(be_report)
    
    for s in suspended: # suspended 값을 하나씩 받아옴
        for i in range(len(id_list)): # id_list 길이 만큼 반복
            if s in reporter[id_list[i]]: # reporter 딕셔너리에 key 값에 id_list[i] 값이 존재하면 answer[i]에 1씩 더해줌
                answer[i] += 1

        
    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
# result = [2, 1, 1, 0]