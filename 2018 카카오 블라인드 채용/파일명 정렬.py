# https://programmers.co.kr/learn/courses/30/lessons/17686?language=python3


def is_num(c):
    if '0' <= c <= '9':
        return True

    else:
        return False


def split_file_name(file_name: str):
    head = ''
    number = ''
    tail = ''

    i = -1
    while i < len(file_name):
        i += 1
        if is_num(file_name[i]):
            head = file_name[:i]
            break

    start_of_num = i
    while i < len(file_name) and i < start_of_num + 5:
        if not is_num(file_name[i]):
            break
        number += file_name[i]
        i += 1

    if i < len(file_name):
        tail = file_name[i:]

    return head, number, tail


def solution(files):
    temp = []

    for f in files:
        temp.append(split_file_name(f))

    temp.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return list(map(''.join, temp))


if __name__ == '__main__':
    f = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
    # print(solution(f))

    f= 	 ['img0000a12345', 'img1.png','img2','IMG02']
    print(solution(f))