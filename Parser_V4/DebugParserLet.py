# Set up a logging object
import sys
import logging
logging.basicConfig(
     level = logging.DEBUG,
     filename = "parselog.txt",
     filemode = "w",
     format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()
from LexLet import lex
import ParserLetError as p

#lex.lex(debug=True,debuglog=log)
if __name__ == "__main__":
    file_name = sys.argv[1]
    f = open(file_name, "r")

    data = f.read()
    resultado = p.parser.parse(data,debug=log)
    print(resultado)