import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import ply.lex as lex
import ply.yacc as yacc

# List of token names
tokens = (
    'newline', 'id', 'entier', 'reel', 'chaine',
    'commentaire', 'FIN_I', 'SI', 'SINON', 'DEB_SI',
    'FIN_SI', 'IMPRIMER', 'DEB_SNK', 'FIN_SNK',
    'ENTIER', 'REEL', 'CHAINE', 'SET', 'GET',
    'FROM', 'VIR', 'CRG', 'CRD', 'OPERATEUR',
)

# Regular expression rules for simple tokens
t_id = r'[a-zA-Z][a-zA-Z0-9]*'
t_entier = r'[0-9]+'
t_reel = r'[0-9]+\.[0-9]+'
t_chaine = r'"[^"]*"'
t_VIR = r','
t_CRG = r'\['
t_CRD = r'\]'
t_OPERATEUR = r'<=|>=|!=|==|<|>'
t_commentaire = r'\#\#.*'
t_FIN_I = r'\#'
t_ignore = ' \t'

def t_DEB_SNK(t):
    r'Snk_Begin'
    return t

def t_FIN_SNK(t):
    r'Snk_End'
    return t
def t_IMPRIMER(t):
    r'Snk_Print'
    return t
    return t
def t_ENTIER(t):
    r'Snk_Int'
    return t
def t_EEEL(t):
    r'Snk_Real'
    return t
def t_CHAINE(t):
    r'Snk_Strg'
    return t
def t_SET(t):
    r'Set'
    return t
def t_GET(t):
    r'Get'
    return t
def t_FROM(t):
    r'From'
    return t
def t_SI(t):
    r'If'
    return t
def t_SINON(t):
    r'Else'
    return t
def t_DEB_SI(t):
    r'Begin'
    return t
def t_FIN_SI(t):
    r'End'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Define a rule for each production rule
def p_S(p):
    '''S : DEB_SNK newline Code FIN_SNK
         |'''
    pass
def p_Code(p):
    '''Code : Instructions newline Code
            |'''

def p_Instructions(p):
    '''Instructions :  Declaration FIN_I
                    | Affectation FIN_I
                    | Affichage FIN_I
                    | commentaire
                    | Condition'''
    pass

def p_Declaration(p):
    '''Declaration : ENTIER Ids
                   | REEL Ids
                   | CHAINE Ids'''
    pass

def p_Ids(p):
    '''Ids : id VIR Ids
           | id'''
    pass

def p_Affectation(p):
    '''Affectation : SET id entier
                   | SET id reel
                   | GET id FROM id'''
    pass

def p_Affichage(p):
    '''Affichage : IMPRIMER Ids
                 | IMPRIMER chaine'''
    pass
def p_Condition(p):
    '''Condition : Si
                 | Si Sinon'''
    pass

def p_Si(p):
    '''Si : SI CRG Comparaison CRD newline CodeSi'''
    pass

def p_CodeSi(p):
    '''CodeSi : DEB_SI newline Code FIN_SI'''
    pass
def p_Sinon(p):
    '''Sinon : SINON newline CodeSi'''

def p_Comparaison(p):
    '''Comparaison : Operande OPERATEUR Operande'''
    pass

def p_Operande(p):
    '''Operande : id
                | entier
                | reel
                | chaine'''

# Error rule for syntax errors
def p_error(p):
    print("Erreur syntaxique !")

root = tk.Tk()
root.title("Analyseur Snake")
root.geometry("680x770")
root.resizable(False, False)

file_content = ""

# Panel for file selection
selection_fichier = ttk.Frame(root)
selection_fichier.place(x=10, y=10, width=664, height=90)

def charger_fichier():
    global file_content
    file_path = filedialog.askopenfilename()
    if file_path:
        text_field.delete(0, tk.END)
        text_field.insert(0, file_path)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier: {e}")

btn_charger = ttk.Button(selection_fichier, text="Charger un fichier", command=charger_fichier)
btn_charger.pack(side=tk.LEFT, padx=5, pady=5)

text_field = ttk.Entry(selection_fichier, width=50)
text_field.pack(side=tk.LEFT, padx=5, pady=5)

# Panel for analysis
analyse = ttk.Frame(root)
analyse.place(x=10, y=111, width=664, height=639)

tab_control = ttk.Notebook(analyse)
tab_control.place(x=10, y=10, width=642, height=573)

tab_code_source = ttk.Frame(tab_control)
tab_control.add(tab_code_source, text="Code Source")
scroll_code_source = ttk.Scrollbar(tab_code_source)
scroll_code_source.pack(side=tk.RIGHT, fill=tk.Y)
text_code_source = tk.Text(tab_code_source, wrap=tk.WORD, yscrollcommand=scroll_code_source.set)
text_code_source.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
scroll_code_source.config(command=text_code_source.yview)

tab_lexicale = ttk.Frame(tab_control)
tab_control.add(tab_lexicale, text="Analyse Lexicale")
scroll_lexicale = ttk.Scrollbar(tab_lexicale)
scroll_lexicale.pack(side=tk.RIGHT, fill=tk.Y)
text_lexicale = tk.Text(tab_lexicale, wrap=tk.WORD, yscrollcommand=scroll_lexicale.set, state=tk.DISABLED)
text_lexicale.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
scroll_lexicale.config(command=text_lexicale.yview)

tab_syntaxique = ttk.Frame(tab_control)
tab_control.add(tab_syntaxique, text="Analyse Syntaxique")
scroll_syntaxique = ttk.Scrollbar(tab_syntaxique)
scroll_syntaxique.pack(side=tk.RIGHT, fill=tk.Y)
text_syntaxique = tk.Text(tab_syntaxique, wrap=tk.WORD, yscrollcommand=scroll_syntaxique.set, state=tk.DISABLED)
text_syntaxique.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
scroll_syntaxique.config(command=text_syntaxique.yview)

tab_semantique = ttk.Frame(tab_control)
tab_control.add(tab_semantique, text="Analyse Sémantique")
scroll_semantique = ttk.Scrollbar(tab_semantique)
scroll_semantique.pack(side=tk.RIGHT, fill=tk.Y)
text_semantique = tk.Text(tab_semantique, wrap=tk.WORD, yscrollcommand=scroll_semantique.set, state=tk.DISABLED)
text_semantique.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
scroll_semantique.config(command=text_semantique.yview)

def analyser():
    global file_content
    if file_content:
        # Initialize the lexer
        lexer = lex.lex()
        lexer.input(file_content)
        
        # Perform lexical analysis
        text_code_source.delete(1.0, tk.END)
        text_code_source.insert(tk.END, file_content)
        
        text_lexicale.config(state=tk.NORMAL)
        text_lexicale.delete(1.0, tk.END)
        try:
            tokens = []
            while tok := lexer.token():
                tokens.append(f"Line {tok.lineno}: {tok.type}({tok.value})")
            text_lexicale.insert(tk.END, "\n".join(tokens))
        except Exception as e:
            text_lexicale.insert(tk.END, f"Lexer Error: {e}")
        text_lexicale.config(state=tk.DISABLED)
        
        # Initialize the parser
        parser = yacc.yacc()
        
        # Perform syntax analysis
        text_syntaxique.config(state=tk.NORMAL)
        text_syntaxique.delete(1.0, tk.END)
        try:
            parse_result = parser.parse(input=file_content, lexer=lexer)
            text_syntaxique.insert(tk.END, "Syntax Analysis Completed Successfully!\n")
            text_syntaxique.insert(tk.END, f"Parse Result: {parse_result}")
        except Exception as e:
            text_syntaxique.insert(tk.END, f"Syntax Error: {e}")
        text_syntaxique.config(state=tk.DISABLED)
        
        # Placeholder for semantic analysis
        text_semantique.config(state=tk.NORMAL)
        text_semantique.delete(1.0, tk.END)
        text_semantique.insert(tk.END, "Semantic Analysis Not Implemented.")
        text_semantique.config(state=tk.DISABLED)

btn_analyser = ttk.Button(analyse, text="Analyser", command=analyser)
btn_analyser.place(x=516, y=595, width=136, height=33)

root.mainloop()
