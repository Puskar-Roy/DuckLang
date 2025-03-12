from typing import Optional
from .error_config import ErrorConfig
from .error_formatter import ErrorFormatter

class DuckLangError(Exception):
    """Base class for DuckLang errors"""
    def __init__(self, 
                 error_type: str,
                 message: str,
                 line: int,
                 column: int,
                 file_name: str,
                 suggestion: Optional[str] = None):
        self.error_type = error_type
        self.message = message
        self.line = line
        self.column = column
        self.file_name = file_name
        self.suggestion = suggestion
        super().__init__(message)

class ErrorHandler:
    def __init__(self):
        self.config = ErrorConfig()
        self.formatter = None
    
    def set_current_file(self, file_content: str):
        """Set the current file being processed for context in error messages"""
        self.formatter = ErrorFormatter(file_content)
    
    def raise_syntax_error(self, 
                          error_type: str,
                          line: int,
                          column: int,
                          file_name: str,
                          **kwargs):
        """Raise a syntax error with formatted message"""
        message = f"[{error_type}] {self.config.get_message(error_type, line=line, **kwargs)}"
        suggestion = self.config.get_suggestion(error_type, **kwargs)
        self._raise_error('Syntax Error', error_type, message, line, column, file_name, suggestion)
    
    def raise_runtime_error(self,
                           error_type: str,
                           line: int,
                           column: int,
                           file_name: str,
                           **kwargs):
        """Raise a runtime error with formatted message"""
        message = f"[{error_type}] {self.config.get_message(error_type, **kwargs)}"
        suggestion = self.config.get_suggestion(error_type, **kwargs)
        self._raise_error('Runtime Error', error_type, message, line, column, file_name, suggestion)
    
    def raise_config_error(self,
                          error_type: str,
                          line: int,
                          column: int,
                          file_name: str,
                          **kwargs):
        """Raise a configuration error with formatted message"""
        message = f"[{error_type}] {self.config.get_message(error_type, **kwargs)}"
        suggestion = self.config.get_suggestion(error_type, **kwargs)
        self._raise_error('Configuration Error', error_type, message, line, column, file_name, suggestion)
    
    def raise_function_error(self,
                           error_type: str,
                           line: int,
                           column: int,
                           file_name: str,
                           **kwargs):
        """Raise a function-related error with formatted message"""
        message = f"[{error_type}] {self.config.get_message(error_type, **kwargs)}"
        suggestion = self.config.get_suggestion(error_type, **kwargs)
        self._raise_error('Function Error', error_type, message, line, column, file_name, suggestion)
    
    def raise_type_error(self,
                        error_type: str,
                        line: int,
                        column: int,
                        file_name: str,
                        **kwargs):
        """Raise a type-related error with formatted message"""
        message = f"[{error_type}] {self.config.get_message(error_type, **kwargs)}"
        suggestion = self.config.get_suggestion(error_type, **kwargs)
        self._raise_error('Type Error', error_type, message, line, column, file_name, suggestion)
    
    def raise_io_error(self,
                      error_type: str,
                      line: int,
                      column: int,
                      file_name: str,
                      **kwargs):
        """Raise an IO-related error with formatted message"""
        message = f"[{error_type}] {self.config.get_message(error_type, **kwargs)}"
        suggestion = self.config.get_suggestion(error_type, **kwargs)
        self._raise_error('IO Error', error_type, message, line, column, file_name, suggestion)
    
    def _raise_error(self,
                    category: str,
                    error_type: str,
                    message: str,
                    line: int,
                    column: int,
                    file_name: str,
                    suggestion: Optional[str] = None):
        """Format and raise the error"""
        if self.formatter:
            formatted_message = self.formatter.format_error(
                category,
                message,
                line,
                column,
                file_name,
                suggestion
            )
            raise DuckLangError(error_type, formatted_message, line, column, file_name, suggestion)
        else:
            # Fallback if no formatter is available
            error_msg = f"{category} at line {line}, column {column} in {file_name}: {message}"
            if suggestion:
                error_msg += f"\nSuggestion: {suggestion}"
            raise DuckLangError(error_type, error_msg, line, column, file_name, suggestion) 