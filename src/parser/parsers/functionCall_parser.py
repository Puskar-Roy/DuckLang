from ..ast import FunctionCallNode
from ...lexer.token_types import TokenType
from .literal_parser import LiteralParser

class FunctionCallParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        start_pos = self.current
        
        # Check if this looks like a function call
        if not (self.check(TokenType.IDENTIFIER) and 
                self.current + 1 < len(self.tokens) and 
                self.tokens[self.current + 1].token_type == TokenType.LEFT_PAREN):
            return None, 0
        
        # Get function name
        name_token = self.consume(TokenType.IDENTIFIER, "Expected function name.")
        self.consume(TokenType.LEFT_PAREN, "Expected '(' after function name.")
        
        # Parse arguments
        args = []
        while not self.check(TokenType.RIGHT_PAREN):
            # Skip whitespace before argument
            while self.check(TokenType.WHITESPACE):
                self.advance()
                
            # Parse argument (which could be an expression)
            arg_parser = LiteralParser(self.tokens[self.current:])
            arg, arg_consumed = arg_parser.parse()
            if not arg:
                raise SyntaxError("Expected function argument.")
            
            args.append(arg)
            self.current += arg_consumed
            
            # Skip whitespace after argument
            while self.check(TokenType.WHITESPACE):
                self.advance()
                
            # Check for comma
            if self.check(TokenType.COMMA):
                self.advance()
        
        self.consume(TokenType.RIGHT_PAREN, "Expected ')' after arguments.")
        
        # Calculate total tokens consumed
        total_consumed = self.current - start_pos
        
        return FunctionCallNode(name_token.value, args), total_consumed

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