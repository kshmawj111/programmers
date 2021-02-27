# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
'''

 주어지는 배열의 값을 OR bit operation을 통해 값을 구하도록 한다.

'''
def solution(n, arr1, arr2):
    entire_map_num = []
    answer = []

    for x in range(n):
        entire_map_num.append(arr1[x] | arr2[x])

    for num in entire_map_num:
        binary_string = bin(num)[2:]
        binary_string = binary_string.zfill(n)
        binary_string = binary_string.replace('1', '#')
        binary_string = binary_string.replace('0', ' ')
        answer.append(binary_string)

    return answer

if __name__ == '__main__':
    n = 5
    a1 = [9, 20, 28, 18, 11]
    a2 = [30, 1, 21, 17, 28]
    # print(solution(n, a1, a2))

    n = 6
    a1 = [46, 33, 33 ,22, 31, 50]
    a2 = 	[27 ,56, 19, 14, 14, 10]
    print(solution(n, a1, a2))