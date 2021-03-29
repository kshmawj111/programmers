# https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3

# m: 열, n: 행
def solution(m, n, puddles):
    ROW = 1
    COL = 0

    dp = [0 for x in range(m)]
    dp[0] = 1

    puddles.sort(key=lambda x: x[ROW], reverse=True)
    puddle_columns = []
    row = 0
    p_row, p_col = 0,0
    print(dp)

    while row < n:
        # 웅덩이가 남아있고 현재 웅덩이가 비어있다면
        if puddles and not puddle_columns:
            puddle = puddles.pop()
            p_col = max(puddle[COL] - 1, 0)
            p_row = max(puddle[ROW] - 1, 0)
            puddle_columns.append(p_col)

            while puddles and p_row + 1 == puddles[-1][ROW]:
                puddle = puddles.pop()
                p_col = max(puddle[COL] - 1, 0)
                puddle_columns.append(p_col)

        if row == p_row:
            # 현재 찾는 행에 웅덩이가 있다면
            for x in puddle_columns:
                dp[x] = 0

            for col in range(1, m):
                if col not in puddle_columns:
                    dp[col] += dp[col-1]

            # 행의 웅덩이 리스트 비우기
            puddle_columns = []

        else:
            for col in range(1, m):
                dp[col] += dp[col-1]

        row += 1
        print(dp)
    answer = dp[-1] % 1000000007
    return answer


if __name__ == '__main__':
    m,n, puddles = 4, 3, [[0,1], [1,0]]
    print(solution(m,n,puddles))