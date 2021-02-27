# https://programmers.co.kr/learn/courses/30/lessons/12985?language=python3


def next_round_num(number):
    if number % 2 == 0:
        return int(number / 2)

    else:
        return int((number+1)/ 2)


def solution(n,a,b):
    if a > b:
        temp = a
        a = b
        b = temp

    num_rounds = 0

    while True:
        num_rounds += 1

        if b-a == 1 and a % 2 == 1:
            break

        a = next_round_num(a)
        b = next_round_num(b)

    answer = num_rounds
    print(answer)
    return answer


if __name__ == '__main__':
    solution(8,4,7)