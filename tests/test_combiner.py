from rule_engine.combiner import combine_rules

def test_combine_rules():
    rule1 = "age > 30 AND department = Sales"
    rule2 = "age < 25 AND department = Marketing"
    combined_ast = combine_rules([rule1, rule2])
    assert combined_ast is not None  # Add more checks for combined AST structure
