from .base_node import BaseNode

class LiteralNode(BaseNode):
    """AST node representing literal values."""

    def __init__(self, value):
        super().__init__("Literal")
        self.value = value

    def __repr__(self):
        return f"Literal({self.value})"
