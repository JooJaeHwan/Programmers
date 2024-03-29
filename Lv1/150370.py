'''
연습문제
개인정보 수집 유효기간
https://school.programmers.co.kr/learn/courses/30/lessons/150370
'''


from dateutil.relativedelta import relativedelta
from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    today = datetime.strptime(today, "%Y.%m.%d").date()
    terms = {term.split(" ")[0] : int(term.split(" ")[1]) for term in terms}
    for idx, privacy in enumerate(privacies):
        date = datetime.strptime(privacy.split(" ")[0], "%Y.%m.%d").date()
        period = terms[privacy.split(" ")[1]]
        if date + relativedelta(months=period) <= today:
            answer.append(idx+1)
    return answer


solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])

# result = [1, 3]