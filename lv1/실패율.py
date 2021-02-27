# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
import itertools
import copy

def calculate_failure(stage: int, stage_player_info: list):
    current_stage_players = 0
    num_players_failed = 0

    for player in stage_player_info:
        if player > stage:
            current_stage_players += 1

        elif player == stage:
            current_stage_players += 1
            num_players_failed += 1

    if current_stage_players != 0:
        return num_players_failed / current_stage_players

    else:
        return 0



def solution(N, stages_orig):
    result = {}
    stages = copy.deepcopy(stages_orig)

    for stage in range(1, N+1):
        result[stage] = calculate_failure(stage, stages)

    result_sorted = sorted(result.items(), key=lambda x: x[1], reverse=True)
    result_sorted = list(map(lambda x: x[0], result_sorted))
    return result_sorted


if __name__ == '__main__':
    N = 5
    stages= [2, 1, 2, 6, 2, 4, 3, 3]

    print(solution(N, stages))