# https://programmers.co.kr/learn/courses/30/lessons/17679?language=python3


# 아래에서 작업을 좀 더 직관적으로 하기 위해 전치시킨 게임판을 리턴한다
def initialize_board(height, width, board: list):
    new_board = [[] for _ in range(width)]
    for x in range(height):
        for w in range(width):
            new_board[w].append(board[x][w])

    return new_board


def mark_delete(board):
    delete_list = []
    for r in range(1, len(board)):
        for c in range(1, len(board[0])):
            if board[r][c] == board[r-1][c-1] == board[r-1][c] == board[r][c-1] and board[r][c] != 0:
                delete_list.append((r, c))

    return delete_list


def delete_marked(board, delete_list):
    num_deleted = 0
    original_cols = len(board[0])
    REMOVE_TARGET = -1

    # 지울 인덱스를 -1로 지정
    for r, c in delete_list:
        for x in range(-1, 1):
            for y in range(-1, 1):
                board[r+x][c+y] = REMOVE_TARGET

    # 각 행에서 지울 값이 있는지 확인하고 있다면 값을 제거함
    for row in board:
        while REMOVE_TARGET in row:
            row.remove(REMOVE_TARGET)
            num_deleted += 1

    # 값이 움직인거를 표현하기 위해 앞에 0을 추가함.
    # transposed 된 보드이기 때문에 앞에다 추가하였음.
    for row in board:
        while len(row) < original_cols:
            row.insert(0, 0)

    return num_deleted


def solution(m, n, board):
    answer = 0
    board = initialize_board(m, n, board)
    delete_list = mark_delete(board)

    while delete_list:
        answer += delete_marked(board, delete_list)
        delete_list = mark_delete(board)

    return answer


if __name__ == '__main__':
    m  = 4
    n = 5
    b = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    solution(m,n, b)