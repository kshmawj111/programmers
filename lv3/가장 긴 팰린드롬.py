# https://programmers.co.kr/learn/courses/30/lessons/12904?language=python3
"""
    s = abcdcba
    -> 2,3,4 -> cdc -> 팰린드롬이면
        -> 1, 5 같을 경우엔 1 ~ 5역시 팰린드롬



"""


def solution(s):
    answer = 1
    palin_table = [[0 for _ in range(len(s))] for _ in range(len(s))] # palin_talbe[i][j] -> i에서 j까지는 palin인지 기록
    length = 3

    for i in range(len(s)):
        palin_table[i][i] = 1

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            palin_table[i][i+1] = 1

    while length < len(s) + 1:
        for x in range(len(s)-length+1): # 문자열에서 검색하고자 하는 substring의 길이
            y = x + length - 1

            if s[x] == s[y] and palin_table[x+1][y-1] == 1: # 문자가 같으면서 substring 안에 팰린드롬이 있다면
                palin_table[x][y] = 1

                if answer < length:
                    answer = length
                    break

        length += 1

    return answer


if __name__ == '__main__':
    s = "abcdcba"
    print(solution(s))