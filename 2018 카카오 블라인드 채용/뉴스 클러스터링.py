# https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3


def cross(a: dict, b: dict):
    total_keys = set(list(a.keys())+list(b.keys()))
    result = {}

    for k in total_keys:
        if k in a.keys() and k in b.keys():
            result[k] = min(a[k], b[k])

    return result


def union(a: dict, b:dict):
    total_keys = set(list(a.keys()) + list(b.keys()))
    result = {}

    for k in total_keys:
        if k in a.keys() and k in b.keys():
            result[k] = max(a[k], b[k])

        elif k in a.keys():
            result[k] = a[k]

        elif k in b.keys():
            result[k] = b[k]

    return result


def only_alphabets(string):
    for c in string:
        if 'a' <= c <= 'z':
            pass

        else:
            return False

    return True


def convert_string(string: str):
    i = 0
    converted_result = {}

    while i+1 < len(string):
        sub = string[i:i+2]

        if only_alphabets(sub):
            if not sub in converted_result.keys():
                converted_result[sub] = 1

            else:
                converted_result[sub] += 1

        i += 1

    return converted_result


def solution(s1: str, s2: str):
    s1 = s1.lower()
    s2 = s2.lower()

    c1 = convert_string(s1)
    c2 = convert_string(s2)

    cross_set = cross(c1, c2)
    union_set = union(c1, c2)

    cross_val = sum(cross_set.values())
    union_val = sum(union_set.values())

    if union_val != 0:
        similarity = cross_val/union_val*65536

    else:
        similarity = 65536

    return int(similarity)


if __name__ == '__main__':
    s1, s2 = 	"E=M*C^2", "e=m*c^2"
    print(jacard_similarity(s1, s2))



