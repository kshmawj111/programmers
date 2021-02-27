# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3


def solution(number: str, k):
    maximum = max(number[:k])
    max_idx = number.find(maximum)
    answer = [maximum]
    k -= max_idx
    number = number[max_idx:]

    for i in range(1, len(number)):
        last = answer[-1]
        incoming = number[i]

        while last < incoming and k > 0:
            if answer:
                answer.pop()
                k -= 1

                if answer:
                    last = answer[-1]

        answer.append(incoming)

        if k <= 0 and i < len(number):
            answer += number[i+1:]
            break

    if k > 0:
       for i in range(k):
           answer.remove(min(answer))

    temp = ''

    for n in answer:
        temp += n

    return temp

if __name__ == '__main__':
    inputs = [('99991', 3), ('99923', 2), ('111119', 3)]

    for n, k in inputs:
        print(solution(n, k))