# https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3


def solution(triangle):
    dp = [[-1]*len(x) for x in triangle]
    dp[0][0] = triangle[0][0]
    answer = 0

    for row in range(1, len(triangle)):
        for i in range(len(triangle[row])):
            temp_sum = []
            node_val = 0

            if 0 < i < len(triangle[row])-1:
                temp_sum.append(dp[row-1][i-1]+triangle[row][i])
                temp_sum.append(dp[row-1][i]+triangle[row][i])
                node_val = max(temp_sum)

            elif i == 0:
                node_val = dp[row-1][i] + triangle[row][i]

            elif i == len(triangle[row])-1:
                node_val = dp[row-1][i-1] + triangle[row][i]

            if answer < node_val:
                answer = node_val

            dp[row][i] = node_val

    return answer


if __name__ == '__main__':
    t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(t))