from .base_node import BaseNode

class FunctionDefNode(BaseNode):
    """AST node for function definitions."""

    def __init__(self, name, parameters, body):
        super().__init__("FunctionDef")
        self.name = name
        self.parameters = parameters
        self.body = body

    def __repr__(self):
        return f"FunctionDef({self.name}({self.parameters}) -> {self.body})"
