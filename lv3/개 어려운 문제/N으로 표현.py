# https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3
"""
    N으로 만들 수 있는 수의 집합을 유지하며 number가 해당 집합에 있는지 확인하는 방법이 더 해결하기
    쉬워보임.

    number를 N에 맞추는 과정은 더 복잡함

테스트 1 〉	통과 (1.01ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (8.56ms, 10.5MB)
테스트 5 〉	실패 (5.55ms, 10.6MB)
테스트 6 〉	실패 (5.46ms, 10.6MB)
테스트 7 〉	실패 (2.30ms, 10.4MB)
테스트 8 〉	실패 (6.48ms, 10.5MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)

"""


def solution(N, number):
    answer = -1
    memory = []
    # 최솟값이 8보다 크면 -1 반환하므로 최대 8까지만 찾아도 됨
    for N_used in range(1, 9):
        state = set()
        state.add(int(str(N)*N_used))
        # state[p] = [ NN..N, (x op y) for x in state[k] for y in state[p-k] while k < p]
        if N_used > 1:
            for p in range(N_used-1):
                for x in memory[p]:
                    for y in memory[N_used-2-p]:
                        # for debug
                        """state.add(f'{x}+{y}')
                        state.add(f'{x}-{y}')
                        state.add(f'{x}/{y}')
                        state.add(f'{x}*{y}')"""
                        state.add(x+y)
                        state.add(x-y)
                        state.add(x*y)
                        if y > 0:
                            state.add(x // y)

        memory.append(state)
        print(state)
        if number in state:
            answer = N_used
            break

    return answer


if __name__ == '__main__':
    a = [(5, 12), (2, 11)]

    for x, y in a:
        print(solution(x, y))