from ...lexer.token_types import TokenType

class BaseParser:
    """Base class for all parsers."""

    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def peek(self):
        """Peek at the current token."""
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return None

    def consume(self, expected_type, error_message):
        """Consume a token of the expected type or raise an error."""
        self.skip_whitespace()
        
        if self.current < len(self.tokens) and self.tokens[self.current].token_type == expected_type:
            token = self.tokens[self.current]
            self.advance()
            return token
        
        raise SyntaxError(error_message)

    def match(self, token_type):
        """Check if the current token matches the expected type and advance if it does."""
        if self.peek() is not None and self.peek().token_type == token_type:
            self.advance()
            return True
        return False

    def advance(self):
        """Move to the next token."""
        if self.current < len(self.tokens):
            self.current += 1

    def skip_whitespace(self):
        """Skip whitespace tokens."""
        while self.current < len(self.tokens) and self.tokens[self.current].token_type == TokenType.WHITESPACE:
            self.advance()

    def parse(self):
        """Parse method to be implemented by subclasses."""
        raise NotImplementedError("Parse method should be implemented by subclasses.")