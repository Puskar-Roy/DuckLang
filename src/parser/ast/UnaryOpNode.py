from .base_node import BaseNode
from .literal_node import LiteralNode
from ...lexer.token_types import TokenType

class UnaryOpNode(BaseNode):
    """AST node for unary operations."""

    def __init__(self, operator, operand):
        super().__init__("UnaryOp")
        self.operator = operator
        self.operand = operand
        self.interpreter = None  # Will be set by the interpreter

    def evaluate(self):
        """Evaluate the unary operation."""
        if self.interpreter:
            operand = self.interpreter.execute(self.operand)
        else:
            operand = self.operand.value if hasattr(self.operand, 'value') else self.operand

        if isinstance(operand, str):
            try:
                operand = float(operand) if '.' in operand else int(operand)
            except ValueError:
                pass

        if self.operator == TokenType.NOT:
            result = not bool(operand)
        elif self.operator == TokenType.MINUS:
            if not isinstance(operand, (int, float)):
                raise TypeError(f"Cannot apply unary minus to {type(operand)}")
            result = -operand
        else:
            raise RuntimeError(f"Unknown unary operator: {self.operator}")

        return LiteralNode(result)

    def __repr__(self):
        return f"UnaryOp({self.operator} {self.operand})"
