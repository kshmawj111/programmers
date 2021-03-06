# https://programmers.co.kr/learn/courses/30/lessons/12900?language=python3


def solution(n):
    dp = [1, 2]
    for i in range(2, n):
        dp.append((dp[i - 1] + dp[i - 2]) % 1000000007)
    answer = dp[n - 1]
    return answer


if __name__ == '__main__':
    n = 4
    print(solution(n))