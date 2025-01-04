import re
from tkinter import Tk, filedialog, Button, Text, END

# Lexer
KEYWORDS = ["Snk_Begin", "Snk_End", "Snk_Int", "Snk_Real", "Snk_Strg", "Set", "If", "Else", "Begin", "End", "Get", "from", "Snk_Print"]
TOKEN_SPECIFICATION = [
    ('KEYWORD', r'|'.join(KEYWORDS)),
    ('IDENTIFIER', r'[a-zA-Z][a-zA-Z0-9]*'),
    ('NUMBER', r'\d+(\.\d+)?'),
    ('STRING', r'\".*?\"'),
    ('OPERATOR', r'[<>=]'),
    ('CONDITION_START', r'\['),
    ('CONDITION_END', r'\]'),
    ('SEPARATOR', r'[,:]'),
    ('END_STATEMENT', r'#'),
    ('COMMENT', r'##.*'),
    ('WHITESPACE', r'[ \t]+'),
    ('NEWLINE', r'\n'),
    ('MISMATCH', r'.'),
]
TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)

def tokenize(code):
    tokens = []
    for match in re.finditer(TOKEN_REGEX, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'WHITESPACE' or kind == 'COMMENT':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unexpected token: {value}')
        tokens.append((kind, value))
    return tokens

# Parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def match(self, expected):
        if self.pos < len(self.tokens) and self.tokens[self.pos][1] == expected:
            self.pos += 1
            return True
        return False

    def expect(self, expected):
        if self.pos >= len(self.tokens):
            raise SyntaxError(f"Expected {expected} but got end of file")
        if not self.match(expected):
            if self.pos < len(self.tokens):
                raise SyntaxError(f'Expected {expected} but got {self.tokens[self.pos][0]}')
            else:
                raise SyntaxError(f'Expected {expected} but got end of file')

    def parse(self):
        self.expect("Snk_Begin")
        while self.pos < len(self.tokens):
            if self.match("Snk_End"):
                break
            self.statement()
        if not self.match("Snk_End"):
            raise SyntaxError("Expected Snk_End at the end of the file")

    def statement(self):
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] == "NEWLINE":
            self.pos += 1

        if self.pos >= len(self.tokens):
            return

        if self.match("Snk_Int") or self.match("Snk_Real") or self.match("Snk_Strg"):
            self.declaration()
        elif self.match("Set"):
            self.assignment()
        elif self.match("If"):
            self.if_statement()
        elif self.match("Snk_Print"):
            self.print_statement()
        elif self.match("Else"):
            pass
        elif self.match("Begin"):
            pass
        elif self.match("End"):
            pass
        else:
            if self.pos < len(self.tokens):
                raise SyntaxError(f'Unknown statement at {self.tokens[self.pos]}')
            else:
                raise SyntaxError("Unexpected end of file")

    def declaration(self):
        self.expect("IDENTIFIER")
        while self.match("SEPARATOR"):
            self.expect("IDENTIFIER")
        self.expect("END_STATEMENT")

    def assignment(self):
        self.expect("IDENTIFIER")
        self.expect("NUMBER")
        self.expect("END_STATEMENT")

    def if_statement(self):
        self.expect("CONDITION_START")
        self.expression()
        self.expect("CONDITION_END")
        while not self.match("Else") and not self.match("End") and self.pos < len(self.tokens):
            self.statement()

    def print_statement(self):
        while self.match("IDENTIFIER") or self.match("STRING"):
            self.match(",")
        self.expect("END_STATEMENT")

    def expression(self):
        self.expect("IDENTIFIER")
        self.expect("OPERATOR")
        self.expect("NUMBER")

# Semantic Analyzer
class SemanticAnalyzer:
    def __init__(self):
        self.symbols = set()

    def analyze(self, tokens):
        i = 0
        while i < len(tokens):
            kind, value = tokens[i]
            if kind == 'KEYWORD' and value in ['Snk_Int', 'Snk_Real', 'Snk_Strg']:
                i += 1
                while i < len(tokens) and tokens[i][0] == 'IDENTIFIER':
                    self.symbols.add(tokens[i][1])
                    i += 1
                    if i < len(tokens) and tokens[i][0] == 'SEPARATOR':
                        i += 1
            elif kind == 'IDENTIFIER' and value not in self.symbols:
                raise NameError(f'Undefined variable: {value}')
            i += 1

# GUI Application
def run_gui():
    def load_file():
        filepath = filedialog.askopenfilename(filetypes=[("Snake Files", "*.snk")])
        if filepath:
            with open(filepath, 'r') as file:
                code = file.read()
                code_text.delete("1.0", END)
                code_text.insert(END, code)

    def analyze(action):
        try:
            code = code_text.get("1.0", END)
            tokens = tokenize(code)
            if action == "Lexical":
                output_text.delete("1.0", END)
                output_text.insert(END, "Lexical analysis:\n")
                output_text.insert(END, "\n".join(map(str, tokens)))
            elif action == "Syntax":
                parser = Parser(tokens)
                parser.parse()
                output_text.delete("1.0", END)
                output_text.insert(END, "Syntax analysis successful!")
            elif action == "Semantic":
                analyzer = SemanticAnalyzer()
                analyzer.analyze(tokens)
                output_text.delete("1.0", END)
                output_text.insert(END, "Semantic analysis successful!")
        except Exception as e:
            output_text.delete("1.0", END)
            output_text.insert(END, str(e))

    root = Tk()
    root.title("Snake Compiler")

    Button(root, text="Load File", command=load_file).pack()
    Button(root, text="Lexical Analysis", command=lambda: analyze("Lexical")).pack()
    Button(root, text="Syntax Analysis", command=lambda: analyze("Syntax")).pack()
    Button(root, text="Semantic Analysis", command=lambda: analyze("Semantic")).pack()

    code_text = Text(root, height=15, width=50)
    code_text.pack()

    output_text = Text(root, height=15, width=50)
    output_text.pack()

    root.mainloop()

if __name__ == "__main__":
    run_gui()