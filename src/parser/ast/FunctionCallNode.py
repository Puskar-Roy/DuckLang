from .base_node import BaseNode

class FunctionCallNode(BaseNode):
    """AST node for function calls."""

    def __init__(self, name, arguments):
        super().__init__("FunctionCall")
        self.name = name
        self.arguments = arguments

    def __repr__(self):
        return f"FunctionCall({self.name}, {self.arguments})"
