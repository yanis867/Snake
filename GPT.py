import ply.lex as lex

# Liste des mots-clés avec leur type de token
keywords = {
    'Snk_Begin': 'DEB_SNK',
    'Snk_End': 'FIN_SNK',
    'Snk_Int': 'ENTIER',
    'Snk_Real': 'REEL',
    'Snk_Strg': 'CHAINE',
    'Set': 'SET',
    'Get': 'GET',
    'From': 'FROM',
    'Snk_Print': 'IMPRIMER',
    'If': 'SI',
    'Else': 'SINON',
    'Begin': 'DEB_SI',
    'End': 'FIN_SI',
}

# Liste des tokens
tokens = list(keywords.values()) + [
    'id', 'entier', 'reel', 'chaine',
    'VIR', 'CRG', 'CRD', 'OPERATEUR'
]

# Règles des tokens fixes (mots-clés et symboles)
t_VIR = r','
t_CRG = r'\['
t_CRD = r'\]'
t_OPERATEUR = r'<=|>=|!=|==|<|>'

# Ignorer les espaces et les tabulations
t_ignore = ' \t'

# Règles pour les types de données
def t_entier(t):
    r'[0-9]+'
    t.value = int(t.value)  # Convertir en entier
    return t

def t_reel(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)  # Convertir en réel
    return t

def t_chaine(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Supprimer les guillemets
    return t

# Règle pour les identificateurs et les mots-clés
def t_id(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = keywords.get(t.value, 'id')  # Vérifie si c'est un mot-clé
    return t

# Règle pour gérer les nouvelles lignes
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Gestion des erreurs
def t_error(t):
    print(f"Caractère invalide : {t.value[0]} à la ligne {t.lexer.lineno}")
    t.lexer.skip(1)

# Construction de l'analyseur lexical
lexer = lex.lex()

# Exemple de test
if __name__ == "__main__":
    data = '''
    Snk_Begin
    Snk_Int x, y
    Set x 10
    If [x > y]
    Begin
        Snk_Print x
    End
    Snk_End
    '''
    lexer.input(data)

    # Analyse lexicale
    print("Tokens générés :")
    for token in lexer:
        print(token)

lexer = lex.lex()
