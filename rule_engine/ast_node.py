class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # Type of node ('operator' or 'operand')
        self.value = value  # Value of the operand node
        self.left = left  # Left child (Node)
        self.right = right  # Right child (Node)

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value}, left={self.left}, right={self.right})"

