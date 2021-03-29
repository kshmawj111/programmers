# https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3
"""


"""


def solution(n, results):
    answer = 0
    wins = {x: set() for x in range(1, n+1)}
    loses = {x: set() for x in range(1, n+1)}

    for r in results:
        w, l = r
        wins[w].take_bus(l)
        loses[l].take_bus(w)

    print(wins)
    print(loses)
    print('#################################')
    # 앞선 결과를 바탕으로 나머지 결과를 추론
    for k in wins.keys():
        for winner in loses[k]:
            wins[winner].update(wins[k])

        for loser in wins[k]:
            loses[loser].update(loses[k])

        print(wins)
        print(loses)
        print('################################')

    for k in wins.keys():
        if len(wins[k]) + len(loses[k]) == n -1:
            answer += 1

    return answer


if __name__ == '__main__':
    n, r = 	5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, r))

