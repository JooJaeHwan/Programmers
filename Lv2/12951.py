'''
연습문제
JadenCase 문자열 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12951
'''


def solution(s):
    s=s.split(' ')
    for i in range(len(s)):
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer


solution("3people unFollowed me")
# result = "3people Unfollowed Me"