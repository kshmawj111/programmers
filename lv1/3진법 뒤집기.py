# https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3

def solution(n):
    answer = ''

    while n:
        answer += str(n % 3)
        n = int(n / 3)

    answer = answer[::-1]
    answer_num = 0

    for digit_idx in range(len(answer)):
        power = int(pow(3, int(digit_idx)))
        digit_num = int(answer[digit_idx])
        answer_num += digit_num * power

    print(answer_num)
    return answer_num

if __name__ == '__main__':
    solution(45)