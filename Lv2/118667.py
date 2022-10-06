'''
2022 KAKAO TECH INTERNSHIP
두 큐 합 같게 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/118667
'''


from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    
    for _ in range(3*len(queue1)):
        if sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        elif sum2 > sum1:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        else:
            return answer
        answer += 1
    return -1


solution([3, 2, 7, 2], [4, 6, 5, 1])
# result = 2