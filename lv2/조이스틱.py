# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3


def calculate_min_up_down(current_char, target_char, alphabets_list):
    if isinstance(current_char, str):
        current_char = ord(current_char)

    if isinstance(target_char, str):
        target_char = ord(target_char)

    forward = target_char - current_char
    backward = len(alphabets_list) - forward
    return min(forward, backward)


def calculate_min_left_right(name):
    num_A_observed = 0
    total_moves = 0

    if isinstance(name, str):
        for char in name:
            if char == 'A':
                num_A_observed += 1

            else:
                total_moves += num_A_observed + 1
                num_A_observed = 0

        return total_moves

    elif isinstance(name, list):
        for e in name:
            if e == 0:
                num_A_observed += 1

            else:
                total_moves += num_A_observed + 1
                num_A_observed = 0

        return total_moves


def greedy_probe(name):
    extended = list(name[1:]) + list(name)

    for e in range(len(extended)):
        if extended[e] == 'A':
            extended[e] = 0

        else:
            extended[e] = 1

    extended_length = len(extended)

    # 시작 위치를 초기 값으로 포함 하여 시작
    i = (extended_length// 2) + 1
    num_of_moves = 1

    # 초기 시작 위치도 방문하였다고 한 뒤 탐색 시작
    extended[i-1] = 0

    while sum(extended) > 0:
        # 방문했음을 표시
        extended[i] = 0

        if i > extended_length / 2:
            paired_element_index = i - len(name)

        else:
            paired_element_index = i + len(name)

        extended[paired_element_index] = 0

        right_side = extended[i+1:]
        left_side = extended[:i]

        right_side_moves = calculate_min_left_right(right_side)
        left_side_moves = calculate_min_left_right(list(reversed(left_side)))

        # 모든 위치 다 갔다면
        if left_side_moves + right_side_moves == 0:
            break

        if right_side_moves > left_side_moves:
            i -= 1
            num_of_moves += 1

            while extended[i] == 0:
                num_of_moves += 1
                i -= 1

        else:
            i += 1
            num_of_moves += 1

            while extended[i] == 0:
                num_of_moves += 1
                i += 1

    return num_of_moves


def solution(name):
    alphabets = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    answer = 0

    right_probe = calculate_min_left_right(name[1:])
    left_probe = calculate_min_left_right(''.join(reversed(name[1:])))
    greedy_moves = greedy_probe(name)
    # 각 알파벳 별 카운트 계산
    for n in name:
        min_move = calculate_min_up_down('A', n, alphabets)
        answer += min_move

    answer += min(right_probe, left_probe, greedy_moves)
    print(answer)
    return answer


if __name__ == '__main__':
    n = [# 'ABABAAAAABA',
         'BBBAAAB',
         'BBAABB']
    for _n in n:
        solution(_n)