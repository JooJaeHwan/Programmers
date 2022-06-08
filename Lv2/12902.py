'''
연습문제
3 x n 타일링
https://programmers.co.kr/learn/courses/30/lessons/12902?language=python3
'''

'''
가로 길이가 2일 때는 3이다.

가로 길이가 4일 때는 3*3 + 2 = 11이다.

가로 길이가 6일 때는 11*3 + 8 = 41이다.
'''

def solution(n):
    answer = 0
    dp = [0 for _ in range(n+1)]
    dp[0] = 1  # 아무것도 두지 않는 경우도 1가지
    sub = 0
    for i in range(2, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + sub * 2
        sub += dp[i - 2]

    answer = dp[n] % 1000000007

    return answer


solution(4)
# result = 11