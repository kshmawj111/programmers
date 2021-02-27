# https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3


def parse_num(part_of_result: str):
    num = '0'
    symbol = ''
    option = None

    if part_of_result[:2] == '10':
        num += '10'
        part_of_result = part_of_result[2:]

    else:
        num += part_of_result[0]
        part_of_result = part_of_result[1:]

    symbol = part_of_result[0]
    part_of_result = part_of_result[1:]

    option = part_of_result
    part_of_result

    '''for i in range(len(part_of_result)):
        char = part_of_result[i]
        
        if '0' <= char <= '9':
            if int(num + char) <= 10:
                num += char

        elif char == 'S' or char == 'D' or char == 'T':
            symbol += char

        elif char == '#' or char == '*':
            option = char'''

    return int(num), symbol, option


def solution(dartResult):
    answer = 0
    score_array = []

    for x in range(3):
        base_score, square, option = parse_num(dartResult)

        if square[0] == 'D':
            base_score = int(pow(base_score, 2))

        elif square[0] == 'T':
            base_score = int(pow(base_score, 3))

        score_array.append(base_score)

        if option == '*':
            current_score = score_array[x]
            score_array[x] = current_score * 2

            # 이전
            if x >= 1:
                prev_score = score_array[x - 1]
                score_array[x - 1] = prev_score * 2

            dartResult = dartResult[3:]

        elif option == '#':
            score_array[x] = -1 * score_array[x]
            dartResult = dartResult[3:]

        else:
            dartResult = dartResult[2:]

    for score in score_array:
        answer += score

    print(answer)
    return answer


if __name__ == '__main__':
    a = '1S2D*3T'
    # solution(a)

    a = '1D2S#10S'
    solution(a)

    a = '1D2S0T'
    solution(a)

    a = '1D#2S*3S'
    solution(a)

    a = '1S*2T*3S'
    solution(a)

    a = '1T2D3D#'
    solution(a)

    a = '1D2S3T*'
    solution(a)
