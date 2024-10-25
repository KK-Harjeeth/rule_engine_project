import re
from .ast_node import Node

def create_rule(rule_string):
    # Tokenize the rule_string based on whitespace and special characters
    tokens = re.findall(r'\(|\)|\w+|[><=!]+|AND|OR', rule_string)
    
    # Define precedence for operators
    operators = {'>': 2, '<': 2, '=': 2, '!=': 2, 'AND': 1, 'OR': 1}
    stack = []
    operator_stack = []

    def apply_operator():
        op = operator_stack.pop()
        right = stack.pop()
        left = stack.pop()
        # If applying an operator between two operands, combine them correctly
        if op in {'>', '<', '=', '!='}:
            condition = f"{left.value} {op} {right.value}"
            stack.append(Node("operand", value=condition))
        else:
            # Create an operator node (AND, OR)
            stack.append(Node("operator", value=op, left=left, right=right))

    for token in tokens:
        if token not in operators:
            # Create an operand node for a simple value like an attribute or constant
            stack.append(Node("operand", value=token))
        else:
            # Handle precedence: Apply any operators with greater or equal precedence
            while (operator_stack and operator_stack[-1] in operators
                   and operators[token] <= operators[operator_stack[-1]]):
                apply_operator()
            operator_stack.append(token)

    # Apply remaining operators
    while operator_stack:
        apply_operator()

    return stack[-1]
