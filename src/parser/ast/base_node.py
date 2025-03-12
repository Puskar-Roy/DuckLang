class BaseNode:
    """Base class for all AST nodes."""

    def __init__(self, node_type):
        self.node_type = node_type

    def __repr__(self):
        return f"{self.node_type}()"
