#importaciones de las liberias 

import ply.yacc as yacc

#importaremos del analizador sintactico los tokens 
from AnalizadorLexico import tokens 

precedence = (
    ('left', 'IF', 'LET'),
    ('right', 'ENDLET', 'ENDIF', 'IN'),
    ('left', 'MAS','MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('right', 'IGUAL')
)

# p --> Significa la produccion 
#[i] --> Indice de la produccion , tambien  es nuestro nodo puede tener cualquier valor asignado
#La sintaxis generalmente se especifica en términos de una gramática BNF

#Definir las funciones 

def p_programa(p):
    ' programa : condicion'
    p[0] = p[1]

def p_condicion(p):
    ''' condicion : expresion                   
    '''
    p[0] = p[1]


def p_expresion(p):
    ''' expresion : termino                    
    '''    
    p[0] = p[1]

def p_termino(p):
    ''' termino : factor 
    '''
    p[0] = p[1]

def p_factor(p):
    ''' factor : PARIZQ expresion PARDER         
                | IF condicion  THEN programa ELSE programa  ENDIF
    '''
    p[0] = p[1]

def p_factor_ID(p):
    ''' factor_ID : ID'''
    p[0] = p[1]

def p_factor_LET(p):
    '''factor_LET : LET ID IGUAL expresion  IN programa ENDLET
                | LET ID ENTERO IGUAL expresion IN programa ENDLET'''
'''expresion:expresion MASS termino
            | expresion MENOSS termino
            | termino'''

def p_expresion_MAS(p):
     'expresion : expresion MAS termino'
     p[0] = p[2] 
 
def p_expresion_MENOS(p):
     'expresion : expresion MENOS termino'
     p[0] = p[2] 

def p_termino_MULTIPLICACION(p):
     '''termino : factor MULTIPLICACION expresion
              | factor DIVISION expresion '''

     p[0] = p[2] 

def p_expresion_Comentario(p):
    'expresion : COMENTARIO'
    p[0] = p[1]   

def p_condicion_Relacional(p):  
    '''condicion : expresion MAYOR expresion
                | expresion MENOR expresion
                | expresion MAYORIGUAL expresion  
                | expresion MENORIGUAL expresion
                | expresion IGUALIGUAL expresion
                | expresion DIFERENTE expresion '''
    if p[1] == '==' : p[0] = p[1] == p[3]
    elif p[1] == '>' : p[0] = p[1] > p[3]
    elif p[1] == '<' : p[0] = p[1] < p[3]
    elif p[1] == '<=' : p[0] = p[1] <= p[3]
    elif p[1] == '>=' : p[0] = p[1] >= p[3]
    elif p[1] == '!=' : p[0] = p[1] != p[3]
    
def p_numero(p):
    '''
    '''
    pass
def p_factor_ENTERO(p):
     'factor_ENTERO : ENTERO'
     p[0] = p[1]

def p_factor_DECIMAL(p):
     'factor : DECIMAL'
     p[0] = p[1]	 

def p_expresion_SignosPuntuacion(p):
    '''expresion : expresion PTCOMA''' 
    p[0] = p[2]     

def p_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)  # se salta un caracter

#Crear parser que nos va a permitir manejar nuestro yacc
#El Yacc nos va a permitir al programa hacer un analisis sintactico de todo codigo fuente
import logging
logging.basicConfig(
     level = logging.DEBUG,
     filename = "parser.txt",
     filemode = "w",
     format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()
parser = yacc.yacc(debug=True,debuglog=log)