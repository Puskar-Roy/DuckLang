from .base_parser import BaseParser
from ..ast import AssignmentNode
from ...lexer.token_types import TokenType
from .expression_parser import ExpressionParser

class AssignmentParser(BaseParser):
    def __init__(self, tokens):
        super().__init__(tokens)
        self.debug_mode = True

    def debug(self, message):
        if self.debug_mode:
            print(f"[AssignmentParser DEBUG] {message}")

    def parse(self):
        start_pos = self.current
        
        # Get the identifier token
        identifier_token = self.tokens[self.current]
        self.debug(f"Parsing assignment for: {identifier_token.value}")
        self.advance()  # Move past identifier
        
        # Skip any whitespace
        while self.current < len(self.tokens) and self.tokens[self.current].token_type == TokenType.WHITESPACE:
            self.advance()
        
        # Consume the assignment operator
        if self.current >= len(self.tokens) or self.tokens[self.current].token_type != TokenType.ASSIGN:
            raise SyntaxError(f"Expected '=' after identifier, got {self.tokens[self.current].token_type if self.current < len(self.tokens) else 'END OF TOKENS'}.")
        self.advance()  # Move past '='
        
        # Skip any whitespace
        while self.current < len(self.tokens) and self.tokens[self.current].token_type == TokenType.WHITESPACE:
            self.advance()
        
        # Debug print all tokens from current position
        self.debug("Tokens for parsing:")
        for i, token in enumerate(self.tokens[self.current:]):
            self.debug(f"{i}: {token}")
        
        # Create an expression parser using the current token index
        expression_parser = ExpressionParser(self.tokens[self.current:])
        expression, expr_consumed = expression_parser.parse()
        
        # Verify expression was parsed
        if expression is None:
            raise SyntaxError("Could not parse expression in assignment")
        
        # Update current position based on tokens consumed by expression parser
        self.current += expr_consumed
        
        # Calculate total tokens consumed
        consumed = self.current - start_pos
        
        self.debug(f"Successfully parsed assignment: {identifier_token.value} = {expression}")
        self.debug(f"Tokens consumed: {consumed}")
        
        # Return both the node and tokens consumed
        return AssignmentNode(identifier_token.value, expression), consumed