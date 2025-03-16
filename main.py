from src.lexer import Lexer

# Sample source code input
source_code =   """
                    def match(self, text):
        if self.source[self.position.index:self.position.index + len(text)] -> == text:
            for . in range(len(text)):  
                self.advance()
            return True
        return False

                """

# Initialize lexer
lexer = Lexer()
tokens = lexer.tokenize(source_code)

# Print detailed token information
print("\n📝 Token Details:")
if not tokens:
    print("⚠️ No tokens found! Check the lexer implementation or input source code.")
else:
    for token in tokens:
        print(f"🔹 {token}")

# Print a nicely formatted table
print("\n📌 Token Table:")

# Define column widthsa
col_widths = [30, 12, 14, 12, 6, 8]
line_sep = "+" + "+".join(["-" * w for w in col_widths]) + "+"

# Print table header
print(line_sep)
print(f"| {'Type':<20} | {'Value':<12} | {'Start Index':<14} | {'End Index':<12} | {'Line':<6} | {'Column':<8} |")
print(line_sep)

# Print table rows
for token in tokens:
    print(f"| {str(token.token_type):<20} | {str(token.value):<12} | {str(token.start_pos.index):<14} | {str(token.end_pos.index):<12} | {str(token.start_pos.line):<6} | {str(token.start_pos.column):<8} |")

# Print table footer
print(line_sep)
