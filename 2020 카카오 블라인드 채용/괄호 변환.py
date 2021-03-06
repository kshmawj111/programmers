# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3

"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.

"""


def is_valid_brackets(target_string:str):
    bracket_count = 0

    if target_string == '':
        return True

    elif target_string[0] == '(':
        for char in range(len(target_string)):
            if target_string[char] == '(':
                bracket_count += 1

            elif target_string[char] == ')':
                bracket_count -= 1

            if bracket_count == 0:
                temp = target_string[char+1:]
                result = is_valid_brackets(temp)
                return result

    else:
        return False


def divide_into_uv(string):
    l_bracket = 0
    r_bracket = 0

    for char in range(len(string)):
        if string[char] == '(':
            l_bracket += 1

        elif string[char] == ')':
            r_bracket += 1

        if l_bracket == r_bracket:
            u = string[:char+1]
            v = string[char+1:]
            return u, v


def reverse_bracket(string):
    string = [x for x in string]

    for c in range(len(string)):
        if string[c] == '(':
            string[c] = ')'

        else:
            string[c] = '('

    return ''.join(string)


def solution(p):
    if not p:
        return ''

    if not is_valid_brackets(p):
        u, v = divide_into_uv(p)

    else:
        return p

    if is_valid_brackets(u):
        u += solution(v)
        answer = u

    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        u = reverse_bracket(u)
        answer += u

    return answer


if __name__ == '__main__':
    p = ["()))((()"]

    for _p in p:
        print(solution(_p))