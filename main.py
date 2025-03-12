import sys
from src.error import ErrorHandler, DuckLangError
from src.lexer import Lexer
from src.parser.main_parser import MainParser
from src.interpreter import Interpreter
from src.utils.debug import debug, DebugLevel

def execute_program(source_code, file_path, error_handler):
    """Execute a DuckLang program with proper error handling"""
    try:
        # Create instances
        lexer = Lexer()
        tokens = lexer.tokenize(source_code)
        
        parser = MainParser(tokens)
        ast = parser.parse()
        
        if not ast:
            error_handler.raise_syntax_error(
                'SYNTAX_GENERIC',
                line=1,
                column=0,
                file_name=file_path,
                message="Could not generate AST"
            )
            return
            
        # Execute the program
        interpreter = Interpreter(debug_mode=True)
        interpreter.interpret(ast)
        
    except Exception as e:
        # Get line and column info if available
        line = getattr(e, 'line', 1)
        column = getattr(e, 'column', 0)
        
        # Determine error type from exception
        if 'division by zero' in str(e):
            error_handler.raise_runtime_error(
                'DIVISION_BY_ZERO',
                line=line,
                column=column,
                file_name=file_path
            )
        elif 'undefined variable' in str(e):
            error_handler.raise_runtime_error(
                'UNDEFINED_VAR',
                line=line,
                column=column,
                file_name=file_path,
                var_name=str(e).split("'")[1] if "'" in str(e) else "unknown"
            )
        elif 'type mismatch' in str(e):
            error_handler.raise_runtime_error(
                'TYPE_MISMATCH',
                line=line,
                column=column,
                file_name=file_path,
                expected_type=getattr(e, 'expected_type', 'unknown'),
                actual_type=getattr(e, 'actual_type', 'unknown')
            )
        else:
            # Default to syntax error for unrecognized errors
            error_handler.raise_syntax_error(
                'SYNTAX_GENERIC',
                line=line,
                column=column,
                file_name=file_path
            )

def main():
    # Check if a file was provided
    if len(sys.argv) < 2:
        print("🦆 Quack! Please provide a .duck file to run")
        print("Usage: python main.py your_program.duck")
        sys.exit(1)

    # Get the file path from command line arguments
    file_path = sys.argv[1]
    
    try:
        # Initialize error handler
        error_handler = ErrorHandler()
        
        # Read the file
        with open(file_path, 'r') as file:
            file_content = file.read()
            
        # Set up error handling for this file
        error_handler.set_current_file(file_content)
        
        # Execute the program
        execute_program(file_content, file_path, error_handler)
        
    except FileNotFoundError:
        print(f"🦆 Quack! Cannot find file '{file_path}'")
        print("Make sure the file exists and the path is correct!")
        sys.exit(1)
    except DuckLangError as e:
        # This is our custom error, just print its message
        print(e)
        sys.exit(1)
    except Exception as e:
        # For unexpected errors during startup
        print("🦆 Quack! Something went wrong while starting up!")
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
