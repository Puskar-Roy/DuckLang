from ...lexer.token_types import TokenType
from ..ast import IfNode, WhileNode, ForNode, ReturnNode, BreakNode, ContinueNode
from .base_expression_parser import BaseExpressionParser
from ...utils.debug import DebugLevel

class ControlFlowParser(BaseExpressionParser):
    def parse_if(self):
        """Parse if statement: if (condition) { block } else { block }"""
        self.debug("Parsing if statement", DebugLevel.DEBUG)
        
        if not self.match(TokenType.IF):
            return None, 0
            
        self.skip_whitespace()
        
        # Parse condition
        if not self.match(TokenType.LEFT_PAREN):
            error_msg = "Expected '(' after 'if'"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        condition, consumed = self.get_expression_parser().parse()
        if not condition:
            error_msg = "Expected condition in if statement"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        self.current += consumed
        self.skip_whitespace()
        
        if not self.match(TokenType.RIGHT_PAREN):
            error_msg = "Expected ')' after if condition"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        # Parse if block
        if_block, consumed = self.get_block_parser().parse_block()
        if not if_block:
            error_msg = "Expected block after if condition"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        self.current += consumed
        self.skip_whitespace()
        
        # Parse optional else block
        else_block = None
        if self.match(TokenType.ELSE):
            self.skip_whitespace()
            else_block, consumed = self.get_block_parser().parse_block()
            if not else_block:
                error_msg = "Expected block after 'else'"
                self.debug(error_msg, DebugLevel.ERROR)
                raise SyntaxError(error_msg)
            self.current += consumed
            
        return IfNode(condition, if_block, else_block), self.current

    def parse_while(self):
        """Parse while statement: while (condition) { block }"""
        self.debug("Parsing while statement", DebugLevel.DEBUG)
        
        if not self.match(TokenType.WHILE):
            return None, 0
            
        self.skip_whitespace()
        
        # Parse condition
        if not self.match(TokenType.LEFT_PAREN):
            error_msg = "Expected '(' after 'while'"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        condition, consumed = self.get_expression_parser().parse()
        if not condition:
            error_msg = "Expected condition in while statement"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        self.current += consumed
        self.skip_whitespace()
        
        if not self.match(TokenType.RIGHT_PAREN):
            error_msg = "Expected ')' after while condition"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        # Parse block
        block, consumed = self.get_block_parser().parse_block()
        if not block:
            error_msg = "Expected block after while condition"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        self.current += consumed
        return WhileNode(condition, block), self.current

    def parse_for(self):
        """Parse for statement: for (init; condition; update) { block }"""
        self.debug("Parsing for statement", DebugLevel.DEBUG)
        
        if not self.match(TokenType.FOR):
            return None, 0
            
        self.skip_whitespace()
        
        if not self.match(TokenType.LEFT_PAREN):
            error_msg = "Expected '(' after 'for'"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        # Parse initialization
        init, consumed = self.get_statement_parser().parse()
        self.current += consumed
        
        if not self.match(TokenType.SEMICOLON):
            error_msg = "Expected ';' after for init"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        # Parse condition
        condition, consumed = self.get_expression_parser().parse()
        self.current += consumed
        
        if not self.match(TokenType.SEMICOLON):
            error_msg = "Expected ';' after for condition"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        # Parse update
        update, consumed = self.get_statement_parser().parse()
        self.current += consumed
        
        if not self.match(TokenType.RIGHT_PAREN):
            error_msg = "Expected ')' after for clauses"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        # Parse block
        block, consumed = self.get_block_parser().parse_block()
        if not block:
            error_msg = "Expected block in for statement"
            self.debug(error_msg, DebugLevel.ERROR)
            raise SyntaxError(error_msg)
            
        self.current += consumed
        return ForNode(init, condition, update, block), self.current

    def parse_return(self):
        """Parse return statement: return [expression];"""
        self.debug("Parsing return statement", DebugLevel.DEBUG)
        
        if not self.match(TokenType.RETURN):
            return None, 0
            
        self.skip_whitespace()
        
        # Parse optional return value
        value = None
        if not self.check(TokenType.SEMICOLON, TokenType.NEWLINE):
            expr, consumed = self.get_expression_parser().parse()
            if expr:
                value = expr
                self.current += consumed
                
        return ReturnNode(value), self.current

    def parse_break(self):
        """Parse break statement: break;"""
        self.debug("Parsing break statement", DebugLevel.DEBUG)
        
        if not self.match(TokenType.BREAK):
            return None, 0
            
        return BreakNode(), self.current

    def parse_continue(self):
        """Parse continue statement: continue;"""
        self.debug("Parsing continue statement", DebugLevel.DEBUG)
        
        if not self.match(TokenType.CONTINUE):
            return None, 0
            
        return ContinueNode(), self.current

    def get_expression_parser(self):
        from .expression_parser import ExpressionParser
        return ExpressionParser(self.tokens[self.current:])

    def get_block_parser(self):
        from .block_parser import BlockParser
        return BlockParser(self.tokens[self.current:])

    def get_statement_parser(self):
        from .statement_parser import StatementParser
        return StatementParser(self.tokens[self.current:]) 