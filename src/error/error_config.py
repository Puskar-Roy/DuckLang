from typing import Dict, Optional
from dotenv import load_dotenv
import os

class ErrorConfig:
    def __init__(self):
        load_dotenv()
        self.default_messages = {
            # Syntax Errors
            'SYNTAX_GENERIC': "Quack! Your code seems a bit scrambled at line {line}",
            'MISSING_BRACKET': "Waddle waddle... missing a {bracket_type} at line {line}",
            'INVALID_TOKEN': "This syntax makes me want to duck for cover! Found {token} at line {line}",
            'UNEXPECTED_TOKEN': "Found a strange duck in the pond: {token} at line {line}",
            'INVALID_INDENTATION': "Your ducks aren't lined up properly at line {line}",
            'MISSING_SEMICOLON': "Missing a tail feather at line {line}",
            
            # Runtime Errors
            'DIVISION_BY_ZERO': "That operation is like dividing by zero ducks... impossible!",
            'UNDEFINED_VAR': "This variable seems to have flown south for the winter: {var_name}",
            'TYPE_MISMATCH': "Expected a duck, but got a goose! Expected {expected_type} but got {actual_type}",
            'INDEX_OUT_OF_RANGE': "Trying to catch a duck that's not in the pond! Index {index} is out of range",
            'STACK_OVERFLOW': "Too many nested ducks! Stack overflow at line {line}",
            'MEMORY_ERROR': "The duck pond is full! Out of memory at line {line}",
            
            # Function Errors
            'UNDEFINED_FUNCTION': "Can't find this duck call: {func_name}",
            'INVALID_ARGUMENTS': "Wrong number of ducks! Expected {expected} arguments but got {actual}",
            'RECURSION_LIMIT': "Too much duck recursion! Maximum depth exceeded",
            
            # Configuration Errors
            'INVALID_KEYWORD': "That keyword doesn't fit in our duck pond: {keyword}",
            'DUPLICATE_KEYWORD': "Two ducks can't share the same name: {keyword} is already used for {existing_use}",
            'INVALID_CONFIG': "Your duck configuration seems wrong: {details}",
            
            # Import/Module Errors
            'MODULE_NOT_FOUND': "Couldn't find this duck module: {module}",
            'CIRCULAR_IMPORT': "Your ducks are chasing their own tails! Circular import detected",
            
            # Type Errors
            'TYPE_CONVERSION': "Can't turn this {from_type} duck into a {to_type} duck!",
            'INVALID_OPERATION': "These ducks don't play well together: can't {operation} with {type1} and {type2}",
            'NULL_REFERENCE': "Found an empty nest where a duck should be!",
            
            # IO Errors
            'FILE_NOT_FOUND': "This duck nest doesn't exist: {file}",
            'PERMISSION_DENIED': "This duck pond is private! No permission to access {file}",
            'IO_ERROR': "Duck communication error: {details}"
        }
        
        self.suggestions = {
            'SYNTAX_GENERIC': "Check your syntax and make sure all brackets and parentheses are properly closed.",
            'MISSING_BRACKET': "Add a closing {bracket_type} to match the opening one.",
            'INVALID_TOKEN': "Make sure you're using valid DuckLang syntax and keywords.",
            'UNEXPECTED_TOKEN': "Remove or replace the unexpected {token}.",
            'INVALID_INDENTATION': "Fix the indentation to match the code block structure.",
            'DIVISION_BY_ZERO': "Check your division operation and make sure the denominator is not zero.",
            'UNDEFINED_VAR': "Declare the variable '{var_name}' before using it.",
            'TYPE_MISMATCH': "Convert your {actual_type} to {expected_type} before this operation.",
            'INDEX_OUT_OF_RANGE': "Make sure your index is within the valid range [0 to {max_index}].",
            'STACK_OVERFLOW': "Reduce the number of nested function calls or recursion depth.",
            'UNDEFINED_FUNCTION': "Define the function '{func_name}' before calling it.",
            'INVALID_ARGUMENTS': "Provide exactly {expected} arguments to this function.",
            'TYPE_CONVERSION': "Use appropriate type conversion functions or check your data types.",
            'INVALID_OPERATION': "Make sure both operands are of compatible types for {operation}.",
            'NULL_REFERENCE': "Initialize your variable before using it.",
            'FILE_NOT_FOUND': "Check if the file path '{file}' is correct and the file exists.",
            'PERMISSION_DENIED': "Run the program with appropriate permissions or check file access rights.",
            'CIRCULAR_IMPORT': "Restructure your imports to avoid circular dependencies."
        }
        
        self.messages = self._load_custom_messages()
    
    def _load_custom_messages(self) -> Dict[str, str]:
        """Load custom error messages from .env file, falling back to defaults"""
        messages = {}
        for key in self.default_messages.keys():
            env_key = f"ERROR_{key}"
            messages[key] = os.getenv(env_key, self.default_messages[key])
        return messages
    
    def get_message(self, error_type: str, **kwargs) -> str:
        """Get formatted error message with placeholders filled in"""
        message = self.messages.get(error_type, self.default_messages.get(error_type))
        if not message:
            return self.default_messages['SYNTAX_GENERIC'].format(line=kwargs.get('line', '?'))
        
        try:
            return message.format(**kwargs)
        except KeyError:
            return self.default_messages['SYNTAX_GENERIC'].format(line=kwargs.get('line', '?'))
    
    def get_suggestion(self, error_type: str, **kwargs) -> Optional[str]:
        """Get a helpful suggestion for the error"""
        suggestion = self.suggestions.get(error_type)
        if not suggestion:
            return None
            
        try:
            return suggestion.format(**kwargs)
        except KeyError:
            return None 