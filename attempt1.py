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
t_SI = r'If'
t_SINON = r'Else'
t_DEB_SI = r'Begin'
t_FIN_SI = r'End'
t_IMPRIMER = r'Snk_Print'
t_DEB_SNK = r'Snk_Begin'
t_FIN_SNK = r'Snk_End'
t_ENTIER = r'Snk_Int'
t_REEL = r'Snk_Real'
t_CHAINE = r'Snk_Strg'
t_SET = r'Set'
t_GET = r'Get'
t_FROM = r'From'
t_ignore = ' \t'


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

# Build the lexer
lexer = lex.lex()

# Build the parser
parser = yacc.yacc()

# Testing the parser
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if s:
        parser.parse(s)
