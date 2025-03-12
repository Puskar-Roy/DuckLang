from ..token_types import TokenType
from ..state import LexerState, Position
from .base import TokenHandler
from src.utils.config import LanguageConfig

class IdentifierHandler(TokenHandler):
    """Handles identifiers and keywords."""

    def __init__(self):
        super().__init__()
        self.config = LanguageConfig.get_instance()

    def can_handle(self, state: LexerState):
        """Check if the current character starts an identifier (letter or underscore)."""
        char = state.current_char()
        return char is not None and (char.isalpha() or char == "_")
    
    def handle(self, state: LexerState, start_pos: Position):
        """Processes identifiers and keywords."""
        identifier = ""

        # Read while the character is alphanumeric or underscore
        while True:
            char = state.current_char()
            if char is None or not (char.isalnum() or char == "_"):
                break
            identifier += char
            state.advance()

        # Convert to lowercase for keyword comparison
        lower_identifier = identifier.lower()
        
        # Get token type from configuration
        token_type = self.config.get_token_type(lower_identifier)
        if token_type is None:
            token_type = TokenType.IDENTIFIER
        
        # Handle special cases
        if token_type == TokenType.BOOLEAN:
            value = lower_identifier == self.config.get_keyword(TokenType.BOOLEAN)
        elif token_type == TokenType.NONE:
            value = None
        elif token_type == TokenType.IDENTIFIER:
            value = identifier  # Keep original case for identifiers
        else:
            value = lower_identifier  # Use lowercase for keywords

        # Store the token
        state.add_token(token_type, value, start_pos, identifier)