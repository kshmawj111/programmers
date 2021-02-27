# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    answers = []

    for command in commands:
        temp = array[command[0]-1:command[1]]
        answer = sorted(temp)
        answer = answer[command[2]-1]
        answers.append(answer)

    return answers

if __name__ == '__main__':
    solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])