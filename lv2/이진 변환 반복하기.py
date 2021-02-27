# https://programmers.co.kr/learn/courses/30/lessons/70129?language=python3


def convert(s):
    zero_out_string = ''

    for x in s:
        if x != '0':
            zero_out_string += x

    num_of_zero_deleted = len(s) - len(zero_out_string)
    return num_of_zero_deleted, bin(len(zero_out_string))[2:]


def solution(s):
    num_iter = 0
    z_count = 0

    while s != '1':
        z, s = convert(s)
        z_count += z
        num_iter += 1

    return [num_iter, z_count]


if __name__ == '__main__':
    s = "01110"
    solution(s)
