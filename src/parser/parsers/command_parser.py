from ...lexer.token_types import TokenType
from ..ast import PrintNode, VariableDeclarationNode
from .base_expression_parser import BaseExpressionParser
from ...utils.debug import DebugLevel

class CommandParser(BaseExpressionParser):
    def parse_print(self):
        """Parse a print statement: print <expression>"""
        self.debug("Parsing print command", DebugLevel.DEBUG)
        
        if not self.match(TokenType.PRINT_COMMAND):
            return None, 0
            
        self.skip_whitespace()
        expr_parser = self.get_expression_parser()
        expression, consumed = expr_parser.parse()
        
        if not expression:
            error_msg = "Expected expression after print command"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        return PrintNode(expression), self.current + consumed

    def parse_variable_declaration(self):
        """Parse a variable declaration: var <identifier> = <expression>"""
        self.debug("Parsing variable declaration", DebugLevel.DEBUG)
        
        if not self.match(TokenType.VARIABLE_DECLARE):
            return None, 0
            
        self.skip_whitespace()
        
        if not self.match(TokenType.IDENTIFIER):
            error_msg = "Expected identifier after variable declaration"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        identifier = self.previous().value
        self.skip_whitespace()
        
        if not self.match(TokenType.ASSIGN):
            error_msg = "Expected '=' after variable identifier"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        self.skip_whitespace()
        expr_parser = self.get_expression_parser()
        expression, consumed = expr_parser.parse()
        
        if not expression:
            error_msg = "Expected expression after '='"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        return VariableDeclarationNode(identifier, expression), self.current + consumed

    def get_expression_parser(self):
        """Get a new expression parser starting from current position"""
        from .expression_parser import ExpressionParser
        return ExpressionParser(self.tokens[self.current:]) 