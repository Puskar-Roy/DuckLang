from .parsers.expression_parser import ExpressionParser
from .parsers.symbol_table import SymbolTable
from .ast import (
    AssignmentNode,
    BinaryOpNode,
    FunctionCallNode,
    IfNode,
    LiteralNode,
    PrintNode,
    ReturnNode,
    UnaryOpNode,
    VariableNode,
    WhileNode,
    BlockNode,
    ArrayNode,
    ArrayAccessNode,
    FunctionDefNode,
    BreakNode,
    ContinueNode,
    ForNode
)
from src.lexer.token_types import TokenType
from ..utils.debug import debug, DebugLevel

# Disable debugging
debug.level = DebugLevel.ERROR

class MainParser:
    DEBUG_MODE = False

    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.symbol_table = SymbolTable()
        self.component_name = "MainParser"

    def parse(self):
        """Parse the token stream and return an AST."""
        statements = []
        
        while not self.is_at_end():
            statement = self.parse_statement()
            if statement:
                statements.append(statement)
            else:
                self.synchronize()
                if not self.is_at_end():
                    self.advance()
        
        return BlockNode(statements)

    def parse_statement(self):
        """Parse a statement."""
        current = self.current_token()
        
        statement = None
        if current.token_type == TokenType.PRINT_COMMAND:
            statement = self.parse_print_statement()
        elif current.token_type == TokenType.LEFT_BRACE:
            statement = self.parse_block()
        elif current.token_type == TokenType.FUNCTION:
            statement = self.parse_function_definition()
        elif current.token_type == TokenType.RETURN:
            statement = self.parse_return()
        elif current.token_type == TokenType.IF:
            statement = self.parse_if()
        elif current.token_type == TokenType.WHILE:
            statement = self.parse_while()
        elif current.token_type == TokenType.FOR:
            statement = self.parse_for()
        elif current.token_type == TokenType.BREAK:
            statement = self.parse_break()
        elif current.token_type == TokenType.CONTINUE:
            statement = self.parse_continue()
        elif current.token_type == TokenType.VARIABLE_DECLARE:
            statement = self.parse_variable_declaration()
        else:
            statement = self.parse_expression_statement()
        
        # Consume any trailing semicolon
        if self.check(TokenType.SEMICOLON):
            self.consume(TokenType.SEMICOLON)
        
        # Skip any whitespace after the statement
        while self.check(TokenType.WHITESPACE, TokenType.NEWLINE):
            self.advance()
            
        return statement

    def parse_function_definition(self):
        """Parse a function definition."""
        self.consume(TokenType.FUNCTION)
        
        name_token = self.consume(TokenType.IDENTIFIER)
        name = name_token.value
        
        self.consume(TokenType.LEFT_PAREN)
        parameters = []
        
        if not self.check(TokenType.RIGHT_PAREN):
            while True:
                param_token = self.consume(TokenType.IDENTIFIER)
                parameters.append(param_token.value)
                if not self.match(TokenType.COMMA):
                    break
        
        self.consume(TokenType.RIGHT_PAREN)
        body = self.parse_block()
        
        return FunctionDefNode(name, parameters, body)

    def parse_block(self):
        """Parse a block of statements."""
        self.consume(TokenType.LEFT_BRACE)
        statements = []
        
        while not self.check(TokenType.RIGHT_BRACE) and not self.is_at_end():
            statement = self.parse_statement()
            if statement:
                statements.append(statement)
        
        self.consume(TokenType.RIGHT_BRACE)
        return BlockNode(statements)

    def parse_if(self):
        """Parse an if statement."""
        self.consume(TokenType.IF)
        
        condition = self.parse_expression()
        if_block = self.parse_block()
        else_block = None
        
        if self.match(TokenType.ELSE):
            else_block = self.parse_block()
        
        return IfNode(condition, if_block, else_block)

    def parse_while(self):
        """Parse a while statement."""
        self.consume(TokenType.WHILE)
        
        condition = self.parse_expression()
        body = self.parse_block()
        
        return WhileNode(condition, body)

    def parse_expression(self):
        """Parse an expression."""
        expr_parser = ExpressionParser(self.tokens[self.current:])
        expr, consumed = expr_parser.parse()
        self.current += consumed
        return expr

    def parse_expression_statement(self):
        """Parse an expression statement."""
        expr = self.parse_expression()
        if self.check(TokenType.SEMICOLON):
            self.consume(TokenType.SEMICOLON)
        return expr

    def parse_print_statement(self):
        """Parse a print statement."""
        self.consume(TokenType.PRINT_COMMAND)
        expression = self.parse_expression()
        return PrintNode(expression)

    def parse_return(self):
        """Parse a return statement."""
        self.consume(TokenType.RETURN)
        value = None
        if not self.check(TokenType.RIGHT_BRACE):
            value = self.parse_expression()
        return ReturnNode(value)

    def parse_break(self):
        """Parse a break statement."""
        self.consume(TokenType.BREAK)
        return BreakNode()

    def parse_continue(self):
        """Parse a continue statement."""
        self.consume(TokenType.CONTINUE)
        return ContinueNode()

    def parse_variable_declaration(self):
        """Parse a variable declaration."""
        self.consume(TokenType.VARIABLE_DECLARE)
        name_token = self.consume(TokenType.IDENTIFIER)
        name = name_token.value
        
        if not self.match(TokenType.ASSIGN):
            return None
            
        value = self.parse_expression()
        return AssignmentNode(name, value)

    def is_at_end(self):
        """Check if we've reached the end of the token stream."""
        return self.current >= len(self.tokens)

    def current_token(self):
        """Get the current token."""
        if self.is_at_end():
            return self.tokens[-1]
        return self.tokens[self.current]

    def previous(self):
        """Get the previous token."""
        return self.tokens[self.current - 1]

    def advance(self):
        """Advance to the next token."""
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def match(self, *types):
        """Match and consume a token if it matches any of the given types."""
        for t in types:
            if self.check(t):
                self.advance()
                return True
        return False

    def check(self, *types):
        """Check if the current token is of any of the given types."""
        if self.is_at_end():
            return False
        return self.current_token().token_type in types

    def consume(self, expected_type, error_message=None):
        """Consume a token of the expected type."""
        if error_message is None:
            error_message = f"Expected {expected_type}"
            
        if self.check(expected_type):
            return self.advance()
            
        raise SyntaxError(f"{error_message}, got {self.current_token()}")

    def synchronize(self):
        """Skip tokens until we find a statement boundary."""
        self.advance()

        while not self.is_at_end():
            if self.previous().token_type == TokenType.SEMICOLON:
                return

            if self.current_token().token_type in {
                TokenType.FUNCTION,
                TokenType.VARIABLE_DECLARE,
                TokenType.FOR,
                TokenType.IF,
                TokenType.WHILE,
                TokenType.PRINT_COMMAND,
                TokenType.RETURN,
            }:
                return

            self.advance()

    def resolve_expression(self, expr):
        """ Recursively resolve VariableNode and BinaryOpNode expressions """
        if isinstance(expr, VariableNode):
            value = self.symbol_table.get(expr.name)
            if value is not None:
                return value
            return expr  # If the variable is undefined, return the node itself

        elif isinstance(expr, BinaryOpNode):
            expr.left = self.resolve_expression(expr.left)
            expr.right = self.resolve_expression(expr.right)

            if isinstance(expr.left, LiteralNode) and isinstance(expr.right, LiteralNode):
                result = expr.evaluate()
                return result

        elif isinstance(expr, ArrayAccessNode):
            array = self.resolve_expression(expr.array)
            index = self.resolve_expression(expr.index)
            
            # Convert string index to integer if needed
            if isinstance(index, LiteralNode):
                try:
                    idx = int(str(index.value))  # Convert any numeric string to int
                except (ValueError, TypeError):
                    raise TypeError(f"Array index must be an integer, got {type(index.value)}")
            else:
                raise TypeError(f"Array index must be a literal value")

            if isinstance(array, (ArrayNode, LiteralNode)):
                if isinstance(array, ArrayNode):
                    if 0 <= idx < len(array.elements):
                        return array.elements[idx]
                    else:
                        raise IndexError(f"Array index {idx} out of bounds")
                elif isinstance(array.value, list):
                    if 0 <= idx < len(array.value):
                        return LiteralNode(array.value[idx])
                    else:
                        raise IndexError(f"Array index {idx} out of bounds")
            else:
                raise TypeError(f"Cannot index into non-array: {array}")

        elif isinstance(expr, ArrayNode):
            # Resolve each element in the array
            resolved_elements = []
            for element in expr.elements:
                resolved = self.resolve_expression(element)
                if isinstance(resolved, LiteralNode):
                    resolved_elements.append(resolved)
                else:
                    resolved_elements.append(LiteralNode(resolved))
            expr.elements = resolved_elements
            return expr

        return expr

    def evaluate_binary_operation(self, left, operator, right):
        """Evaluate a binary operation using the BinaryOpNode's evaluate method."""
        binary_op = BinaryOpNode(left, operator, right)
        return binary_op.evaluate()

    def consume_optional_separators(self):
        """Consume any optional statement separators (semicolons, whitespace, newlines)."""
        while self.check(TokenType.SEMICOLON, TokenType.WHITESPACE, TokenType.NEWLINE):
            self.advance()
