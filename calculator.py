import pytest
import re


def prefix_calc(prefix_input):
    if not prefix_input: return

    operators = set(['+', '-', '*', '/'])
    stack = []

    while prefix_input:
        curr = prefix_input.pop(0)
        if curr not in operators:
            stack.append(curr)
        else:
            left_num = stack.pop()
            right_num = stack.pop()
            res = eval(' '.join([left_num, curr, right_num]))
            stack.append(str(res))

    return stack[0]


def infix_calc(infix_input):
    if not infix_input: return

    stack = []
    while infix_input:
        curr = infix_input.pop()
        if curr != '(':
            stack.append(curr)
        else:
            left_num = stack.pop()
            operator = stack.pop()
            right_num = stack.pop()
            res = eval(' '.join([left_num, operator, right_num]))
            stack.append(str(res))

    return stack[0]


if __name__ == '__main__':
    input_str = ' + 1 * 2 3'
    input_str = '( 1 + ( 2 * 3 ) )'

    assert bool(re.search('[a-zA-Z]', input_str)) is False

    if ')' in input_str:  # infix notation
        input_arr = input_str.replace(')', '').split()
        print(infix_calc(input_arr))
    else:  # prefix notation
        input_arr = input_str.split()
        input_arr.reverse()
        print(prefix_calc(input_arr))
