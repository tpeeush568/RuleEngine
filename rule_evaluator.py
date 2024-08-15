# rule_evaluator.py

def evaluate_rule(ast, data):
    if ast.type == "operand":
        key, operator, value = ast.value.split(maxsplit=2)
        key = key.strip()
        value = value.strip()
        data_value = data.get(key)

        if operator == ">":
            return data_value > float(value)
        elif operator == "<":
            return data_value < float(value)
        elif operator == "=":
            return data_value == value
        else:
            return False
    elif ast.type == "operator":
        if ast.value == "AND":
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == "OR":
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)
    return False
