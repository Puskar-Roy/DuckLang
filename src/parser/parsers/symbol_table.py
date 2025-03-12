class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent
        self.children = []

    def create_child_scope(self):
        """Create a new child scope."""
        child = SymbolTable(parent=self)
        self.children.append(child)
        return child

    def set(self, name, value):
        """Set a variable in the current scope."""
        self.symbols[name] = value

    def get(self, name):
        """Get a variable from the current scope or parent scopes."""
        value = self.symbols.get(name)
        if value is not None:
            return value
        if self.parent:
            return self.parent.get(name)
        return None

    def update(self, name, value):
        """Update a variable in its original scope."""
        if name in self.symbols:
            self.symbols[name] = value
            return True
        if self.parent:
            return self.parent.update(name, value)
        return False

    def exists(self, name):
        """Check if a variable exists in any accessible scope."""
        return name in self.symbols or (self.parent and self.parent.exists(name))

    def get_scope(self, name):
        """Get the scope where a variable is defined."""
        if name in self.symbols:
            return self
        if self.parent:
            return self.parent.get_scope(name)
        return None

    def dump(self, indent=0):
        """Print the symbol table contents with scope information."""
        print("\n📄 [Symbol Table Dump]")
        self._dump_recursive(indent)

    def _dump_recursive(self, indent=0):
        """Helper method for recursive symbol table dumping."""
        indent_str = "  " * indent
        print(f"{indent_str}🔷 Scope Level {indent}:")
        for var, value in self.symbols.items():
            print(f"{indent_str}  🔑 {var} = {value}")
        for child in self.children:
            child._dump_recursive(indent + 1)

    def __repr__(self):
        scope_info = "global" if not self.parent else "local"
        return f"{scope_info} SymbolTable{self.symbols}"
