# https://programmers.co.kr/learn/courses/30/lessons/12980?language=python3


def find_min_battery(N, dp: dict):
    if N % 2 == 0:
        dp[N] = find_min_battery(N / 2, dp)
        return dp[N]

    else:
        if N == 1:
            return 1

        dp[N] = find_min_battery(N-1, dp) + 1 # 이전에 사용한 것에서 점프 한 번 추가

        return dp[N]


def solution(n):
    dp = {1: 1} # key: dis, value: battery

    answer = find_min_battery(n, dp)
    print(answer)
    return answer


if __name__ == '__main__':
    solution(1)
    solution(5)
    solution(6)
    solution(5000)