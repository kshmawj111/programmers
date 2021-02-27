# https://programmers.co.kr/learn/courses/30/lessons/12949?language=python3


def solution(arr1, arr2):
    answer = []

    for row in arr1:
        temp = []
        for col_idx in range(len(arr2[0])):
            col = [x[col_idx] for x in arr2]
            temp.append(sum([r * c for r, c in zip(row, col)]))

        answer.append(temp)

    return answer


if __name__ == '__main__':
    a1 = [[1, 4, 5], [3, 2, -1], [4, 1, 0]]
    a2 = [[1, 2], [3, 4], [5,6]]

    print(solution(a1, a2))