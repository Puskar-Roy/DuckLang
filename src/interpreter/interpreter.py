from ..lexer.token_types import TokenType
from ..utils.debug import debug, DebugLevel
from ..parser.ast import (
    AssignmentNode,
    BinaryOpNode,
    UnaryOpNode,
    LiteralNode,
    VariableNode,
    ArrayNode,
    ArrayAccessNode,
    PrintNode,
    IfNode,
    WhileNode,
    BlockNode,
    FunctionDefNode,
    FunctionCallNode,
    ReturnNode,
    BreakNode,
    ContinueNode,
    ForNode
)
import sys
sys.setrecursionlimit(10000)  # Increase recursion limit

class BreakException(Exception):
    """Exception raised when a break statement is encountered."""
    pass

class ContinueException(Exception):
    """Exception raised when a continue statement is encountered."""
    pass

class Interpreter:
    def __init__(self, debug_mode=False):
        self.symbol_table = {}
        self.component_name = "Interpreter"
        self.debug_mode = False  # Always set to False
        self.call_stack = []  # Stack for managing function calls
        debug.level = DebugLevel.OFF  # Always set to OFF

    def interpret(self, node):
        """Interpret an AST node and return the result."""
        if node is None:
            return None
            
        if isinstance(node, BlockNode):
            result = None
            for statement in node.statements:
                result = self.interpret(statement)
            return result
            
        elif isinstance(node, AssignmentNode):
            if isinstance(node.target, str):
                # Simple variable assignment
                value = self.interpret(node.value)
                self.symbol_table[node.target] = value
                return value
            elif isinstance(node.target, ArrayAccessNode):
                # Array element assignment
                array = self.interpret(node.target.array)
                index = self.interpret(node.target.index)
                value = self.interpret(node.value)
                
                if not isinstance(array, list):
                    raise TypeError(f"Cannot index into non-array: {array}")
                    
                try:
                    idx = int(index) if isinstance(index, str) else index
                except (ValueError, TypeError):
                    raise TypeError(f"Array index must be an integer, got {type(index)}")
                    
                if not (0 <= idx < len(array)):
                    raise IndexError(f"Array index {idx} out of bounds")
                    
                array[idx] = value
                return value
            else:
                raise TypeError(f"Invalid assignment target: {node.target}")
                
        elif isinstance(node, BinaryOpNode):
            left = self.interpret(node.left)
            right = self.interpret(node.right)
            
            # Convert string operands to numbers if possible for arithmetic operations
            if node.operator in {TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY, TokenType.DIVIDE}:
                try:
                    if isinstance(left, str):
                        left = int(left)
                    if isinstance(right, str):
                        right = int(right)
                except ValueError:
                    pass  # Keep as strings if conversion fails
                    
            if node.operator == TokenType.PLUS:
                result = left + right
            elif node.operator == TokenType.MINUS:
                result = left - right
            elif node.operator == TokenType.MULTIPLY:
                result = left * right
            elif node.operator == TokenType.DIVIDE:
                result = left / right
            elif node.operator == TokenType.EQUALS:
                result = left == right
            elif node.operator == TokenType.NOT_EQUALS:
                result = left != right
            elif node.operator == TokenType.LESS_THAN:
                result = left < right
            elif node.operator == TokenType.GREATER_THAN:
                result = left > right
            elif node.operator == TokenType.LESS_EQUAL:
                result = left <= right
            elif node.operator == TokenType.GREATER_EQUAL:
                result = left >= right
            elif node.operator == TokenType.AND:
                result = left and right
            elif node.operator == TokenType.OR:
                result = left or right
            else:
                raise ValueError(f"Unknown operator: {node.operator}")
                
            return result
            
        elif isinstance(node, UnaryOpNode):
            operand = self.interpret(node.operand)
            
            if node.operator == TokenType.MINUS:
                try:
                    if isinstance(operand, str):
                        operand = int(operand)
                except ValueError:
                    pass
                result = -operand
            elif node.operator == TokenType.NOT:
                result = not operand
            else:
                raise ValueError(f"Unknown operator: {node.operator}")
                
            return result
            
        elif isinstance(node, PrintNode):
            value = self.interpret(node.expression)
            print(value)
            return value
            
        elif isinstance(node, VariableNode):
            if node.name not in self.symbol_table:
                raise NameError(f"Variable '{node.name}' is not defined")
            return self.symbol_table[node.name]
            
        elif isinstance(node, LiteralNode):
            return node.value
            
        elif isinstance(node, ArrayNode):
            elements = [self.interpret(element) for element in node.elements]
            return elements
            
        elif isinstance(node, ArrayAccessNode):
            array = self.interpret(node.array)
            index = self.interpret(node.index)
            
            if not isinstance(array, list):
                raise TypeError(f"Cannot index into non-array: {array}")
                
            try:
                idx = int(index) if isinstance(index, str) else index
            except (ValueError, TypeError):
                raise TypeError(f"Array index must be an integer, got {type(index)}")
                
            if not (0 <= idx < len(array)):
                raise IndexError(f"Array index {idx} out of bounds")
                
            return array[idx]
            
        elif isinstance(node, IfNode):
            condition = self.interpret(node.condition)
            if condition:
                return self.interpret(node.if_block)
            elif node.else_block:
                return self.interpret(node.else_block)
            return None
            
        elif isinstance(node, WhileNode):
            result = None
            while self.interpret(node.condition):
                try:
                    result = self.interpret(node.body)
                except BreakException:
                    break
                except ContinueException:
                    pass  # Skip to next iteration
                # Any cleanup code (like decrementing counters) should go here
            return result
            
        elif isinstance(node, ForNode):
            # Initialize
            self.interpret(node.initializer)
            
            # Loop
            result = None
            while self.interpret(node.condition):
                try:
                    result = self.interpret(node.body)
                except BreakException:
                    break
                except ContinueException:
                    pass  # Continue to increment step
                # Increment
                self.interpret(node.increment)
            return result
            
        elif isinstance(node, BreakNode):
            raise BreakException()
            
        elif isinstance(node, ContinueNode):
            raise ContinueException()
            
        elif isinstance(node, FunctionDefNode):
            self.symbol_table[node.name] = node
            return node
            
        elif isinstance(node, FunctionCallNode):
            # Get the function definition
            func = self.symbol_table.get(node.name)
            if not func or not isinstance(func, FunctionDefNode):
                raise NameError(f"Function '{node.name}' is not defined")
                
            if len(node.arguments) != len(func.parameters):
                raise TypeError(f"Function '{node.name}' takes {len(func.parameters)} arguments but {len(node.arguments)} were given")
                
            # Evaluate arguments before binding them to parameters
            arg_values = [self.interpret(arg) for arg in node.arguments]
            
            # Create a new symbol table for the function scope
            new_symbol_table = self.symbol_table.copy()
            
            # Bind arguments to parameters in the new scope
            for param, value in zip(func.parameters, arg_values):
                new_symbol_table[param] = value
                
            # Save the current symbol table
            old_symbol_table = self.symbol_table
            
            # Set the new symbol table
            self.symbol_table = new_symbol_table
            
            try:
                # Execute the function body
                result = self.interpret(func.body)
            finally:
                # Restore the original symbol table
                self.symbol_table = old_symbol_table
                
            return result
            
        elif isinstance(node, ReturnNode):
            if node.value:
                return self.interpret(node.value)
            return None
            
        else:
            raise TypeError(f"Unknown AST node type: {type(node)}") 