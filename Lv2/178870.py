'''
연습문제
연속된 부분 수열의 합
https://school.programmers.co.kr/learn/courses/30/lessons/178870
'''

def solution(sequence, k):
    answer = []
    n = len(sequence)
    limit_sum, end = 0,0
    
    for i in range(n):
        while limit_sum < k and end < n:
            limit_sum += sequence[end]
            end +=1
        
        if limit_sum == k:
            answer.append([i, end-1])
        
        limit_sum-= sequence[i]
    
    answer.sort(key=lambda x: x[1]-x[0])
    return answer[0]