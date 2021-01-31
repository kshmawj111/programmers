# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

import pandas as pd
import numpy as np

def solution(answers):
    result = {1: 0, 2: 0, 3: 0}
    answer_list = []

    first = np.array([x for x in range(1, 6)])
    second = np.array([2, 1, 2, 3, 2, 4, 2,5])
    third = np.array([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    first_length = len(first)
    second_length = len(second)
    third_length = len(third)

    for x in range(len(answers)):
        current_answer = answers[x]

        first_idx = x % first_length
        second_idx = x % second_length
        third_idx = x % third_length

        if first[first_idx] == current_answer:
            result[1] += 1

        if second[second_idx] == current_answer:
            result[2] += 1

        if third[third_idx] == current_answer:
            result[3] += 1

    for person, score in result.items():
        if score == max(result.values()):
            answer_list.append(person)

    return answer_list

if __name__ == '__main__':
    rsult = solution([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])
    print(rsult)