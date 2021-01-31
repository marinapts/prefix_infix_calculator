import argparse
import re


def compute_calculation(input_str):
    """Computes prefix or infix calculation, depending on the notation of the input expression.
    Also checks that the given input doesn't contain any alphabetical characters.
    Args:
        input_str (str): The input expression in string format
    Returns:
        res (float): The result of the prefix or infix calculation
    """
    assert bool(re.search('[a-zA-Z]', input_str)) is False, 'Only digits and operators +-*/() are allowed.'

    if '(' in input_str or ')' in input_str:  # Infix notation
        res = infix_calc(input_str)
        print('Infix result: ', res)
    else:  # Prefix notation
        res = prefix_calc(input_str)
        print('Prefix result:', res)

    return res


def prefix_calc(prefix_str):
    """Calculates an expression in prefix notation. E.g. + * 1 2 3 should return 5
    Args:
        prefix_str (str): The input in prefix notation
    Returns:
        (float): The result of the prefix calculation
    """
    prefix_arr = prefix_str.split()
    prefix_arr.reverse()

    if not prefix_arr:
        return None

    operators = set(['+', '-', '*', '/'])
    stack = []

    while prefix_arr:
        curr = prefix_arr.pop(0)
        if curr not in operators:
            stack.append(curr)
        else:
            left_num = stack.pop()
            right_num = stack.pop()
            res = eval(' '.join([left_num, curr, right_num]))
            stack.append(str(res))

    return float(stack[0])


def infix_calc(infix_str):
    """Calculates an expression in infix notation. E.g.  ( ( 1 * 2 ) + 3 ) should return 5
    Args:
        infix_str (str): The input in infix notation
    Returns:
        (float): The result of the infix calculation
    """
    assert infix_str.count('(') == infix_str.count(')'), 'Expression not correct. Ensure all parentheses are closed.'
    infix_arr = infix_str.replace(')', '').split()

    if not infix_arr:
        return None

    stack = []
    while infix_arr:
        curr = infix_arr.pop()
        if curr != '(':
            stack.append(curr)
        else:
            left_num = stack.pop()
            operator = stack.pop()
            right_num = stack.pop()
            res = eval(' '.join([left_num, operator, right_num]))
            stack.append(str(res))

    return float(stack[0])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=False, help='Expression for prefix or infix calculation')
    args = parser.parse_args()
    input_str = args.input

    if input_str:  # Input expression was not passed through the command line
        compute_calculation(input_str)
    else:  # Allow for user interaction using the input prompt
        while True:
            input_str = input('Enter prefix or infix expression: ')
            if not input_str: break
            compute_calculation(input_str)

