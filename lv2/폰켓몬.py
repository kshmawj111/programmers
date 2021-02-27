# https://programmers.co.kr/learn/courses/30/lessons/1845?language=python3

def solution(nums):
    unique = set(nums)
    num_of_choices = len(nums)//2

    if len(unique) >= num_of_choices:
        answer = num_of_choices

    else:
        answer = len(unique)

    return answer


if __name__ == '__main__':
    n = [3,1,2,3]
    solution(n)