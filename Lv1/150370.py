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