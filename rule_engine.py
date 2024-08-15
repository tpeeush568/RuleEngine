from ast_parser import create_rule
from rule_evaluator import evaluate_rule

# Sample usage
rule_string = "age > 30 AND salary > 50000"
data = {"age": 35, "salary": 60000}

rule_ast = create_rule(rule_string)
result = evaluate_rule(rule_ast, data)
print(f"Evaluation Result: {result}")
