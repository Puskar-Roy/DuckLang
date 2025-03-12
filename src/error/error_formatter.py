from typing import Optional, List, Tuple
import os

class ErrorFormatter:
    """Formats error messages with color and context"""
    
    def __init__(self, file_content: str):
        self.file_content = file_content
        self.lines = file_content.split('\n')
        
        # ANSI color codes
        self.RED = '\033[91m'
        self.YELLOW = '\033[93m'
        self.BLUE = '\033[94m'
        self.GREEN = '\033[92m'
        self.GRAY = '\033[90m'
        self.RESET = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
        
        # Disable colors if not supported
        if os.name == 'nt' and not os.environ.get('FORCE_COLOR'):
            self.RED = self.YELLOW = self.BLUE = self.GREEN = self.GRAY = ''
            self.RESET = self.BOLD = self.UNDERLINE = ''
    
    def format_error(self,
                    category: str,
                    message: str,
                    line: int,
                    column: int,
                    file_name: str,
                    suggestion: Optional[str] = None,
                    context_lines: int = 2) -> str:
        """Format an error message with context and color
        
        Args:
            category: The type of error (e.g., 'Syntax Error', 'Runtime Error')
            message: The error message to display
            line: The line number where the error occurred (1-based)
            column: The column number where the error occurred (0-based)
            file_name: The name of the file containing the error
            suggestion: Optional suggestion for fixing the error
            context_lines: Number of lines of context to show before and after the error
        
        Returns:
            A formatted error message string with color and context
        """
        error_lines = []
        
        # Header with error type and location
        error_lines.extend([
            f"{self.BOLD}🦆 DuckLang Error: {category}{self.RESET}",
            f"{self.BLUE}📍 {self._format_location(line, column, file_name)}{self.RESET}",
            f"{self.RED}❌ {message}{self.RESET}",
            ""
        ])
        
        # Add code context if available
        if self.lines and 0 <= line - 1 < len(self.lines):
            error_lines.extend(self._format_code_context(line, column, context_lines))
        
        # Add suggestion if available
        if suggestion:
            error_lines.extend([
                "",
                f"{self.GREEN}💡 Suggestion:{self.RESET}",
                f"   {suggestion}"
            ])
        
        return "\n".join(error_lines)
    
    def _format_location(self, line: int, column: int, file_name: str) -> str:
        """Format the error location information"""
        location_parts = []
        
        # Add line and column info
        if line > 0:
            location_parts.append(f"Line {line}")
        if column >= 0:
            location_parts.append(f"Column {column}")
        
        # Add file name
        if file_name:
            location_parts.append(f"in '{file_name}'")
        
        return ", ".join(location_parts)
    
    def _format_code_context(self, error_line: int, error_column: int, context_lines: int) -> List[str]:
        """Format the code context around the error
        
        Args:
            error_line: The line number where the error occurred (1-based)
            error_column: The column where the error occurred (0-based)
            context_lines: Number of lines to show before and after the error
        
        Returns:
            List of formatted context lines
        """
        output = ["Code:"]
        
        # Calculate the range of lines to show
        start_line = max(1, error_line - context_lines)
        end_line = min(len(self.lines), error_line + context_lines)
        
        # Calculate line number width for padding
        line_num_width = len(str(end_line))
        
        # Show the context lines
        for line_num in range(start_line, end_line + 1):
            # Get the line content
            line_idx = line_num - 1
            if 0 <= line_idx < len(self.lines):
                line_content = self.lines[line_idx]
                
                # Format the line prefix
                if line_num == error_line:
                    prefix = f"{self.RED}>{self.RESET}"
                    line_num_color = self.RED
                else:
                    prefix = " "
                    line_num_color = self.GRAY
                
                # Format the line
                formatted_line = (
                    f"{prefix} {line_num_color}{line_num:>{line_num_width}} |{self.RESET} "
                    f"{line_content}"
                )
                output.append(formatted_line)
                
                # Add error pointer if this is the error line
                if line_num == error_line and error_column >= 0:
                    pointer = " " * (line_num_width + 4 + error_column) + "^"
                    output.append(f"{self.RED}{pointer}{self.RESET}")
        
        return output
    
    def get_line_context(self, line: int, context_lines: int = 2) -> str:
        """Get the surrounding lines of code for context
        
        Args:
            line: The line number to get context for (1-based)
            context_lines: Number of lines to show before and after
        
        Returns:
            A string containing the formatted context lines
        """
        return "\n".join(self._format_code_context(line, -1, context_lines)) 