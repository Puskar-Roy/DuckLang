from enum import Enum

class TokenType(Enum):
    # Commands
    PRINT_COMMAND = "PRINT_COMMAND"
    VARIABLE_DECLARE = "VARIABLE_DECLARE"
    FUNCTION = "FUNCTION"

    # Basic Data Types
    IDENTIFIER = "IDENTIFIER"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    STRING = "STRING"
    BYTES = "BYTES"
    BOOLEAN = "BOOLEAN"
    NONE = "NONE"

    # Brackets 
    LEFT_PAREN = "LEFT_PAREN"      # (
    RIGHT_PAREN = "RIGHT_PAREN"    # )
    LEFT_BRACKET = "LEFT_BRACKET"  # [
    RIGHT_BRACKET = "RIGHT_BRACKET" # ]
    LEFT_BRACE = "LEFT_BRACE"      # {
    RIGHT_BRACE = "RIGHT_BRACE"    # }

    # Operators
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    FLOOR_DIVIDE = "FLOOR_DIVIDE"
    POWER = "POWER"
    MODULO = "MODULO"

    # Comparisons
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    LESS_EQUAL = "LESS_EQUAL"
    GREATER_EQUAL = "GREATER_EQUAL"

    # Logical
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    IN = "IN"
    NOT_IN = "NOT_IN"
    IS = "IS"
    IS_NOT = "IS_NOT"

    # Control Flow
    FOR = "FOR"
    IF = "IF"
    ELSE = "ELSE"
    WHILE = "WHILE"
    BREAK = "BREAK"
    CONTINUE = "CONTINUE"
    RETURN = "RETURN"

    # Miscellaneous
    COMMA = "COMMA"
    DOT = "DOT"
    COLON = "COLON"
    SEMICOLON = "SEMICOLON"
    ASSIGN = "ASSIGN"
    ARROW = "ARROW"
    WHITESPACE = "WHITESPACE"
    NEWLINE = "NEWLINE"  

class Position:
    def __init__(self, line, column, index=0):
        self.line = line
        self.column = column
        self.index = index
    
    def copy(self):
        return Position(self.line, self.column, self.index)
    
    def __str__(self):
        return f"line {self.line}, column {self.column}"

class Token:
    def __init__(self, token_type: TokenType, value, start_pos: Position, end_pos: Position, raw=None):
        self.token_type = token_type
        self.value = value
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.raw = raw if raw is not None else str(value)

    def __repr__(self):
        return f"Token({self.token_type}, {repr(self.value)}, {self.start_pos}, {self.end_pos})"

    def __str__(self):
        return f"{self.token_type}({repr(self.value)})"