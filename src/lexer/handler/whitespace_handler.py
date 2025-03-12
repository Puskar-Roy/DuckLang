from ..token_types import TokenType
from ..state import LexerState
from .base import TokenHandler

class WhiteSpaceHandler(TokenHandler):
    def __init__(self, store_whitespace=False):
        self.store_whitespace = store_whitespace

    def can_handle(self, state: LexerState) -> bool:
        return state.current_char() in {' ', '\t', '\n', '\r'}
    
    def handle(self, state: LexerState, start_pos):
        if self.store_whitespace:
            raw_value = ''
        
        while state.has_more_chars() and state.current_char() in {' ', '\t', '\n', '\r'}:
            # Handle Windows-style line endings (\r\n)
            if state.current_char() == '\r' and state.peek(1) == '\n':
                if self.store_whitespace:
                    raw_value += '\r\n'
                state.position.line += 1
                state.position.column = 0
                state.advance(2)  # Skip both \r and \n
            # Handle Unix-style line endings (\n)
            elif state.current_char() == '\n':
                if self.store_whitespace:
                    raw_value += state.current_char()
                state.position.line += 1
                state.position.column = 0
                state.advance()
            # Handle other whitespace
            else:
                if self.store_whitespace:
                    raw_value += state.current_char()
                state.position.column += 1
                state.advance()

        if self.store_whitespace:
            state.add_token(TokenType.WHITESPACE, raw_value, start_pos, raw_value)