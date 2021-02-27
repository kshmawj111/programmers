# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3


def solution(numbers):
    sorted_list = list(sorted(map(lambda x: str(x), numbers), key=lambda x: x*3, reverse=True))

    if sorted_list.count('0') != len(numbers):
        return ''.join(sorted_list)

    else:
        return '0'



if __name__ == '__main__':
    n=[3, 30, 34, 5, 9]
    sorted(n)

    print('3' > '30')