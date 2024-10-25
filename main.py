from rule_engine.parser import create_rule
from rule_engine.combiner import combine_rules
from rule_engine.evaluator import evaluate_rule
from rule_engine.ast_node import Node  # Import the Node class

def create_rule_api(rule_string):
    return create_rule(rule_string)

def combine_rules_api(rule_strings):
    return combine_rules(rule_strings)

def evaluate_rule_api(ast, attributes):
    # Directly evaluate the AST node passed in as `ast`
    return evaluate_rule(ast, attributes)

if __name__ == "__main__":
    # Sample rules and data
    rule1 = "age > 30 AND department = Sales"
    rule2 = "age < 25 AND department = Marketing"

    # Create individual rules
    rule_ast1 = create_rule_api(rule1)
    rule_ast2 = create_rule_api(rule2)

    # Combine rules
    combined_rule = combine_rules_api([rule1, rule2])

    # Sample data to evaluate
    sample_data = {
        "age": 28,
        "department": "Marketing",
        "salary": 60000,
        "experience": 3
    }

    # Evaluate combined rule
    result = evaluate_rule_api(combined_rule, sample_data)
    print(f"Result of rule evaluation: {result}")
