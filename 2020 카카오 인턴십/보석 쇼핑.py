# https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
"""
    왼쪽, 오른쪽 인덱스를 움직여서 구간을 좁혀감
    구간을 한 번 좁힌 후에는 해당 구간 안에 방금 제외된 값이 있는지 확인
    제외된 값이 없다면 좁힌거 복구
    제외된 값이 존재하면 keep

    제외 판별 알고리즘
    -> 해시 테이블로 전체 구간에 대한 보석의 출현 빈도를 기록
    구간을 좁혀가면서 pop하는 아이템의 빈도를 1씩 줄여나감.

    -> 이 방법은 [1,2,3,4,4,4,5, 1,2,3,4,5, 1,2,3,4,4,4,5] 같은 경우 가운데에 최선의 값이 있는 경우를 못 찾아냄

    따라서 조금 응용하여 sliding window 알고리즘과 비슷하게 구현

    이는 처음부터 끝까지 리스트를 탐색하되 모든 종류의 보석이 들어있는 구간을 만들면
    해당 구간을 후보로 두고 이후 계속 진행할 때 더 짧은 구간이 나온다면 해당 구간으로 교체하도록 함

"""


def solution(gems):
    answer = [0, len(gems)]
    left, right = 0, -1
    length = len(gems)
    num_unique_gems = len(set(gems))
    table = {}

    while left < length and right < length: # right 만으로 체크하지 않는 이유는, right가 묶인 채로 left가 줄어들면서 더 짧은 구간을 만들 수 있기 때문
        # 모든 보석이 들어있는 구간일 때
        if len(table) == num_unique_gems:
            # 교체
            if answer[1] - answer[0] > right - left:
                answer = [left+1, right+1]

            key = gems[left]
            # 이후 구간의 앞축을 풀어서 새로 움직이도록 한다.
            table[key] -= 1

            # 만약 하나 없앴는데 0이 되면, 즉 보석이 구간에서 사라지면
            # table 에서도 마찬가지로 없애주도록 함
            if table[key] <= 0:
                del table[key]

            left += 1

        # 모든 보석이 구간에 존재하지 않아 뒷축 늘려가야할 때
        else:
            right += 1
            if right >= length:
                break
            key = gems[right]

            if key not in table.keys():
                table[key] = 1

            else:
                table[key] += 1

    return answer



if __name__ == '__main__':
    gems = ["A", "A", "B"]
    print(solution(gems))
