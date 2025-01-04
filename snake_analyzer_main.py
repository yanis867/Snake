import re
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


from typing import List, Tuple
class Lexer:
    # Define token patterns based on the grammar
    token_patterns = [
        ('DEB_SNK', r'Snk_Begin'), ('FIN_SNK', r'Snk_End'),
        ('ENTIER', r'Snk_Int'), ('REEL', r'Snk_Real'), ('CHAINE', r'Snk_Strg'),
        ('SI', r'If'), ('SINON', r'Else'), ('DEB_SI', r'Begin'), ('FIN_SI', r'End'),
        ('IMPRIMER', r'Snk_Print'), ('SET', r'Set'), ('GET', r'Get'), ('FROM', r'From'),
        ('VIR', r','), ('CRG', r'\['), ('CRD', r'\]'),
        ('OPERATEUR', r'<=|>=|!=|[<>]|=='),
        ('entier', r'[0-9]+'), ('reel', r'[0-9]+\.[0-9]+'),
        ('chaine', r'"[^"]*"'), ('id', r'[a-zA-Z][a-zA-Z0-9]*'),
        ('DEB_C', r'\#\#'), ('FIN_I', r'\#'),
        ('tout', r'.+')


class Parser:
    def __init__(self, tokens: List[Tuple[str, str, int]]):
        self.tokens = tokens
        self.current_index = 0

    def current_token(self) -> Tuple[str, str, int]:
        return self.tokens[self.current_index] if self.current_index < len(self.tokens) else ("EOF", "", 0)

    def advance(self):
        self.current_index += 1

    def parse(self):
        results = []
        while self.current_token()[0] != "EOF":
            results.append(self.statement())
        return results

    def statement(self):
        token_type, token_value, line_number = self.current_token()
        if token_type == "DEB_SNK":
            self.advance()
            return "Program Start"
        elif token_type == "FIN_SNK":
            self.advance()
            return "Program End"
        elif token_type == "IMPRIMER":
            return self.print_statement()
        else:
            raise SyntaxError(f"Unexpected token {token_value} at line {line_number}")

    def print_statement(self):
        token_type, token_value, line_number = self.current_token()
        if token_type == "IMPRIMER":
            self.advance()
            return f"Print"
        else:
            raise SyntaxError(f"Expected 'IMPRIMER', got {token_value} at line {line_number}")

    def tokenize(self, code):
        """Tokenizes the input code based on the defined patterns."""
        tokens = []
        line_number = 1
        index = 0

        while index < len(code):
            match = None
            for token_type, pattern in self.token_patterns:
                regex = re.compile(r'^\s*' + pattern)  # Match from the start with whitespace tolerance
                match = regex.match(code[index:])
                if match:
                    value = match.group().strip()
                    tokens.append((token_type, value, line_number))
                    index += len(match.group())
                    break

            if not match:  # No token matched
                tokens.append(("ERROR", code[index], line_number))
                index += 1

            # Check for newlines
            if '\n' in code[index - len(match.group()):index]:
                line_number += 1

        return tokens

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Analyseur Snake")
        self.geometry("680x770")
        self.resizable(False, False)

        # Panel for file selection
        self.selection_fichier = ttk.Frame(self)
        self.selection_fichier.place(x=10, y=10, width=664, height=90)

        self.btn_charger = ttk.Button(self.selection_fichier, text="Charger un fichier", command=self.charger_fichier)
        self.btn_charger.pack(side=tk.LEFT, padx=5, pady=5)

        self.text_field = ttk.Entry(self.selection_fichier, width=50)
        self.text_field.pack(side=tk.LEFT, padx=5, pady=5)

        # Panel for analysis
        self.analyse = ttk.Frame(self)
        self.analyse.place(x=10, y=111, width=664, height=639)

        self.tab_control = ttk.Notebook(self.analyse)
        self.tab_control.place(x=10, y=10, width=642, height=573)

        self.tab_lexicale = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_lexicale, text="Analyse Lexicale")
        self.scroll_lexicale = ttk.Scrollbar(self.tab_lexicale)
        self.scroll_lexicale.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_lexicale = tk.Text(self.tab_lexicale, wrap=tk.WORD, yscrollcommand=self.scroll_lexicale.set,
                                     state=tk.DISABLED)
        self.text_lexicale.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
        self.scroll_lexicale.config(command=self.text_lexicale.yview)

        self.tab_syntaxique = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_syntaxique, text="Analyse Syntaxique")
        self.scroll_syntaxique = ttk.Scrollbar(self.tab_syntaxique)
        self.scroll_syntaxique.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_syntaxique = tk.Text(self.tab_syntaxique, wrap=tk.WORD, yscrollcommand=self.scroll_syntaxique.set,
                                       state=tk.DISABLED)
        self.text_syntaxique.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
        self.scroll_syntaxique.config(command=self.text_syntaxique.yview)

        self.tab_semantique = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_semantique, text="Analyse Sémantique")
        self.scroll_semantique = ttk.Scrollbar(self.tab_semantique)
        self.scroll_semantique.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_semantique = tk.Text(self.tab_semantique, wrap=tk.WORD, yscrollcommand=self.scroll_semantique.set,
                                       state=tk.DISABLED)
        self.text_semantique.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
        self.scroll_semantique.config(command=self.text_semantique.yview)

        self.btn_analyser = ttk.Button(self.analyse, text="Analyser", command=self.analyser)
        self.btn_analyser.place(x=516, y=595, width=136, height=33)

        self.file_content = ""  # To store file content

    def charger_fichier(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.text_field.delete(0, tk.END)
            self.text_field.insert(0, file_path)

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.file_content = file.read()
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier: {e}")

    def analyser(self):
        if self.file_content:
            # Lexical Analysis
            lexer = Lexer()
            tokens = lexer.tokenize(self.file_content)
            lexical_output = "\n".join([f"{t[0]}: {t[1]} (Line {t[2]})" for t in tokens])
            self.text_lexicale.config(state=tk.NORMAL)
            self.text_lexicale.delete(1.0, tk.END)
            self.text_lexicale.insert(tk.END, lexical_output)
            self.text_lexicale.config(state=tk.DISABLED)

            # Syntax Analysis
            try:
                self.parser = Parser(tokens)
                syntax_results = self.parser.parse()
                syntax_output = "\n".join(syntax_results)
            except SyntaxError as e:
                syntax_output = f"Syntax Error: {str(e)}"

            self.text_syntaxique.config(state=tk.NORMAL)
            self.text_syntaxique.delete(1.0, tk.END)
            self.text_syntaxique.insert(tk.END, syntax_output)
            self.text_syntaxique.config(state=tk.DISABLED)

self.parser = None

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()