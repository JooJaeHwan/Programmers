'''
연습문제
가운데 글자 가져오기
https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3
'''

def solution(s):
    return f'{s[len(s)//2 -1]}{s[len(s)//2]}' if len(s) % 2 == 0 else f'{s[len(s)//2]}'


solution("abcde")
# result = "c"