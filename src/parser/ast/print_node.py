from .base_node import BaseNode

class PrintNode(BaseNode):
    """AST node for print statements."""

    def __init__(self, expression):
        super().__init__("Print")
        self.expression = expression

    def __repr__(self):
        return f"Print({self.expression})"
