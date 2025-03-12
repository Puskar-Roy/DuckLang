from .base_node import BaseNode

class BlockNode(BaseNode):
    def __init__(self, statements):
        super().__init__("Block")
        self.statements = statements

    def __str__(self):
        statements_str = '\n  '.join(str(stmt) for stmt in self.statements)
        return f"Block[\n  {statements_str}\n]" 