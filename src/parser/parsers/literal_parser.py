from ..ast import LiteralNode
from ...lexer.token_types import TokenType

class LiteralParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        start_pos = self.current
        
        # Skip any whitespace
        while self.current < len(self.tokens) and self.tokens[self.current].token_type == TokenType.WHITESPACE:
            self.current += 1
            
        # Check if there are tokens left
        if self.is_at_end():
            return None, 0
            
        # Check for literal types
        if self.check(TokenType.INTEGER, TokenType.FLOAT, TokenType.STRING):
            token = self.current_token()
            self.advance()
            # Calculate tokens consumed (including any whitespace we skipped)
            consumed = self.current - start_pos
            return LiteralNode(token.value), consumed
        
        # No literal found
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