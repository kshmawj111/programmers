# https://programmers.co.kr/learn/courses/30/lessons/12905?language=python3


def solution(board):
    w = len(board[0])
    h = len(board)
    for row in range(h-1):
        for col in range(w-1):
            minimum = min(board[row][col], board[row+1][col], board[row][col+1])

            if minimum > 0 and board[row+1][col+1] != 0:
                board[row+1][col+1] = minimum + 1

    flattened = [i for x in board for i in x]
    flattened.sort()
    return flattened[-1]*flattened[-1]


if __name__ == '__main__':
    b = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
    print(solution(b))

    """b= [[0,0,1,1],[1,1,1,1]]
    print(solution(b))

    b = [[0,1,1,1],[1,0,1,1],[0,1,0,1],[1,0,1,0]]
    print(solution(b))

    board =  [[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]
    print(solution(board))"""