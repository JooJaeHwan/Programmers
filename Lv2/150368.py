'''
2023 KAKAO BLIND RECRUITMENT
이모티콘 할인행사
https://school.programmers.co.kr/learn/courses/30/lessons/150368
'''


from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    for discounts in product((40, 30, 20, 10), repeat=len(emoticons)):
        sold = [0, 0]   # 이모티콘, 판매액
        for user_discount, user_cost in users:
            sold_emoticons = 0
            for emoticon, discount in zip(emoticons, discounts):
                if discount >= user_discount:
                    sold_emoticons += emoticon * (1 - discount / 100)
            if sold_emoticons >= user_cost:
                sold[0] += 1
            else:
                sold[1] += sold_emoticons
        answer = max(answer, sold)
        
    return answer