import os
from dotenv import load_dotenv
from src.lexer.token_types import TokenType

class LanguageConfig:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        self.load_config()
    
    def load_config(self):
        """Load configuration from .env file"""
        load_dotenv()
        
        # Default keywords if not specified in .env
        self.keyword_mappings = {
            'print': TokenType.PRINT_COMMAND,
            'if': TokenType.IF,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'for': TokenType.FOR,
            'function': TokenType.FUNCTION,
            'return': TokenType.RETURN,
            'break': TokenType.BREAK,
            'continue': TokenType.CONTINUE,
            'and': TokenType.AND,
            'or': TokenType.OR,
            'not': TokenType.NOT,
            'true': TokenType.BOOLEAN,
            'false': TokenType.BOOLEAN,
            'none': TokenType.NONE,
            'var': TokenType.VARIABLE_DECLARE
        }
        
        # Override with custom keywords from .env
        custom_keywords = {
            'KEYWORD_PRINT': TokenType.PRINT_COMMAND,
            'KEYWORD_IF': TokenType.IF,
            'KEYWORD_ELSE': TokenType.ELSE,
            'KEYWORD_WHILE': TokenType.WHILE,
            'KEYWORD_FOR': TokenType.FOR,
            'KEYWORD_FUNCTION': TokenType.FUNCTION,
            'KEYWORD_RETURN': TokenType.RETURN,
            'KEYWORD_BREAK': TokenType.BREAK,
            'KEYWORD_CONTINUE': TokenType.CONTINUE,
            'KEYWORD_AND': TokenType.AND,
            'KEYWORD_OR': TokenType.OR,
            'KEYWORD_NOT': TokenType.NOT,
            'KEYWORD_TRUE': TokenType.BOOLEAN,
            'KEYWORD_FALSE': TokenType.BOOLEAN,
            'KEYWORD_NONE': TokenType.NONE,
            'KEYWORD_VAR': TokenType.VARIABLE_DECLARE
        }
        
        # Update keyword mappings with custom keywords from .env
        for env_key, token_type in custom_keywords.items():
            custom_keyword = os.getenv(env_key)
            if custom_keyword:
                # Remove old mapping if it exists
                old_keyword = next((k for k, v in self.keyword_mappings.items() if v == token_type), None)
                if old_keyword:
                    del self.keyword_mappings[old_keyword]
                # Add new mapping
                self.keyword_mappings[custom_keyword.lower()] = token_type
    
    def get_keyword(self, token_type):
        """Get the keyword string for a given token type"""
        for keyword, t_type in self.keyword_mappings.items():
            if t_type == token_type:
                return keyword
        return None
    
    def get_token_type(self, keyword):
        """Get the token type for a given keyword string"""
        return self.keyword_mappings.get(keyword.lower()) 