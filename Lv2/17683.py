'''
2018 KAKAO BLIND RECRUITMENT
[3차] 방금그곡
https://programmers.co.kr/learn/courses/30/lessons/17683?language=python3
'''


def replace_code(code):
    code = code.replace('C#', 'c')
    code = code.replace('D#', 'd')
    code = code.replace('F#', 'f')
    code = code.replace('G#', 'g')
    code = code.replace('A#', 'a')
    return code

def solution(m, musicinfos):
    result = []

    for musicinfo in musicinfos:
        info = musicinfo.split(",")
        start_time = info[0].split(":")
        end_time = info[1].split(":")

        time = (int(end_time[0])- int(start_time[0])) * 60 + int(end_time[1]) - int(start_time[1])

        code = replace_code(info[3])
        code *= (time // len(code)) + code[:time % len(code)]

        if replace_code(m) in code:
            result.append([info[2], time])
    
    if len(result) == 0:
        return "(None)"

    else:
        result = sorted(result, key = lambda x: x[1], reverse=True)
        return result[0][0]



solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
# result = 'HELLO'