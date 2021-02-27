# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3


def solution(citations: list):
    counts = {} # k: 논문 수, v: 피인용 횟수
    citations.sort(reverse=True)
    answer = 0

    for num_doc, cit in zip(range(1, len(citations) + 1), citations):
        counts[num_doc] = cit

    for num_doc, num_cits in counts.items():
        if num_doc <= num_cits:
            answer = num_doc

        else:
            return answer

    return len(citations)


if __name__ == '__main__':
    inputs = [[22,33], [3,0,6,1,5]]
    for input in inputs:
        print(solution(input))