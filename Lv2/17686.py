'''
2018 KAKAO BLIND RECRUITMENT
[3차] 파일명 정렬
https://programmers.co.kr/learn/courses/30/lessons/17686?language=python3
'''

def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''     # head, number, tail 을 각각 ''로 초기화

        number_check = False                # number_check는 False로 할당
        for i in range(len(f)):             # f의 길이만큼 반복
            if f[i].isdigit():              # 만약 f[i]가 숫자라면
                number += f[i]              # number에 f[i]를 더하고
                number_check = True         # number_check를 True로 변경
            elif not number_check:          # 숫자가 아니고 number_check 값이 False라면 
                head += f[i]                # head에 f[i]를 더하고
            else:
                tail = f[i:]                # tail에 head,number이 들어가고 남은 값 다 할당
                break                       # 그리고 반복문 나가기
        answer.append((head, number, tail)) # (head, number, tail) 튜플 형식으로 answer 추가
    
    answer.sort(key=lambda x : (x[0].upper(), int(x[1])))   # key를 첫번째로 x[0].upper() 두번째로 int(x[1])을 기준으로 정렬 

    return [''.join(t) for t in answer]     # join으로 합쳐줌


solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
# result = ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]