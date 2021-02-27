# https://programmers.co.kr/learn/courses/30/lessons/17687?language=python3


def convert_digits(num, notation):
    result = []

    while num >= notation:
        r = num % notation
        num = num // notation
        result.append(r)

    result.append(num)

    for x in range(len(result)):
        if result[x] >= 10:
            result[x] = chr(result[x] + 55)

        else:
            result[x] = str(result[x])

    return list(reversed(result))


def solution(n, t, total_people, tube_order):
    answer = ''
    current_num = 0
    current_person = 0
    tube_order -= 1

    while len(answer) < t:
        current_notation = convert_digits(current_num, n)

        for c in current_notation:
            if current_person == tube_order:
                answer += c

            if len(answer) >= t:
                break
            current_person = (current_person + 1) % total_people

        current_num += 1

    return answer


if __name__ == '__main__':
    n,t,m,p = 	16, 16, 2, 1
    print(solution(n,t,m, p))