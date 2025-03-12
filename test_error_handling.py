import sys
from src.error import ErrorHandler, DuckLangError

def test_error_handling():
    test_cases = [
        # Syntax Errors
        {
            'name': 'Basic Syntax Error',
            'code': 'def test() { x = 5 + }',
            'expected_type': 'Syntax Error',
            'error_key': 'SYNTAX_GENERIC',
            'raise_func': 'raise_syntax_error'
        },
        {
            'name': 'Missing Bracket',
            'code': 'when x > 0 { show("test")',
            'expected_type': 'Syntax Error',
            'error_key': 'MISSING_BRACKET',
            'raise_func': 'raise_syntax_error',
            'kwargs': {'bracket_type': '}'}
        },
        {
            'name': 'Invalid Token',
            'code': 'let @invalid = 5',
            'expected_type': 'Syntax Error',
            'error_key': 'INVALID_TOKEN',
            'raise_func': 'raise_syntax_error',
            'kwargs': {'token': '@'}
        },
        
        # Runtime Errors
        {
            'name': 'Undefined Variable',
            'code': 'show(undefinedVariable)',
            'expected_type': 'Runtime Error',
            'error_key': 'UNDEFINED_VAR',
            'raise_func': 'raise_runtime_error',
            'kwargs': {'var_name': 'undefinedVariable'}
        },
        {
            'name': 'Type Mismatch',
            'code': 'let x = "hello" + 5',
            'expected_type': 'Runtime Error',
            'error_key': 'TYPE_MISMATCH',
            'raise_func': 'raise_runtime_error',
            'kwargs': {'expected_type': 'number', 'actual_type': 'string'}
        },
        {
            'name': 'Division by Zero',
            'code': 'let x = 10 / 0',
            'expected_type': 'Runtime Error',
            'error_key': 'DIVISION_BY_ZERO',
            'raise_func': 'raise_runtime_error'
        },
        {
            'name': 'Index Out of Range',
            'code': 'let arr = [1, 2, 3]; show(arr[5])',
            'expected_type': 'Runtime Error',
            'error_key': 'INDEX_OUT_OF_RANGE',
            'raise_func': 'raise_runtime_error',
            'kwargs': {'index': 5, 'max_index': 2}
        },
        
        # Function Errors
        {
            'name': 'Undefined Function',
            'code': 'nonexistent_func()',
            'expected_type': 'Function Error',
            'error_key': 'UNDEFINED_FUNCTION',
            'raise_func': 'raise_function_error',
            'kwargs': {'func_name': 'nonexistent_func'}
        },
        {
            'name': 'Invalid Arguments',
            'code': 'def add(a, b) {} add(1)',
            'expected_type': 'Function Error',
            'error_key': 'INVALID_ARGUMENTS',
            'raise_func': 'raise_function_error',
            'kwargs': {'expected': 2, 'actual': 1}
        },
        
        # Type Errors
        {
            'name': 'Type Conversion Error',
            'code': 'let x = "hello" as number',
            'expected_type': 'Type Error',
            'error_key': 'TYPE_CONVERSION',
            'raise_func': 'raise_type_error',
            'kwargs': {'from_type': 'string', 'to_type': 'number'}
        },
        {
            'name': 'Invalid Operation',
            'code': 'let x = true * 5',
            'expected_type': 'Type Error',
            'error_key': 'INVALID_OPERATION',
            'raise_func': 'raise_type_error',
            'kwargs': {'operation': 'multiply', 'type1': 'boolean', 'type2': 'number'}
        },
        
        # IO Errors
        {
            'name': 'File Not Found',
            'code': 'import "nonexistent.duck"',
            'expected_type': 'IO Error',
            'error_key': 'FILE_NOT_FOUND',
            'raise_func': 'raise_io_error',
            'kwargs': {'file': 'nonexistent.duck'}
        },
        {
            'name': 'Permission Denied',
            'code': 'import "/root/secret.duck"',
            'expected_type': 'IO Error',
            'error_key': 'PERMISSION_DENIED',
            'raise_func': 'raise_io_error',
            'kwargs': {'file': '/root/secret.duck'}
        }
    ]
    
    error_handler = ErrorHandler()
    
    print("🦆 Running DuckLang Error Handler Tests")
    print("======================================")
    
    passed = 0
    total = len(test_cases)
    
    for test in test_cases:
        print(f"\nTesting: {test['name']}")
        print("-" * (9 + len(test['name'])))
        
        try:
            error_handler.set_current_file(test['code'])
            kwargs = test.get('kwargs', {})
            kwargs.update({
                'line': 1,
                'column': 0,
                'file_name': 'test.duck'
            })
            
            # Call the appropriate error raising function
            if hasattr(error_handler, test['raise_func']):
                getattr(error_handler, test['raise_func'])(
                    test['error_key'],
                    **kwargs
                )
                
        except DuckLangError as e:
            print(e)
            print("\nTest Result: ", end="")
            
            # Check if both error type and message are correct
            error_type_correct = test['expected_type'] in str(e)
            error_key_correct = test['error_key'].lower() in str(e).lower()
            suggestion_present = e.suggestion is not None
            
            if error_type_correct and error_key_correct and suggestion_present:
                print("✅ Passed")
                passed += 1
            else:
                print("❌ Failed")
                if not error_type_correct:
                    print(f"Expected error type '{test['expected_type']}' not found in message")
                if not error_key_correct:
                    print(f"Expected error key '{test['error_key']}' not found in message")
                if not suggestion_present:
                    print("No suggestion provided for the error")
                
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            print("\nTest Result: ❌ Failed")
    
    print("\n======================================")
    print(f"Final Results: {passed}/{total} tests passed")
    if passed == total:
        print("🎉 All tests passed!")
    else:
        print(f"😢 {total - passed} tests failed")
    print("======================================")

if __name__ == "__main__":
    test_error_handling() 