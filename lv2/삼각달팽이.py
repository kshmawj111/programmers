# https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3


def fill_triangle(n, start_num):
    triangle_array = [[] for _ in range(n)]
    n = len(triangle_array)
    x = start_num

    if n != 1:
        end_num = x+3*(n-1)-1

    else:
        end_num = x+1

    while x < end_num:
        for i in range(n-1):
            triangle_array[i].append(x)
            x += 1

        while len(triangle_array[n-1]) != n:
            triangle_array[n-1].append(x)
            x += 1

        for i in range(n-2, 0, -1):
            triangle_array[i].append(x)
            x += 1

    return triangle_array


def concat_triangle(t1:list, t2:list, insert_depth: int):
    row_t2_idx = 0
    for row_t1 in range(len(t1)):
        if len(t1[row_t1]) != row_t1 +1:
            # t2꺼 하나씩 앞에서 뽑아서 뒤에다 붙여 넣기
            row_t2 = t2[row_t2_idx]
            while row_t2:
                popped = row_t2.pop(0)
                t1[row_t1].insert(-insert_depth, popped)

            row_t2_idx += 1

    return t1


def solution(n):
    base = fill_triangle(n, 1)

    inner_triangle = n - 3
    next_start = 3*n - 2
    insert_depth = 1
    while inner_triangle > 0:
        temp = fill_triangle(inner_triangle, next_start)

        if len(temp) >= 2:
            next_start = temp[1][-1] + 1

        else:
            next_start = temp[0][0]
        inner_triangle = inner_triangle - 3

        base = concat_triangle(base, temp, insert_depth)
        insert_depth += 1

    for row in base:
        print(row)

    return [n for sublist in base for n in sublist]

if __name__ == '__main__':
    solution(10)