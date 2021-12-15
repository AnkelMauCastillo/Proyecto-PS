#importaciones de las liberias 

import ply.yacc as yacc

#importaremos del analizador sintactico los tokens 
from LexLet import tokens 

precedence = (
    ('left', 'IF', 'LET'),
    ('left', 'MAS','MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('right', 'ENTERO', 'DECIMAL'),
)

# p --> Significa la produccion 
#[i] --> Indice de la produccion , tambien  es nuestro nodo puede tener cualquier valor asignado
#La sintaxis generalmente se especifica en términos de una gramática BNF

#Definir las funciones 

def p_programa(p):
    ' programa : condicion'
    pass

def p_condicion(p):
    ''' condicion : expresion
                    | expresion op_relacional expresion
                    | COMENTARIO                   
    '''
    pass
def p_expresion(p):
    ''' expresion : termino
                    | termino MAS expresion
                    | termino MENOS expresion
    '''
    pass

def p_termino(p):
    ''' termino : factor
                | factor MULTIPLICACION expresion
                | factor DIVISION expresion
    '''
    pass

def p_factor(p):
    ''' factor : ID
                | numero
                | PARIZQ expresion PARDER
                | LET ID IGUAL expresion IN programa ENDLET PTCOMA
                | IF condicion THEN programa ELSE programa ENDIF
    '''
    pass

def p_op_relacional(t):
    ''' op_relacional : expresion MAYOR expresion
                | expresion MENOR expresion
                | expresion MAYORIGUAL expresion  
                | expresion MENORIGUAL expresion               
                | expresion IGUALIGUAL expresion
                |  expresion DIFERENTE expresion'''
    pass

def p_numero(p):
    ''' numero : ENTERO
                | DECIMAL 
    '''
            
def p_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)  # se salta un caracter

#Crear parser que nos va a permitir manejar nuestro yacc
#El Yacc nos va a permitir al programa hacer un analisis sintactico de todo codigo fuente
# Construimos el lexer

parser = yacc.yacc()