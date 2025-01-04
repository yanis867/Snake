import ply.lex as lex

tokens = (
    'int',
    'operand',
    'equals'
)

t_operand = r'[-+\/*]'
t_equals = r'='

def t_int(t):
    r"""[0-9]+"""
    t.value = int(t.value)
    return t

def t_error(t):
    print("caractère illégal : '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#-----------------------------------

data = '1+1=2ghf'

lexer.input(data)

for tok in lexer:
    print(tok.type+' '+str(tok.value))
