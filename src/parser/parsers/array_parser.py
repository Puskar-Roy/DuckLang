from ...lexer.token_types import TokenType
from ..ast import ArrayNode, ArrayAccessNode
from .base_expression_parser import BaseExpressionParser
from ...utils.debug import DebugLevel

class ArrayParser(BaseExpressionParser):
    def parse_array_literal(self):
        """Parse an array literal: [expr1, expr2, ...]"""
        self.debug("Parsing array literal", DebugLevel.DEBUG)
        
        if not self.match(TokenType.LEFT_BRACKET):
            return None, 0
            
        elements = []
        start_pos = self.current
        
        while not self.check(TokenType.RIGHT_BRACKET):
            if len(elements) > 0:
                if not self.match(TokenType.COMMA):
                    error_msg = "Expected ',' between array elements"
                    self.debug(error_msg, DebugLevel.ERROR)
                    raise SyntaxError(error_msg)
                self.skip_whitespace()
                
            expr_parser = self.get_expression_parser()
            expression, consumed = expr_parser.parse()
            
            if not expression:
                if len(elements) == 0 and self.check(TokenType.RIGHT_BRACKET):
                    break  # Empty array
                error_msg = "Expected expression in array"
                self.debug(error_msg, DebugLevel.ERROR)
                raise SyntaxError(error_msg)
                
            elements.append(expression)
            self.current += consumed
            self.skip_whitespace()
            
        if not self.match(TokenType.RIGHT_BRACKET):
            error_msg = "Expected ']' after array elements"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        return ArrayNode(elements), self.current - start_pos

    def parse_array_access(self, array_expr):
        """Parse array access: array[index]"""
        self.debug("Parsing array access", DebugLevel.DEBUG)
        
        if not self.match(TokenType.LEFT_BRACKET):
            return None, 0
            
        self.skip_whitespace()
        expr_parser = self.get_expression_parser()
        index_expr, consumed = expr_parser.parse()
        
        if not index_expr:
            error_msg = "Expected index expression in array access"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        self.current += consumed
        self.skip_whitespace()
        
        if not self.match(TokenType.RIGHT_BRACKET):
            error_msg = "Expected ']' after array index"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        return ArrayAccessNode(array_expr, index_expr), self.current

    def get_expression_parser(self):
        """Get a new expression parser starting from current position"""
        from .expression_parser import ExpressionParser
        return ExpressionParser(self.tokens[self.current:]) 