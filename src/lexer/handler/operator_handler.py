from ..token_types import TokenType
from .base import TokenHandler
from .base import LexerState,Position

class OperatorHandler(TokenHandler):
    """Handles the detection and tokenization of operators."""

    OPERATORS = {
        "+": TokenType.PLUS,
        "-": TokenType.MINUS,
        "*": TokenType.MULTIPLY,
        "/": TokenType.DIVIDE,
        "//": TokenType.FLOOR_DIVIDE,
        "**": TokenType.POWER,
        "%": TokenType.MODULO,
        "==": TokenType.EQUALS,
        "!=": TokenType.NOT_EQUALS,
        "<": TokenType.LESS_THAN,
        ">": TokenType.GREATER_THAN,
        "<=": TokenType.LESS_EQUAL,
        ">=": TokenType.GREATER_EQUAL,
        "=": TokenType.ASSIGN,
        "&&": TokenType.AND,
        "||": TokenType.OR,
        "!": TokenType.NOT,
        "->": TokenType.ARROW,
        ",": TokenType.COMMA,
        ".": TokenType.DOT,
        ":": TokenType.COLON,
        ";": TokenType.SEMICOLON,
        "(": TokenType.LEFT_PAREN,
        ")": TokenType.RIGHT_PAREN,
        "{": TokenType.LEFT_BRACE,
        "}": TokenType.RIGHT_BRACE,
        "[": TokenType.LEFT_BRACKET,
        "]": TokenType.RIGHT_BRACKET
    }

    def can_handle(self, state):
        """Check if the current character is the start of an operator."""
        return state.current_char() in self.OPERATORS or state.peek in self.OPERATORS

    def handle(self, state: LexerState, start_pos: Position):
        """Extracts an operator token from the input"""
        start_pos = state.position.copy()

        # Check if peek exists before trying to create a two-character operator
        if state.peek() and (state.current_char() + state.peek()) in self.OPERATORS:
            operator = state.current_char() + state.peek()
            state.advance(2)  # Move ahead by 2 characters
        else:
            operator = state.current_char()
            state.advance()  # Move ahead by 1 character

        token_type = self.OPERATORS.get(operator)

        if token_type is None:
            raise SyntaxError(f"Unknown operator {operator} at {start_pos}")

        state.add_token(token_type, operator, start_pos, state.position.copy())  # Correctly track the end position
