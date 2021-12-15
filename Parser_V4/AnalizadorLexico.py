"""
Garcia Dominguez Agueda Hazel
Castillo Zavala Angel Mauricio
"""
import ply.lex as lex

# 1) Lista de palabras reservadas
reserved = {
    'let': 'LET',
    'in': 'IN',
    'endlet': 'ENDLET',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'endif': 'ENDIF'
}

# 2) Lista de tokens
tokens = [
             'ID',
             'PTCOMA',
             'PARIZQ',
             'PARDER',
             'DECIMAL',
             'ENTERO',
             'MAYORIGUAL',
             'MENORIGUAL',
             'IGUALIGUAL',
             'DIFERENTE',
             'IGUAL', #=
             'MAYOR',
             'MENOR',             
             'MAS', #+            
             'MENOS', #-
             'MULTIPLICACION',
             'DIVISION',
             'COMENTARIO'

         ] + list(reserved.values())


# 3) Especificación de los tokens

# A) Tokens simples, que solo se definen mediante expresiones regulares
# Inician con el prefijo "t_" seguido del nombre del Token

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    tipo_reservado = reserved.get(t.value, 'ID')
    return t


def t_DECIMAL(t):
    r'\d+\.\d+'  # El punto se tiene que escapar porque en expresiones regulares significa cualqueir símbolo
    # una mejor expresión regular teniendo en cuenta los exponentes:
    '[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor flotante excede los límites %f", t.value)
        t.value = 0
    return t  # Siempre se debe devolver el objeto t, de lo contrario se descarta el token


def t_ENTERO(t):
    r'\d+'  # \d es equivalente a [0-9]

    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor entero excede los límites %d", t.value)
        t.value = 0
    return t  # Siempre se debe devolver el objeto t, de lo contrario se descarta el token


""""
t_EVALUAR  = r'evaluar' #Se incluyen uno por cada palabra reservada
t_SI  = r'si'
"""

t_PTCOMA = r';'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_DIFERENTE = r'!='
t_IGUALIGUAL = r'=='
t_IGUAL = r'='
t_MAS = r'\+'
t_MENOS = r'\-'
t_MAYOR = r'\>'
t_MENOR = r'\<'
t_MULTIPLICACION = '\*'
t_DIVISION = '/'
t_ignore = " \t"  # caracteres ignorados: espacio y tabulador


# B) Tokens que requieren una acción
# Las definiciones de Tokens que requieren otros tipo de acciones se realizan mediante Funciones
# El argumento t es una instancia de LexerToken, el cual tiene cuatro atributos:
# t.type -> tipo del token (int, string, ..)
# t.value -> es el lexema
# t.lineno -> línea en la que se encontró
# t.lexpos -> posición relativa al inicio del texto


def t_COMENTARIO(t):
    r'%.*'  # Una línea que inicia con '#', seguida de lo que una cadena conformada por cualesqueira símbolos
    pass
    # No regresa ningún valor. El token es ignorado


# Definir una regla para que podamos rastrear los números de línea.
def t_newline(t):
    r'\n+'  # expresión regular para indicar que es uno o más saltos de línea
    t.lexer.lineno += len(t.value)


# Definir una regla para los caracteres inválidos
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)  # se salta un caracter


# Construimos el lexer
import logging
logging.basicConfig(
     level = logging.DEBUG,
     filename = "lexerlog.txt",
     filemode = "w",
     format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()
lexer = lex.lex(debug=True,debuglog=log)