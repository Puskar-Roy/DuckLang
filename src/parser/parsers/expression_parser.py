from ...lexer.token_types import TokenType
from ..ast import (
    BinaryOpNode,
    UnaryOpNode,
    LiteralNode,
    VariableNode,
    ArrayNode,
    ArrayAccessNode,
    AssignmentNode,
    FunctionCallNode
)
from .base_expression_parser import BaseExpressionParser

class ExpressionParser(BaseExpressionParser):
    def __init__(self, tokens):
        super().__init__(tokens)
        self.component_name = "ExpressionParser"

    def parse(self):
        """Parse an expression and return the AST node and number of tokens consumed."""
        start_pos = self.current
        
        try:
            self.skip_whitespace()
            expr = self.parse_assignment()
            consumed = self.current - start_pos
            return (expr, consumed) if expr else (None, 0)
        except Exception:
            return None, 0

    def parse_assignment(self):
        """Parse an assignment expression."""
        self.skip_whitespace()
        left = self.parse_logical()
        
        if not left:
            return None
        
        self.skip_whitespace()
        if self.match(TokenType.ASSIGN):
            if isinstance(left, VariableNode):
                value = self.parse_assignment()
                if not value:
                    return None
                return AssignmentNode(left.name, value)
            elif isinstance(left, ArrayAccessNode):
                value = self.parse_assignment()
                if not value:
                    return None
                return AssignmentNode(left, value)
            else:
                return None
        
        return left

    def parse_logical(self):
        """Parse logical operators (and, or)."""
        self.skip_whitespace()
        expr = self.parse_equality()
        
        if not expr:
            return None
        
        while True:
            self.skip_whitespace()
            if not self.match(TokenType.AND, TokenType.OR):
                break
            operator = self.previous().token_type
            right = self.parse_equality()
            if not right:
                return None
            expr = BinaryOpNode(expr, operator, right)
        
        return expr

    def parse_equality(self):
        """Parse equality expressions (==, !=)."""
        self.skip_whitespace()
        expr = self.parse_comparison()
        
        if not expr:
            return None
        
        while True:
            self.skip_whitespace()
            if not self.match(TokenType.EQUALS, TokenType.NOT_EQUALS):
                break
            operator = self.previous().token_type
            right = self.parse_comparison()
            if not right:
                return None
            expr = BinaryOpNode(expr, operator, right)
        
        return expr

    def parse_comparison(self):
        """Parse comparison expressions (<, >, <=, >=)."""
        self.skip_whitespace()
        expr = self.parse_term()
        
        if not expr:
            return None
        
        while True:
            self.skip_whitespace()
            if not self.match(
                TokenType.LESS_THAN, TokenType.GREATER_THAN,
                TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL
            ):
                break
            operator = self.previous().token_type
            right = self.parse_term()
            if not right:
                return None
            expr = BinaryOpNode(expr, operator, right)
        
        return expr

    def parse_term(self):
        """Parse terms (addition and subtraction)."""
        self.skip_whitespace()
        expr = self.parse_factor()
        
        if not expr:
            return None
        
        while True:
            self.skip_whitespace()
            if not self.match(TokenType.PLUS, TokenType.MINUS):
                break
            operator = self.previous().token_type
            right = self.parse_factor()
            if not right:
                return None
            expr = BinaryOpNode(expr, operator, right)
        
        return expr

    def parse_factor(self):
        """Parse factors (multiplication and division)."""
        self.skip_whitespace()
        expr = self.parse_unary()
        
        if not expr:
            return None
        
        while True:
            self.skip_whitespace()
            if not self.match(TokenType.MULTIPLY, TokenType.DIVIDE):
                break
            operator = self.previous().token_type
            right = self.parse_unary()
            if not right:
                return None
            expr = BinaryOpNode(expr, operator, right)
        
        return expr

    def parse_unary(self):
        """Parse unary expressions (-, not)."""
        self.skip_whitespace()
        if self.match(TokenType.MINUS, TokenType.NOT):
            operator = self.previous().token_type
            right = self.parse_unary()
            if not right:
                return None
            expr = UnaryOpNode(operator, right)
            return expr
        
        return self.parse_call()

    def parse_call(self):
        """Parse function calls and array access."""
        self.skip_whitespace()
        expr = self.parse_primary()
        
        if not expr:
            return None
        
        while True:
            self.skip_whitespace()
            if self.match(TokenType.LEFT_PAREN):
                # Function call
                if not isinstance(expr, VariableNode):
                    return None
                
                arguments = []
                if not self.check(TokenType.RIGHT_PAREN):
                    while True:
                        arg = self.parse_assignment()
                        if not arg:
                            return None
                        arguments.append(arg)
                        if not self.match(TokenType.COMMA):
                            break
                
                if not self.match(TokenType.RIGHT_PAREN):
                    return None
                expr = FunctionCallNode(expr.name, arguments)
            elif self.match(TokenType.LEFT_BRACKET):
                # Array access
                index = self.parse_assignment()
                if not index:
                    return None
                if not self.match(TokenType.RIGHT_BRACKET):
                    return None
                expr = ArrayAccessNode(expr, index)
            else:
                break
        
        return expr

    def parse_primary(self):
        """Parse primary expressions (literals, variables, parentheses, arrays)."""
        self.skip_whitespace()
        
        if self.match(TokenType.INTEGER):
            value = int(self.previous().value)
            return LiteralNode(value)
            
        if self.match(TokenType.STRING):
            value = str(self.previous().value)
            return LiteralNode(value)
            
        if self.match(TokenType.BOOLEAN):
            value = self.previous().value
            return LiteralNode(value)
            
        if self.match(TokenType.IDENTIFIER):
            name = self.previous().value
            return VariableNode(name)
            
        if self.match(TokenType.LEFT_PAREN):
            expr = self.parse_assignment()
            if not expr:
                return None
            if not self.match(TokenType.RIGHT_PAREN):
                return None
            return expr
            
        if self.match(TokenType.LEFT_BRACKET):
            elements = []
            if not self.check(TokenType.RIGHT_BRACKET):
                while True:
                    element = self.parse_assignment()
                    if not element:
                        return None
                    elements.append(element)
                    if not self.match(TokenType.COMMA):
                        break
            
            if not self.match(TokenType.RIGHT_BRACKET):
                return None
            return ArrayNode(elements)
        
        return None

    def skip_whitespace(self):
        """Skip whitespace tokens."""
        while self.check(TokenType.WHITESPACE, TokenType.NEWLINE):
            self.advance()

    def consume(self, expected_type, error_message):
        """Consume a token of the expected type or raise an error."""
        self.skip_whitespace()
        if self.check(expected_type):
            return self.advance()
        raise SyntaxError(f"{error_message} at token {self.current_token()}")

    def match(self, *token_types):
        """Match current token against given types."""
        self.skip_whitespace()
        for token_type in token_types:
            if self.check(token_type):
                return self.advance() is not None
        return False

    def check(self, *token_types):
        """Check if current token is of given type."""
        if self.is_at_end():
            return False
        return self.current_token().token_type in token_types