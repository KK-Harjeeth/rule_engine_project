
from rule_engine.parser import create_rule

def test_create_rule():
    rule_string = "age > 30 AND department = Sales"
    ast = create_rule(rule_string)
    assert ast is not None  # Add more checks for AST structure
