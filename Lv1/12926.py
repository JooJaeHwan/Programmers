'''
연습문제
시저 암호
https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3
'''


def solution(s, n):
    '''
    chr() -> 아스키코드에서 문자로
    ord() -> 문자에서 아스키코드로
    '''
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)


solution("AB", 1)
# result = "BC"