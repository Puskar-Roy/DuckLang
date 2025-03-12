from .state import LexerState
from .handler.whitespace_hadler import WhiteSpaceHandler
from .handler.comment_handler import CommentHandler
from .handler.number_handler import NumberHandler
from .handler.string_handler import StringHandler
from .handler.operator_handler import OperatorHandler
from .handler.identifier_handler import IdentifierHandler
from .token_types import TokenType, Token

class Lexer:
    """Main Lexer class to tokenize source code."""

    def __init__(self):
        """Initialize all token handlers."""
        self.debug_mode = False
        self.handlers = [
            WhiteSpaceHandler(),
            CommentHandler(),
            NumberHandler(),
            StringHandler(),
            OperatorHandler(),
            IdentifierHandler(),
        ]

    def tokenize(self, source):
        """Tokenizes the input source code and returns a list of tokens."""
        state = LexerState(source)

        while state.has_more_chars():
            if self.debug_mode:
                print(f"Processing: '{state.current_char()}' at {state.position}")
            
            start_pos = state.position.copy()
            handler_found = False
            
            for handler in self.handlers:
                if handler.can_handle(state):
                    if self.debug_mode:
                        print(f"Using handler: {handler.__class__.__name__}")
                    handler.handle(state, start_pos)
                    handler_found = True
                    break

            if not handler_found:
                if self.debug_mode:
                    print(f"Current char: '{state.current_char()}', Position: {state.position}")
                raise SyntaxError(f"Unexpected character '{state.current_char()}' at {start_pos}")

        return state.tokens
