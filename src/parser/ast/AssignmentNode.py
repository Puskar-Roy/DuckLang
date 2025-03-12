from .base_node import BaseNode

class AssignmentNode(BaseNode):
    """AST node for variable assignments."""

    def __init__(self, target, value):
        super().__init__("Assignment")
        self.target = target  # Can be a string (variable name) or ArrayAccessNode
        self.value = value

    def __repr__(self):
        return f"Assignment({self.target} = {self.value})"
