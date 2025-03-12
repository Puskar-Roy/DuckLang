from .base_parser import BaseParser
from ...lexer.token_types import TokenType
from ...utils.debug import debug, DebugLevel

class BaseExpressionParser(BaseParser):
    def __init__(self, tokens):
        super().__init__(tokens)
        self.component_name = self.__class__.__name__

    def debug(self, message: str, level: DebugLevel = DebugLevel.DEBUG):
        debug.log(level, self.component_name, message)

    def skip_whitespace(self):
        while self.check(TokenType.WHITESPACE):
            self.advance()
            debug.trace(self.component_name, "Skipped whitespace")

    def match(self, *types):
        self.skip_whitespace()
        for token_type in types:
            if self.check(token_type):
                self.advance()
                debug.trace(self.component_name, f"Matched token type: {token_type}")
                return True
        return False

    def check(self, *types):
        if self.is_at_end():
            return False
        current_token = self.peek()
        return any(current_token.token_type == t for t in types)

    def advance(self):
        if not self.is_at_end():
            self.current += 1
            debug.trace(self.component_name, f"Advanced to token: {self.peek()}")
        return self.previous()

    def current_token(self):
        if self.is_at_end():
            raise SyntaxError("Unexpected end of tokens")
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def is_at_end(self):
        return self.current >= len(self.tokens)

    def peek(self):
        if self.is_at_end():
            return None
        return self.tokens[self.current]

    def consume(self, token_type, error_message=None):
        if self.check(token_type):
            debug.debug(self.component_name, f"Consumed token: {self.peek()}")
            return self.advance()
        if error_message is None:
            error_message = f"Expected {token_type}"
        raise SyntaxError(error_message) 