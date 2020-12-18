from collections import deque
from io import StringIO
from shlex import shlex


def read_data(path="input.data"):
    with open(path) as fobj:
        return list(map(str.rstrip, fobj))


def parse(expression, operator_precendence):
    expression = deque(shlex(StringIO(expression)))
    operators = set(operator_precendence)
    output = []
    operator_stack = []
    while expression:
        token = expression.popleft()
        if token not in operators and token not in "()":
            output.append(token)
        elif token in operators:
            token_precendence = operator_precendence[token]
            while operator_stack:
                top = operator_stack[-1]
                if top == "(":
                    break
                if operator_precendence[top] < token_precendence:
                    break
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack:
                op = operator_stack.pop()
                if op == "(":
                    break
                output.append(op)
    while operator_stack:
        op = operator_stack.pop()
        if op in "()":
            raise ValueError("Mismatched parantheses.")
        output.append(op)

    return output


def evaluate(expression):
    expression = deque(expression)
    stack = []
    operators = set("+*")
    while expression:
        token = expression.popleft()
        if token not in operators:
            stack.append(int(token))
            continue
        right = stack.pop()
        left = stack.pop()
        if token == "+":
            stack.append(left + right)
        elif token == "*":
            stack.append(left * right)
    return stack.pop()


def solution_01(path="input.data"):
    return sum(
        evaluate(parse(expression, operator_precendence={"*": 0, "+": 0}))
        for expression in read_data(path)
    )


def solution_02(path="input.data"):
    return sum(
        evaluate(parse(expression, operator_precendence={"*": 0, "+": 1}))
        for expression in read_data(path)
    )


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
