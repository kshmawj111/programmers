# https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3
"""
정확성  테스트
테스트 1 〉	통과 (0.67ms, 10.3MB)
테스트 2 〉	통과 (13.81ms, 10.8MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	통과 (0.63ms, 10.4MB)
테스트 10 〉	통과 (1.17ms, 10.4MB)
테스트 11 〉	통과 (0.68ms, 10.4MB)
테스트 12 〉	통과 (0.75ms, 10.3MB)
테스트 13 〉	통과 (0.69ms, 10.4MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	통과 (125.90ms, 16.5MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실행 중단
테스트 7 〉	실행 중단
테스트 8 〉	실행 중단

"""


def solution(s):
    stack = []

    for c in s:
        stack.append(c)

        if len(stack) >= 2:
            if stack[len(stack)-1] == stack[len(stack)-2]:
                stack.pop()
                stack.pop()

    if stack:
        return 0

    else:
        return 1




if __name__ == '__main__':
    s = 'baabaa'
    print(solution(s))
