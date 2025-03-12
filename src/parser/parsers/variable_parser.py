from ..ast import VariableNode
from ...lexer.token_types import TokenType

class VariableParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        
        from .expression_parser import ExpressionParser
        
        start_pos = self.current
        
        # Check for variable declaration keyword
        if self.check(TokenType.VARIABLE_DECLARE):
            # Consume 'var' keyword
            self.consume(TokenType.VARIABLE_DECLARE, "Expected 'var' keyword.")
            
            # Skip whitespace after 'var'
            while self.check(TokenType.WHITESPACE):
                self.advance()
            
            # Get variable name
            if not self.check(TokenType.IDENTIFIER):
                raise SyntaxError("Expected identifier after 'var'.")
            
            var_name = self.consume(TokenType.IDENTIFIER, "Expected identifier after 'var'.").value
            
            # Skip whitespace after identifier
            while self.check(TokenType.WHITESPACE):
                self.advance()
            
            # Check for initialization
            initial_value = None
            if self.check(TokenType.ASSIGN):
                self.advance()  # Consume '='
                
                # Skip whitespace after '='
                while self.check(TokenType.WHITESPACE):
                    self.advance()
                
                # Parse initial value
                expr_parser = ExpressionParser(self.tokens[self.current:])
                initial_value, expr_consumed = expr_parser.parse()
                
                if not initial_value:
                    raise SyntaxError("Expected expression after '='.")
                
                self.current += expr_consumed
            
            # Calculate total tokens consumed
            total_consumed = self.current - start_pos
            
            return VariableNode(var_name, initial_value), total_consumed
            
        # If not a variable declaration but an identifier
        elif self.check(TokenType.IDENTIFIER):
            var_name = self.consume(TokenType.IDENTIFIER, "Expected identifier.").value
            
            # Calculate tokens consumed
            total_consumed = self.current - start_pos
            
            return VariableNode(var_name, None), total_consumed
            
        return None, 0

    def consume(self, token_type, error_message):
        if self.check(token_type):
            token = self.current_token()
            self.advance()
            return token
        raise SyntaxError(error_message)

    def check(self, *token_types):
        if self.is_at_end():
            return False
        return self.current_token().token_type in token_types

    def advance(self):
        if not self.is_at_end():
            self.current += 1

    def current_token(self):
        return self.tokens[self.current]

    def is_at_end(self):
        return self.current >= len(self.tokens)