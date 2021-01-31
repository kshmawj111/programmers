# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

# finds available element from the board with given column
def search_board(board, column):
    max_rows = len(board)-1
    current_row = 0

    # 어떤 칸에 인형이 나올 때까지 루프 실행
    while current_row <= max_rows:
        # 조사하는 칸에 인형이 없는 경는데
        target_cell_element = board[current_row][column]
        if target_cell_element == 0:
            current_row += 1

        else:
            doll = target_cell_element
            board[current_row][column] = 0
            return doll

    return 0


# 연속되어 매치 되는 경우 고려
def check_bucket(bucket: list):
    matched = 0

    while len(bucket) >= 2:
        last_index = len(bucket) - 1
        one_before_last = len(bucket) - 2

        if bucket[last_index] == bucket[one_before_last]:
            bucket.pop(last_index)
            bucket.pop(one_before_last)
            matched += 2

        # 맨 끝에 두 원소가 다른 경우엔 절대로 매치가 안되므로
        else:
            break

    return matched


def solution(board, moves):
    answer = 0
    bucket = []

    for mov in moves:
        crane_picked_doll = search_board(board, mov-1)
        if crane_picked_doll != 0:
            print(crane_picked_doll)
            bucket.append(crane_picked_doll)

        answer += check_bucket(bucket)
    return answer

if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]

    answer = solution(board, moves)

    print(f'answer: {answer}')