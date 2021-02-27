# https://programmers.co.kr/learn/courses/30/lessons/12907?language=python3
"""
    1. 거스름돈을 만드는 경우 구하는 방법 생각하기 -> 한 가지 동전으로만 만드는 경우 + 차액을 만들어 내는 경우
    2. 거스름돈을 만드는 경우 간 연결고리 파악하기


"""


def solution(n, money):
    dp = [0 for x in range(n+1)]
    dp[0] = 1
    for m in money:
        for target_money in range(1, n+1):
            if target_money - m >= 0:
                dp[target_money] += dp[target_money-m]
        print(dp)

    return dp[n]

if __name__ == '__main__':
    n, m = 	5, [1, 2, 5]
    solution(n, m)