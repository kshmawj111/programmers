# https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3


def parse_string(s):
    result = []
    c_i = 0

    while c_i < len(s)-1:
        temp = []
        c_i += 1

        if s[c_i] == '{': # start parsing numbers
            c_i += 1
            num = ''

            while s[c_i] != '}':
                if s[c_i] == ',':
                    temp.append(int(num))
                    num = ''

                else:
                    num += s[c_i]

                c_i += 1

            temp.append(int(num))
            result.append(temp)

    print(result)
    return result


def solution(s):
    answer = []
    s_list = parse_string(s)
    s_list.sort(key=lambda x: len(x))

    for x in s_list:
        for e in x:
            if e not in answer:
                answer.append(e)

    print(answer)
    return answer


def solution_s(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter

if __name__ == '__main__':
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    solution_s(s)

    s= "{{20,111},{111}}"
    solution_s(s)

