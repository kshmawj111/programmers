# https://programmers.co.kr/learn/courses/30/lessons/17684?language=python3


def initialize_dict():
    alphabets = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    dictionary = {}
    for i, alphabet in enumerate(alphabets):
        dictionary[alphabet] = i+1

    return dictionary


def solution(msg):
    answer = []

    d = initialize_dict()
    initial_v = len(d) + 1

    i = 0
    j = 1
    while i < len(msg):
        j = 1
        w = msg[i]
        c = ''

        # substring이 딕셔너리에 있다면 계속 글자를 늘려감
        while True:
            if i+j < len(msg):
                c = msg[i+j]

            else:
                break

            if w+c in d.keys():
                w = w+c
                j += 1

            else:
                break

        # 없는 글자가 되어 나오는 경우
        answer.append(d[w])

        if c != '':
            d[w+c] = initial_v

        initial_v += 1

        i += j

    print(answer)
    return answer


if __name__ == '__main__':
    t = 	"TOBEORNOTTOBEORTOBEORNOT"
    solution(t)