from .base_node import BaseNode

class ArrayNode(BaseNode):
    def __init__(self, elements):
        super().__init__("Array")
        self.elements = elements

    def __str__(self):
        return f"Array[{', '.join(str(e) for e in self.elements)}]"

class ArrayAccessNode(BaseNode):
    def __init__(self, array, index):
        super().__init__("ArrayAccess")
        self.array = array
        self.index = index

    def __str__(self):
        return f"{self.array}[{self.index}]" 