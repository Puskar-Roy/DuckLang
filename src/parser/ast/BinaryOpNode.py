from .base_node import BaseNode
from .variable_node import VariableNode
from .literal_node import LiteralNode
from .array_node import ArrayNode, ArrayAccessNode
from ...lexer.token_types import TokenType

class BinaryOpNode(BaseNode):
    """AST node for binary operations."""

    def __init__(self, left, operator, right, symbol_table=None):
        super().__init__("BinaryOp")
        self.left = self.resolve(left, symbol_table)
        self.operator = operator
        self.right = self.resolve(right, symbol_table)
        self.interpreter = None  # Will be set by the interpreter

    def resolve(self, node, symbol_table):
        if isinstance(node, VariableNode) and symbol_table:
            return symbol_table.get(node.name, node)  # Lookup value if exists
        return node

    def get_numeric_value(self, node):
        """Get the numeric value from a node, handling both direct values and array operations."""
        if self.interpreter:
            # If we have an interpreter, use it to evaluate the node
            value = self.interpreter.execute(node)
        else:
            # Fallback to direct value extraction
            value = node.value if isinstance(node, LiteralNode) else None

        if isinstance(value, (int, float, bool)):
            return value
        elif isinstance(value, list):
            return value
        elif isinstance(value, str):
            try:
                return float(value) if '.' in value else int(value)
            except ValueError:
                return value
        return None

    def evaluate(self):
        """Evaluate the binary operation."""
        left_value = self.get_numeric_value(self.left)
        right_value = self.get_numeric_value(self.right)

        if left_value is None or right_value is None:
            return None

        # Handle array operations
        if isinstance(left_value, list):
            if self.operator == TokenType.PLUS:
                # Array concatenation
                if isinstance(right_value, list):
                    result = left_value + right_value
                else:
                    result = left_value + [right_value]
                return LiteralNode(result)
            elif self.operator == TokenType.MULTIPLY and isinstance(right_value, (int, float)):
                # Array repetition
                result = left_value * int(right_value)
                return LiteralNode(result)
            elif self.operator == TokenType.IN:
                # Array membership test
                return LiteralNode(right_value in left_value)
            else:
                raise TypeError(f"Unsupported array operation: {self.operator}")

        # Convert string operands to numbers if possible
        if isinstance(left_value, str):
            try:
                left_value = float(left_value) if '.' in left_value else int(left_value)
            except ValueError:
                pass

        if isinstance(right_value, str):
            try:
                right_value = float(right_value) if '.' in right_value else int(right_value)
            except ValueError:
                pass

        # Handle numeric operations
        if self.operator == TokenType.PLUS:
            result = left_value + right_value
        elif self.operator == TokenType.MINUS:
            result = left_value - right_value
        elif self.operator == TokenType.MULTIPLY:
            result = left_value * right_value
        elif self.operator == TokenType.DIVIDE:
            if right_value == 0:
                raise ZeroDivisionError("Division by zero")
            result = left_value / right_value
        elif self.operator == TokenType.MODULO:
            if right_value == 0:
                raise ZeroDivisionError("Modulo by zero")
            result = left_value % right_value
        # Comparison operators
        elif self.operator == TokenType.EQUALS:
            result = left_value == right_value
        elif self.operator == TokenType.NOT_EQUALS:
            result = left_value != right_value
        elif self.operator == TokenType.LESS_THAN:
            result = left_value < right_value
        elif self.operator == TokenType.LESS_EQUAL:
            result = left_value <= right_value
        elif self.operator == TokenType.GREATER_THAN:
            result = left_value > right_value
        elif self.operator == TokenType.GREATER_EQUAL:
            result = left_value >= right_value
        # Logical operators
        elif self.operator == TokenType.AND:
            result = bool(left_value) and bool(right_value)
        elif self.operator == TokenType.OR:
            result = bool(left_value) or bool(right_value)
        else:
            raise ValueError(f"Unsupported operator: {self.operator}")

        return LiteralNode(result)

    def __repr__(self):
        return f"BinaryOp({self.left} {self.operator} {self.right})"
