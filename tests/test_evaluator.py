
from rule_engine.evaluator import evaluate_rule
from rule_engine.parser import create_rule

def test_evaluate_rule():
    rule_string = "age > 30 AND department = Sales"
    ast = create_rule(rule_string)
    data = {"age": 35, "department": "Sales"}
    result = evaluate_rule(ast, data)
    assert result is True  # Expected to be True based on data
