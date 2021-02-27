# https://programmers.co.kr/learn/courses/30/lessons/68936?language=python3


def is_all_same(ary):
    reference = ary[0][0]
    for x in range(len(ary)):
        for y in range(len(ary[0])):
            if ary[x][y] != reference:
                return -1

    return reference


def divide_list(arr):
    if len(arr) > 1:
        divide_ver_idx = len(arr[0])//2
        divide_hor_idx = len(arr)//2

        upper = arr[:divide_hor_idx]
        lower = arr[divide_hor_idx:]
        sq1, sq2, sq3, sq4 = [],[],[],[]

        for v in range(divide_ver_idx):
            temp = []
            for x in upper:
                temp.append(x[v])

            sq1.append(temp)

        for v in range(divide_ver_idx,len(upper[0])):
            temp = []
            for x in upper:
                temp.append(x[v])

            sq2.append(temp)

        for v in range(divide_ver_idx):
            temp = []
            for x in lower:
                temp.append(x[v])

            sq3.append(temp)

        for v in range(divide_ver_idx, len(upper[0])):
            temp = []
            for x in lower:
                temp.append(x[v])

            sq4.append(temp)


        return sq1, sq2, sq3, sq4

    else:
        return 1


# target 넘버로 arr를 채움
def compress_list(target_num):
    return [target_num]


def flatten_arr(arr):
    result = []
    for x in arr:
        if isinstance(x, list):
            result = result + flatten_arr(x)

        else:
            result.append(x)

    return result


def solve(arr):
    answer = []
    all_same = is_all_same(arr)

    if all_same == -1:
        sq1, sq2, sq3, sq4 = divide_list(arr)
        answer.append(solve(sq1))
        answer.append(solve(sq2))
        answer.append(solve(sq3))
        answer.append(solve(sq4))

    else:
        # 통합하는 알고리즘 필요
        answer = compress_list(all_same)

    return answer


def solution(arr):
    answer = solve(arr)
    answer = flatten_arr(answer)
    return [answer.count(0), answer.count(1)]


if __name__ == '__main__':
    a = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
    print(solution(a))