'''
연습문제
호텔 대실
https://school.programmers.co.kr/learn/courses/30/lessons/155651
'''


import heapq

def solution(book_time):
    answer = 1
    
    book_time_ref = [(int(start[:2]) * 60 + int(start[3:]), int(end[:2]) * 60 + int(end[3:])) for start, end in book_time]
    book_time_ref.sort()
    heap = []
    for start, end in book_time_ref:
        if not heap:
            heapq.heappush(heap, end)
            continue
        if heap[0] <= start:
            heapq.heappop(heap)
        else:
            answer += 1
        heapq.heappush(heap, end + 10)
    return answer