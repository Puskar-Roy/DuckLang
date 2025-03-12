# DuckLang Error Handling System

The DuckLang error handling system provides detailed, user-friendly error messages with context and suggestions for fixing issues. The system is designed to be both informative and entertaining, using duck-themed messages to make debugging more enjoyable.

## Features

- 🎯 **Precise Error Location**: Line and column numbers for exact error positioning
- 📝 **Code Context**: Shows surrounding code with the error line highlighted
- 💡 **Helpful Suggestions**: Provides specific suggestions for fixing each error
- 🎨 **Color-Coded Output**: Uses colors to highlight different parts of error messages
- 🦆 **Duck-Themed Messages**: Fun, memorable error messages with a duck theme
- ⚙️ **Customizable Messages**: Ability to override default messages via `.env` file

## Error Categories

DuckLang provides several categories of errors to help identify and fix issues:

### Syntax Errors
- `SYNTAX_GENERIC`: General syntax errors
- `MISSING_BRACKET`: Missing closing brackets/parentheses
- `INVALID_TOKEN`: Invalid characters or tokens
- `UNEXPECTED_TOKEN`: Valid tokens in wrong places
- `INVALID_INDENTATION`: Incorrect code indentation

### Runtime Errors
- `DIVISION_BY_ZERO`: Attempt to divide by zero
- `UNDEFINED_VAR`: Using undefined variables
- `TYPE_MISMATCH`: Type compatibility issues
- `INDEX_OUT_OF_RANGE`: Array index out of bounds
- `STACK_OVERFLOW`: Too many nested function calls
- `MEMORY_ERROR`: Out of memory errors

### Function Errors
- `UNDEFINED_FUNCTION`: Calling undefined functions
- `INVALID_ARGUMENTS`: Wrong number of function arguments
- `RECURSION_LIMIT`: Exceeded maximum recursion depth

### Type Errors
- `TYPE_CONVERSION`: Invalid type conversion attempts
- `INVALID_OPERATION`: Invalid operations between types
- `NULL_REFERENCE`: Using uninitialized variables

### IO Errors
- `FILE_NOT_FOUND`: File not found during import/read
- `PERMISSION_DENIED`: No permission to access file
- `IO_ERROR`: General IO operation errors

### Configuration Errors
- `INVALID_KEYWORD`: Invalid keyword configuration
- `DUPLICATE_KEYWORD`: Duplicate keyword definitions
- `INVALID_CONFIG`: General configuration errors

### Import/Module Errors
- `MODULE_NOT_FOUND`: Missing module during import
- `CIRCULAR_IMPORT`: Circular dependencies detected

## Customizing Error Messages

You can customize error messages by adding entries to your `.env` file. Each error type can have its own custom message:

```env
# Example custom error messages
ERROR_SYNTAX_GENERIC="🦆 Oops! Your code has a syntax error at line {line}"
ERROR_UNDEFINED_VAR="🦆 Can't find the variable '{var_name}'. Did it fly away?"
ERROR_TYPE_MISMATCH="🦆 Expected a {expected_type} but got a {actual_type}. Ducks of a feather..."
```

### Available Placeholders

Different error types support different placeholders in their messages:

- `{line}`: Line number (all errors)
- `{column}`: Column number (all errors)
- `{var_name}`: Variable name (UNDEFINED_VAR)
- `{expected_type}`, `{actual_type}`: Type information (TYPE_MISMATCH)
- `{bracket_type}`: Type of bracket (MISSING_BRACKET)
- `{token}`: Invalid token (INVALID_TOKEN)
- `{func_name}`: Function name (UNDEFINED_FUNCTION)
- `{expected}`, `{actual}`: Argument counts (INVALID_ARGUMENTS)
- `{file}`: File path (FILE_NOT_FOUND, PERMISSION_DENIED)
- `{module}`: Module name (MODULE_NOT_FOUND)
- `{details}`: Additional error details (various errors)

## Example Error Messages

Here are some example error messages you might encounter:

### Syntax Error
```
🦆 DuckLang Error: Syntax Error
📍 Line 5, Column 10 in 'example.duck'
❌ [MISSING_BRACKET] Waddle waddle... missing a } at line 5

Code:
  3 | def greet(name) {
  4 |     show("Hello, " + name)
> 5 |     return
  6 | 

💡 Suggestion: Add a closing } to match the opening one.
```

### Runtime Error
```
🦆 DuckLang Error: Runtime Error
📍 Line 12, Column 15 in 'example.duck'
❌ [TYPE_MISMATCH] Expected a duck, but got a goose! Expected number but got string

Code:
  11 | let name = "John"
> 12 | let result = 42 + name
  13 | show(result)
             ^

💡 Suggestion: Convert your string to number before this operation.
```

## Best Practices

1. **Read the Entire Message**: Error messages include the exact location, context, and a suggestion for fixing the issue.

2. **Check the Context**: Look at the code shown around the error line to understand the context.

3. **Follow Suggestions**: Each error comes with a specific suggestion for fixing the issue.

4. **Customize Messages**: Use the `.env` file to customize error messages for your team or preferences.

5. **Use Error Types**: When catching errors in your code, use the specific error types to handle different cases appropriately.

## Error Handling in Code

Here's how to use the error handling system in your code:

```python
from src.error import ErrorHandler

# Initialize the error handler
error_handler = ErrorHandler()

# Set the current file being processed
error_handler.set_current_file(file_content)

try:
    # Your code here
    if some_error_condition:
        error_handler.raise_syntax_error(
            'MISSING_BRACKET',
            line=5,
            column=10,
            file_name='example.duck',
            bracket_type='}'
        )
except DuckLangError as e:
    print(e)  # Will print the formatted error message
```

## Contributing

To add new error types or enhance the error handling system:

1. Add the error type and message to `ErrorConfig.default_messages`
2. Add a corresponding suggestion to `ErrorConfig.suggestions`
3. Update the documentation with the new error type and its placeholders
4. Add test cases to verify the new error handling 