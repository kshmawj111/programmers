# https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3
"""
    lock의 크기를 가로 세로 1씩 늘려서 홈으로 둔 다음
    key를 lock에 집어넣고 그 결과 확인하기

"""
from copy import deepcopy


# 90도로 돌리는 함수

def rotate_key(key):
    result = [[0 for x in range(len(key))] for _ in range(len(key))]

    for r in range(len(key)):
        for c in range(len(key)):
            result[c][len(key)-1-r] = key[r][c]

    return result


def check_board(board, key_length):
    lock_start_row, lock_start_col = key_length - 1, key_length - 1
    lock_length = len(board) - 2 * (key_length - 1)
    summation = 0

    for x in range(lock_start_row, lock_start_row + lock_length):
        for y in range(lock_start_col, lock_start_col+lock_length):
            summation += board[x][y]

    if summation == lock_length*lock_length:
        return True
    else:
        return False


# 넣을 위치는 정해져 있으므로 보드와 키의 값을 비교하도록 한다
def push_key(board, key, r, c):
    for rotation in range(4):
        # 키 보드에 넣어보기
        for k_r in range(len(key)):
            for k_c in range(len(key)):
                board[r+k_r][c+k_c] = board[r+k_r][c+k_c] ^ key[k_r][k_c]

        if check_board(board, len(key)):
            return True

        else:
            for k_r in range(len(key)):
                for k_c in range(len(key)):
                    board[r + k_r][c + k_c] = board[r + k_r][c + k_c] ^ key[k_r][k_c]

            key = rotate_key(key)

    return False


def solution(key, lock: list):
    answer = False
    board = deepcopy(lock)
    board_length = len(board)
    key_length = len(key)

    for x in range(key_length-1):
        board.insert(0, [1 for _ in range(board_length)])
        board.append([1 for _ in range(board_length)])

    for x in range(len(board)):
        board[x] = [1 for _ in range(key_length-1)] + board[x] + [1 for _ in range(key_length-1)]

    board_length = len(board)

    for r in range(board_length-key_length+1):
        for c in range(board_length-key_length+1):
            result = push_key(board, key, r, c)

            if result:
                return True

    return answer


if __name__ == '__main__':
    """k, l = [[1, 0, 0], [1, 1, 0], [1, 0, 0]], [[1, 1, 1,1], [1, 1, 0,1], [1, 0, 0, 0], [1,1,1,1]] # T
    print(solution(k, l))
    k, l = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[0, 1, 1], [1, 1, 1], [1, 1, 1]] # T
    print(solution(k, l))"""
    k, l = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]] # T
    print(solution(k, l))
    k, l = [[0, 0, 0], [1, 0, 0], [1, 1, 0]], [[1, 1, 1,1], [1, 1, 0,1], [1, 1, 0, 0], [1,1,1,1]] # T
    print(solution(k, l))


