"""
Garcia Dominguez Agueda Hazel
Castillo Zavala Angel Mauricio
"""
from re import DEBUG
import sys
from ParserLetError import yacc


if __name__ == "__main__":
    file_name = sys.argv[1]
    f = open(file_name, "r")

    data = f.read()
    resultado = yacc.parse(data, debug=1)
    print(resultado)

   