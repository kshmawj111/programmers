# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    string_list = [x for x in s]
    result = {}
    unit = 0

    while unit < len(string_list):
        front = 0
        unit += 1
        back = front + unit

        compress_part = string_list[front:back]
        compress_result = ''
        compress_count = 1

        while front <= len(string_list) + 1:
            back += unit
            front += unit

            compared_part = string_list[front:back]

            if compress_part == compared_part:
                compress_count += 1

            else:
                if compress_count > 1:
                    compress_result += str(compress_count)

                compress_result += ''.join(compress_part)
                compress_part = compared_part
                compress_count = 1

        result[unit] = len(compress_result)

    print(result)
    answer = min(result.values())
    print(answer)
    return answer


if __name__ == '__main__':
    s = "abcabcabcabcdededededede"
    solution(s)