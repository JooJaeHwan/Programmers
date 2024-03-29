'''
연습문제
달리기 경주
https://school.programmers.co.kr/learn/courses/30/lessons/178871
'''


def solution(players, callings):    
    player_dict = {player:rank for rank, player in enumerate(players)}
    rank_dict = {rank:player for rank, player in enumerate(players)}
    
    for call in callings:
        rank = player_dict[call]
        
        player_dict[rank_dict[rank-1]], player_dict[rank_dict[rank]] = player_dict[rank_dict[rank]], player_dict[rank_dict[rank-1]]
        rank_dict[rank-1], rank_dict[rank] = rank_dict[rank], rank_dict[rank-1]
    
    return list(rank_dict.values())


solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])
# result = ["mumu", "kai", "mine", "soe", "poe"]