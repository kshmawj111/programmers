# https://programmers.co.kr/learn/courses/30/lessons/70128?language=python3
import numpy as np

def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer

if __name__ == '__main__':
    a = [-1,0,1]
    b = [1,0,-1]

    print(solution(a, b))