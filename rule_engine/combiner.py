from .ast_node import Node
from .parser import create_rule

def combine_rules(rules):
    combined_ast = None
    for rule in rules:
        rule_ast = create_rule(rule)
        if combined_ast is None:
            combined_ast = rule_ast
        else:
            combined_ast = Node("operator", value="AND", left=combined_ast, right=rule_ast)
    return combined_ast
