# https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3
import re
from itertools import permutations


def calculate(op1, op2, operator: str):
    if operator == '+':
        return op1 + op2

    elif operator == '-':
        return op1 - op2

    elif operator == '*':
        return op1 * op2


def convert_to_postfix(expression: list, precedence: dict):
    result = ''
    operator_stack = []
    for incoming in expression:
        # operator 만난 경우
        if incoming in precedence.keys():
            while len(operator_stack)>0 and precedence[incoming] <= precedence[operator_stack[-1]]:
                result += operator_stack.pop() + '.'

            operator_stack.append(incoming)

        # 숫자 만난 경우
        else:
            result += incoming + '.'

    while len(operator_stack) > 0:
        result += operator_stack.pop() + '.'

    return result


def evaluate_postfix(postfix_string:str):
    postfix = re.findall('[0-9]+|[\+\-\*]', postfix_string)
    precedence = ['+', '-', '*']
    result = []

    for incoming in postfix:
        if incoming in precedence:
            op2 = result.pop()
            op1 = result.pop()
            temp = calculate(op1, op2, incoming)
            result.append(temp)

        else:
            result.append(int(incoming))

    result = result[0]
    if result < 0:
        result *= -1

    return result


def solution(expression):
    results = []
    operators = ['+', '-', '*']
    exp = re.findall('[0-9]+|[\+\-\*]', expression)
    precedence = list(permutations(operators, 3))

    def map_to_dict(tuple):
        precedence_dict = {}
        for x in range(len(tuple)):
            precedence_dict[tuple[x]] = x

        return precedence_dict

    precedence = list(map(map_to_dict, precedence))

    for com in precedence:
        postfix = convert_to_postfix(exp, com)
        results.append(evaluate_postfix(postfix))

    return max(results)


if __name__ == '__main__':
    e = "100-200*300-500+20"
    # e = '5+2*7'
    print(solution(e))