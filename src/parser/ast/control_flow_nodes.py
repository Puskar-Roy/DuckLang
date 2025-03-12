from .base_node import BaseNode

class BreakNode(BaseNode):
    def __init__(self):
        super().__init__("Break")

    def __str__(self):
        return "Break"

class ContinueNode(BaseNode):
    def __init__(self):
        super().__init__("Continue")

    def __str__(self):
        return "Continue"

class ForNode(BaseNode):
    def __init__(self, init, condition, update, body):
        super().__init__("For")
        self.init = init
        self.condition = condition
        self.update = update
        self.body = body

    def __str__(self):
        return f"For({self.init}; {self.condition}; {self.update}) {self.body}"

class WhileNode(BaseNode):
    def __init__(self, condition, body):
        super().__init__("While")
        self.condition = condition
        self.body = body

    def __str__(self):
        return f"While({self.condition}) {self.body}"

class IfNode(BaseNode):
    def __init__(self, condition, if_block, else_block=None):
        super().__init__("If")
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

    def __str__(self):
        result = f"If({self.condition}) {self.if_block}"
        if self.else_block:
            result += f" Else {self.else_block}"
        return result 