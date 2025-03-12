# DuckLang Programming Language Documentation

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Language Customization](#language-customization)
- [Basic Syntax](#basic-syntax)
- [Data Types](#data-types)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Examples](#examples)
- [Configuration Guide](#configuration-guide)
- [Error Handling](#error-handling)

## Introduction

DuckLang is a flexible, customizable programming language that allows users to define their own keywords and syntax elements through configuration. This makes it ideal for educational purposes, localization, and creating domain-specific language variants.

## Getting Started

### Running DuckLang Programs
To run a DuckLang program:

1. Save your code with the `.duck` extension (e.g., `program.duck`)
2. Open a terminal in the project directory
3. Run the following command:
```bash
python main.py your_program.duck
```

For example:
```bash
# Running a simple program
python main.py hello.duck

# Running with custom keywords (make sure .env is configured)
python main.py custom_program.duck
```

## Language Customization

### Customizable Keywords
All keywords in Duck can be customized through a `.env` file. Here are the default keywords and their customizable environment variables:

| Default Keyword | Environment Variable | Purpose |
|----------------|---------------------|---------|
| `print` | `KEYWORD_PRINT` | Output command |
| `if` | `KEYWORD_IF` | Conditional statement |
| `else` | `KEYWORD_ELSE` | Alternative condition |
| `while` | `KEYWORD_WHILE` | Loop construct |
| `for` | `KEYWORD_FOR` | Iteration construct |
| `function` | `KEYWORD_FUNCTION` | Function definition |
| `return` | `KEYWORD_RETURN` | Function return |
| `break` | `KEYWORD_BREAK` | Loop termination |
| `continue` | `KEYWORD_CONTINUE` | Skip loop iteration |
| `and` | `KEYWORD_AND` | Logical AND |
| `or` | `KEYWORD_OR` | Logical OR |
| `not` | `KEYWORD_NOT` | Logical NOT |
| `true` | `KEYWORD_TRUE` | Boolean true |
| `false` | `KEYWORD_FALSE` | Boolean false |
| `none` | `KEYWORD_NONE` | Null value |
| `var` | `KEYWORD_VAR` | Variable declaration |

### Example Configuration
```env
KEYWORD_PRINT=show
KEYWORD_IF=when
KEYWORD_ELSE=otherwise
KEYWORD_WHILE=repeat
KEYWORD_FUNCTION=def
KEYWORD_RETURN=give
```

## Basic Syntax

### Statement Separation
Statements in Duck are separated by newlines. Semicolons are not required or used as statement separators.

```python
# Correct way
var x = 5
print(x)

# Not needed (but will work)
var x = 5;
print(x);
```

### Variables
```python
# Variable declaration
var x = 5        # Default syntax
let x = 5        # With KEYWORD_VAR=let

# Variable update (no 'var' keyword needed)
x = 10          # Updating existing variable
```

### Output
```python
print("Hello")   # Default syntax
show("Hello")    # With KEYWORD_PRINT=show
```

### Comments
```python
# Single line comment
```

## Data Types

Duck supports the following data types:

### Primitive Types
- Numbers (integers and floating-point)
- Strings (text enclosed in quotes)
- Booleans (`true`/`false` or customized values)
- None (`none` or customized value)

### Complex Types
- Arrays: `[1, 2, 3]`
- Functions

### Type Examples
```python
# Numbers
var num = 42
var float_num = 3.14

# Strings
var text = "Hello, World!"

# Booleans
var flag = true    # Default
var flag = yes     # With KEYWORD_TRUE=yes

# Arrays
var numbers = [1, 2, 3, 4, 5]
```

## Control Flow

### Conditional Statements
```python
# Default syntax
if x > 0 {
    print("Positive")
} else {
    print("Non-positive")
}

# Customized syntax (with configured keywords)
when x > 0 {
    show("Positive")
} otherwise {
    show("Non-positive")
}
```

### Loops
```python
# While loop (default)
while x > 0 {
    print(x)
    x = x - 1
}

# While loop (customized)
repeat x > 0 {
    show(x)
    x = x - 1
}
```

## Functions

### Function Definition
```python
# Default syntax
function factorial(n) {
    if n <= 1 {
        return 1
    }
    return n * factorial(n - 1)
}

# Customized syntax
def factorial(n) {
    when n <= 1 {
        give 1
    }
    give n * factorial(n - 1)
}
```

### Function Calls
```python
var result = factorial(5)
```

## Examples

### Complete Program Example (Default Syntax)
```python
function factorial(n) {
    if n < 0 {
        return 0
    }
    if n <= 1 {
        return 1
    }
    return n * factorial(n - 1)
}

var numbers = [1, 2, 3, 4, 5]
print("Computing factorials:")

for num in numbers {
    print(factorial(num))
}
```

### Same Program with Custom Keywords
```python
def factorial(n) {
    when n < 0 {
        give 0
    }
    when n <= 1 {
        give 1
    }
    give n * factorial(n - 1)
}

let numbers = [1, 2, 3, 4, 5]
show("Computing factorials:")

loop num in numbers {
    show(factorial(num))
}
```

## Configuration Guide

### Setting Up Custom Keywords

1. Create a `.env` file in your project root
2. Define your custom keywords:
```env
KEYWORD_PRINT=show
KEYWORD_IF=when
KEYWORD_ELSE=otherwise
KEYWORD_WHILE=repeat
KEYWORD_FOR=loop
KEYWORD_FUNCTION=def
KEYWORD_RETURN=give
KEYWORD_BREAK=stop
KEYWORD_CONTINUE=skip
KEYWORD_AND=also
KEYWORD_OR=either
KEYWORD_NOT=negate
KEYWORD_TRUE=yes
KEYWORD_FALSE=no
KEYWORD_NONE=nothing
KEYWORD_VAR=let
```

### Configuration Rules
- Keywords must be unique
- Keywords cannot contain spaces
- Keywords are case-insensitive
- Keywords cannot be special characters used by the language (like operators)

## Error Handling

DuckLang provides a robust and customizable error handling system. Errors can be customized through the `.env` file, allowing you to set your own error messages while maintaining helpful debugging information.

### Error Types

1. **Syntax Errors**
   - Invalid token sequences
   - Missing brackets or parentheses
   - Incorrect indentation
   - Unknown keywords

2. **Runtime Errors**
   - Division by zero
   - Undefined variables
   - Type mismatches
   - Stack overflow
   - Invalid function calls

3. **Configuration Errors**
   - Invalid keyword definitions
   - Duplicate keywords
   - Missing required configurations

### Customizing Error Messages

Error messages can be customized in your `.env` file:

```env
# Syntax Errors
ERROR_SYNTAX_GENERIC="Oops! Something's not quite right at line {line}"
ERROR_MISSING_BRACKET="Hey! You forgot a {bracket_type} at line {line}"
ERROR_INVALID_TOKEN="Unexpected {token} at line {line}"

# Runtime Errors
ERROR_DIVISION_BY_ZERO="Division by zero? That's infinitely bad!"
ERROR_UNDEFINED_VAR="Can't find '{var_name}'. Did it fly away?"
ERROR_TYPE_MISMATCH="Expected {expected_type} but got {actual_type}"

# Configuration Errors
ERROR_INVALID_KEYWORD="'{keyword}' isn't a valid keyword name"
ERROR_DUPLICATE_KEYWORD="'{keyword}' is already used for {existing_use}"
```

### Error Message Format

Each error message can include placeholders for dynamic information:
- `{line}` - Line number
- `{column}` - Column number
- `{token}` - The problematic token
- `{expected}` - Expected value/type
- `{actual}` - Actual value/type
- `{file}` - File name

### Default Fun Error Messages

If no custom error messages are defined, DuckLang uses these quirky fallbacks:

```python
# Syntax Errors
"Quack! Your code seems a bit scrambled at line {line}"
"Waddle waddle... can't parse that!"
"This syntax makes me want to duck for cover!"

# Runtime Errors
"Your code took a wrong turn at the duck pond"
"That operation is like dividing by zero ducks... impossible!"
"This variable seems to have flown south for the winter"

# Type Errors
"Expected a duck, but got a goose!"
"These types don't flock together"
```

### Error Output Format

Errors are displayed in a clear, structured format:

```
🦆 DuckLang Error: Type Mismatch
📍 Line 42, Column 10 in 'example.duck'
❌ Expected number but got string

Code:
   41 | var x = 5
-> 42 | x = "hello"
   43 | print(x)

Custom Message: These types don't flock together!
Suggestion: Try converting "hello" to a number first
```

### Error Handling Best Practices

1. **Clear Messages**
   - Use descriptive but concise messages
   - Include relevant variable/function names
   - Provide suggestions when possible

2. **Consistent Format**
   - Always include line numbers
   - Show the problematic code snippet
   - Provide a suggestion if applicable

3. **Custom Messages**
   - Keep messages user-friendly
   - Use appropriate technical terms
   - Maintain helpful context

4. **Configuration**
   - Back up default error messages
   - Test custom messages thoroughly
   - Keep messages language-appropriate

### Example Error Configurations

Here's a complete example of custom error messages:

```env
# Professional Style
ERROR_SYNTAX="Syntax Error: Invalid syntax at line {line}"
ERROR_TYPE="Type Error: Cannot perform {operation} with {type1} and {type2}"
ERROR_NAME="Name Error: '{name}' is not defined in current scope"

# Fun Style
ERROR_SYNTAX="Quack Attack! Code went wonky at line {line}"
ERROR_TYPE="These types are like oil and water, they don't mix!"
ERROR_NAME="Looks like '{name}' took a swim and never came back"

# Educational Style
ERROR_SYNTAX="Let's check the syntax at line {line}. Remember: {rule}"
ERROR_TYPE="Hint: {type1} operations can't work with {type2} values"
ERROR_NAME="'{name}' hasn't been created yet. Did you forget to declare it?"
```

## Development Status

The Duck programming language is under active development. Current features:
- ✓ Customizable keywords
- ✓ Basic arithmetic operations
- ✓ Control flow statements
- ✓ Functions
- ✓ Arrays
- ✓ Variable declarations

Future enhancements may include:
- Custom operator definitions
- Additional data types
- Module system
- Standard library
- More customization options

