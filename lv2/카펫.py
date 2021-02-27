# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3
from itertools import combinations


def get_divisor(n):
    n = int(n)
    divisors = []
    divisors_quotient = []
    answer = []

    if n > 3:
        for x in range(1, n//2):
            if n % x == 0:
                if x not in divisors and x not in divisors_quotient:
                    divisors.append(x)
                    divisors_quotient.append(int(n / x))

    else:
        divisors.append(1)
        divisors_quotient.append(n)

    for f, b in zip(divisors, divisors_quotient):
        answer.append((b, f))

    return answer


def validate_shape(factor, brown, yellow):
    w = factor[0]
    h = factor[1]

    inferred_yellow_block_max = (w-2, h-2)
    y_w = inferred_yellow_block_max[0]
    y_h = inferred_yellow_block_max[1]

    if y_w * y_h == yellow:
        return True


def solution(brown, yellow):
    '''

    노란색 블록의 크기 6이라고고 하자
    6 약수 집합들을 모두 구하면 (1, 6), (2, 3), (3, 2), (6, 1)이 된다.
    이때 각 순서쌍의 첫 원소를 사각형의 width, 두번째 원소를 height으로 생각하고 각 값을 _w, _h로 정의하자.

    그렇다면 전체 사각형의 요소 w = _w + 2, h = _h + 2가 된다.

    '''
    answer = []
    total_blocks = brown + yellow
    temp = get_divisor(total_blocks)

    # print(f'factors of {yellow}: {temp}')
    factors = []

    for item in temp:
        if item[1] >= 3:
            factors.append(item)

    # print(f'factors of {yellow}: {factors}')
    for factor in factors:
        found = validate_shape(factor, brown, yellow)

        if found:
            answer = factor
            break

    print(answer)
    return answer


if __name__ == '__main__':
    bl = [ 24, 20]
    yl = [24, 16]

    for b, y in zip(bl, yl):
        solution(brown=b, yellow=y)