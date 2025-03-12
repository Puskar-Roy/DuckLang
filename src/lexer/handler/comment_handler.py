from .base import TokenHandler
from ..token_types import TokenType
from ..state import LexerState, Position

class CommentHandler(TokenHandler):
    """Handles single-line (#, //) and multi-line (/* */) comments."""

    def can_handle(self, state):
        """Check if the current character starts a comment."""
        current = state.current_char()
        if current is None:
            return False
            
        # Check for // or /* first (they're two characters)
        if current == '/':
            next_char = state.peek()
            return next_char in ['/', '*']
        # Then check for #
        return current == '#'

    def handle(self, state: LexerState, start_pos: Position):
        """Extracts and handles a comment token."""
        start_pos = state.position.copy()
        current = state.current_char()

        # Multi-line comment (e.g., /* This is a multi-line comment */)
        if current == '/' and state.peek() == '*':
            state.advance(2)  # Skip /*
            while not state.is_at_end() and not (state.current_char() == '*' and state.peek() == '/'):
                state.advance()
            if not state.is_at_end():
                state.advance(2)  # Skip */
            return  # Ignore comment

        # Single-line comment (e.g., // This is a comment)
        if current == '/' and state.peek() == '/':
            state.advance(2)  # Skip //
            while not state.is_at_end() and state.current_char() != '\n':
                state.advance()
            return  # Ignore comment

        # Single-line comment (e.g., # This is a comment)
        if current == '#':
            state.advance()  # Skip #
            while not state.is_at_end() and state.current_char() != '\n':
                state.advance()
            return  # Ignore comment

        # If we reach here, something went wrong
        raise ValueError(f"Unrecognized comment at position {start_pos}")

