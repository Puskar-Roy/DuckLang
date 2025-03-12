from ...lexer.token_types import TokenType
from ..ast import BlockNode
from .base_expression_parser import BaseExpressionParser
from ...utils.debug import DebugLevel

class BlockParser(BaseExpressionParser):
    def parse_block(self):
        """Parse a code block: { statement1; statement2; ... }"""
        self.debug("Parsing code block", DebugLevel.DEBUG)
        
        if not self.match(TokenType.LEFT_BRACE):
            return None, 0
            
        statements = []
        start_pos = self.current
        
        self.skip_whitespace()
        
        while not self.check(TokenType.RIGHT_BRACE):
            if self.is_at_end():
                error_msg = "Unterminated code block"
                self.debug(error_msg, DebugLevel.ERROR)
                raise SyntaxError(error_msg)
                
            statement = self.parse_statement()
            if statement:
                statements.append(statement)
                
            # Skip any statement separators (semicolon or newline)
            while self.match(TokenType.SEMICOLON, TokenType.NEWLINE):
                self.skip_whitespace()
                
        if not self.match(TokenType.RIGHT_BRACE):
            error_msg = "Expected '}' after block statements"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        return BlockNode(statements), self.current - start_pos

    def parse_statement(self):
        """Parse a single statement"""
        from .statement_parser import StatementParser
        parser = StatementParser(self.tokens[self.current:])
        statement, consumed = parser.parse()
        if statement:
            self.current += consumed
        return statement 