import re

class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

def create_rule(rule_string):
    # Define regex patterns for operands and operators
    operand_pattern = re.compile(r'(\w+) (>|<|>=|<=|=) (\d+)')
    operator_pattern = re.compile(r'(AND|OR)')

    tokens = []
    position = 0
    while position < len(rule_string):
        match = operand_pattern.match(rule_string[position:])
        if match:
            tokens.append(match.group())
            position += match.end()
        else:
            match = operator_pattern.match(rule_string[position:])
            if match:
                tokens.append(match.group())
                position += match.end()
            else:
                position += 1  # Move to the next character

    # Handle AST construction
    output = []
    operators = []

    for token in tokens:
        if token in {'AND', 'OR'}:
            while (operators and operators[-1] in {'AND', 'OR'} and
                   operators[-1] == 'AND' and token == 'OR'):
                output.append(operators.pop())
            operators.append(token)
        else:
            key, operator, value = token.split()
            output.append(Node("operand", f"{key} {operator} {value}"))

    while operators:
        output.append(operators.pop())

    # Construct AST from output and operators
    stack = []
    for item in output:
        if isinstance(item, Node):
            stack.append(item)
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(Node("operator", item, left, right))

    return stack[0] if stack else None
