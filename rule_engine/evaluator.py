from .ast_node import Node

def evaluate_rule(ast, data):
    if ast.type == "operand":
        # The operand value should be something like "age > 30"
        condition_parts = ast.value.split()  # Split based on whitespace
        if len(condition_parts) == 3:
            attribute, operator, value = condition_parts
            value = int(value) if value.isdigit() else value
            
            if operator == '>':
                return data.get(attribute, 0) > value
            elif operator == '<':
                return data.get(attribute, 0) < value
            elif operator == '=':
                return data.get(attribute) == value
            elif operator == '!=':
                return data.get(attribute) != value
        else:
            raise ValueError("Invalid operand condition format.")
    
    elif ast.type == "operator":
        # Operator nodes (AND, OR)
        left_value = evaluate_rule(ast.left, data)
        right_value = evaluate_rule(ast.right, data)
        if ast.value == 'AND':
            return left_value and right_value
        elif ast.value == 'OR':
            return left_value or right_value

    return False
