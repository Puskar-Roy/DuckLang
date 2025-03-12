from src.lexer.token_types import Token

class Position:
    """Tracks the position (index, line, column) in the source code."""
    def __init__(self, index=0, line=1, column=1):
        self.index = index
        self.line = line
        self.column = column

    def copy(self):
        """Returns a copy of the current position."""
        return Position(self.index, self.line, self.column)

    def advance(self, char):
        """Advances the position, updating line and column numbers."""
        self.index += 1
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1

    def __str__(self):
        return f"line {self.line}, column {self.column}"

class LexerState:
    """Manages the current state of the lexer, including character position and tokens."""
    def __init__(self, source: str):
        self.source = source
        self.position = Position()
        self.tokens = []
        
    def current_char(self):
        """Returns the current character being processed or None if at end."""
        if self.is_at_end():
            return None
        return self.source[self.position.index]

    def is_at_end(self):
        """Checks if we've reached the end of the source."""
        return self.position.index >= len(self.source)

    def has_more_chars(self):
        """Checks if there are more characters left to process."""
        return not self.is_at_end()
    
    def next_char(self):
        """Returns the next character in the source code or None if at end."""
        if self.is_at_end() or self.position.index + 1 >= len(self.source):
            return None
        return self.source[self.position.index + 1]

    def advance(self, steps=1):
        """Moves forward in the source code by a given number of characters."""
        for _ in range(steps):
            if self.has_more_chars():
                char = self.current_char()
                self.position.advance(char)

    def peek(self, offset=1):
        """Looks ahead in the source without advancing the position."""
        peek_index = self.position.index + offset
        if peek_index >= len(self.source):
            return None
        return self.source[peek_index]
    
    def match(self, text):
        """Checks if the next characters match the given text and advances if true."""
        if self.position.index + len(text) > len(self.source):
            return False
        
        if self.source[self.position.index:self.position.index + len(text)] == text:
            for _ in range(len(text)):
                self.advance()
            return True
        return False

    def add_token(self, token_type, value, start_pos, raw=None):
        """Creates and stores a new token."""
        if raw is None:
            raw = str(value)
            
        token = Token(
            token_type=token_type,
            value=value,
            start_pos=start_pos,
            end_pos=self.position.copy(),
            raw=raw
        )
        self.tokens.append(token)