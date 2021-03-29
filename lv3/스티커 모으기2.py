# https://programmers.co.kr/learn/courses/30/lessons/12971?language=python3


def solution(sticker):
    dp0 = [0 for _ in sticker]
    dp1 = [0 for _ in sticker]

    dp0[0] = dp0[1] = sticker[0]
    dp1[1] = sticker[1]

    for i in range(2, len(sticker)):
        if i < len(sticker) - 1:
            dp0[i] = max(dp0[i-2]+sticker[i], dp0[i-1])

        dp1[i] = max(dp1[i-2]+sticker[i], dp1[i-1])

    print(dp0)
    print(dp1)
    answer = max(dp0[-2], dp1[-1])
    return answer

if __name__ == '__main__':
    s = [14, 6, 5, 11, 3, 9, 2, 10]
    print(solution(s))

    s = 	[1, 3, 2, 5, 4]
    print(solution(s))