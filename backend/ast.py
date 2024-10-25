class Node:
    def __init__(self, node_type, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = None
        self.right = None
        self.value = value  # e.g., age > 30, department = 'Sales'

    def evaluate(self, data):
        """Evaluates the AST against the provided data dictionary."""
        if self.type == "operand":
            # Evaluating a condition like age > 30
            # Change here to convert the third part of the value to an int if it's a number
            left_value = data[self.value[0]]  # This gets the field (e.g., age)
            operator = self.value[1]  # This gets the operator (e.g., >)
            right_value = int(self.value[2]) if self.value[2].isdigit() else self.value[2]  # Convert to int if it’s a number
            if operator == '>':
                return left_value > right_value
            elif operator == '<':
                return left_value < right_value
            elif operator == '=':
                return left_value == right_value
            elif operator == '!=':
                return left_value != right_value
            # Add other operators as necessary
        elif self.type == "operator":
            if self.value == "AND":
                return self.left.evaluate(data) and self.right.evaluate(data)
            elif self.value == "OR":
                return self.left.evaluate(data) or self.right.evaluate(data)
        return False

    def to_dict(self):
        """Converts the AST node to a dictionary representation."""
        return {
            "type": self.type,
            "value": self.value,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
        }
