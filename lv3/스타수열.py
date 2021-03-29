# https://programmers.co.kr/learn/courses/30/lessons/70130?language=python3
"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	실패 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.3MB)
테스트 11 〉	통과 (0.05ms, 10.2MB)
테스트 12 〉	통과 (0.05ms, 10.3MB)
테스트 13 〉	통과 (113.89ms, 23MB)
테스트 14 〉	실패 (195.67ms, 43.1MB)
테스트 15 〉	실패 (186.19ms, 35.9MB)
테스트 16 〉	통과 (210.84ms, 31.5MB)
테스트 17 〉	통과 (235.70ms, 67.1MB)
테스트 18 〉	통과 (67.38ms, 26.7MB)
테스트 19 〉	통과 (144.08ms, 43MB)
테스트 20 〉	통과 (353.11ms, 81.2MB)
테스트 21 〉	통과 (352.03ms, 81.1MB)
테스트 22 〉	통과 (363.48ms, 81MB)
테스트 23 〉	통과 (283.82ms, 73.2MB)
테스트 24 〉	통과 (335.42ms, 79.6MB)
테스트 25 〉	통과 (356.40ms, 81.2MB)
테스트 26 〉	통과 (360.41ms, 77.6MB)
테스트 27 〉	통과 (247.26ms, 67.4MB)
테스트 28 〉	실패 (0.02ms, 10.3MB)
"""


def solution(a):
    # 숫자 출현 빈도의 딕셔너리 작성
    occurrences = {}
    answer = 0

    for x in a:
        if x not in occurrences.keys():
            occurrences[x] = 1

        else: occurrences[x] += 1

    occurrences = dict(sorted(occurrences.items(), key=lambda x: x[1]))
    keys = list(occurrences.keys())
    found = False

    while keys:
        temp = []
        temp_num = 0
        key = keys.pop()

        if occurrences[key]*2 > answer:
            i = 0
            while i < len(a)-1:
                if a[i] == key or a[i+1] == key:
                    if a[i] != a[i+1]:
                        temp.append((a[i], a[i+1]))
                        temp_num += 2
                        found = True
                        i += 2

                    else: i += 1

                else:
                    i += 1

            if found and temp_num > answer:
                answer = temp_num


    return answer


if __name__ == '__main__':
    '''a = [0,3,3,0,7,2,0,2,2,0]
    print(solution(a))

    a = [0,3,2,3,0]
    print(solution(a))'''

    a = [4, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3]
    print(solution(a))