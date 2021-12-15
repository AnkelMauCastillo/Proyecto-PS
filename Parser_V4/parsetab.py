
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIFLETleftMASMENOSleftMULTIPLICACIONDIVISIONrightENTERODECIMALCOMENTARIO DECIMAL DIFERENTE DIVISION ELSE ENDIF ENDLET ENTERO ID IF IGUAL IGUALIGUAL IN LET MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MULTIPLICACION PARDER PARIZQ PTCOMA THEN programa : condicion condicion : expresion\n                    | expresion op_relacional expresion\n                    | COMENTARIO                   \n     expresion : termino\n                    | termino MAS expresion\n                    | termino MENOS expresion\n     termino : factor\n                | factor MULTIPLICACION expresion\n                | factor DIVISION expresion\n     factor : ID\n                | numero\n                | PARIZQ expresion PARDER\n                | LET ID IGUAL expresion IN programa ENDLET PTCOMA\n                | IF condicion THEN programa ELSE programa ENDIF\n     op_relacional : expresion MAYOR expresion\n                | expresion MENOR expresion\n                | expresion MAYORIGUAL expresion  \n                | expresion MENORIGUAL expresion               \n                | expresion IGUALIGUAL expresion\n                |  expresion DIFERENTE expresion numero : ENTERO\n                | DECIMAL \n    '
    
_lr_action_items = {'COMENTARIO':([0,11,36,45,46,],[4,4,4,4,4,]),'ID':([0,3,5,6,7,8,9,10,11,12,13,15,16,17,18,19,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,50,51,],[7,7,-5,-8,-11,-12,7,21,7,-22,-23,7,7,7,7,7,7,7,7,7,7,7,-6,-7,-9,-10,-13,7,7,-16,-17,-18,-19,-20,-21,7,7,-15,-14,]),'PARIZQ':([0,3,5,6,7,8,9,11,12,13,15,16,17,18,19,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,50,51,],[9,9,-5,-8,-11,-12,9,9,-22,-23,9,9,9,9,9,9,9,9,9,9,9,-6,-7,-9,-10,-13,9,9,-16,-17,-18,-19,-20,-21,9,9,-15,-14,]),'LET':([0,3,5,6,7,8,9,11,12,13,15,16,17,18,19,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,50,51,],[10,10,-5,-8,-11,-12,10,10,-22,-23,10,10,10,10,10,10,10,10,10,10,10,-6,-7,-9,-10,-13,10,10,-16,-17,-18,-19,-20,-21,10,10,-15,-14,]),'IF':([0,3,5,6,7,8,9,11,12,13,15,16,17,18,19,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,50,51,],[11,11,-5,-8,-11,-12,11,11,-22,-23,11,11,11,11,11,11,11,11,11,11,11,-6,-7,-9,-10,-13,11,11,-16,-17,-18,-19,-20,-21,11,11,-15,-14,]),'ENTERO':([0,3,5,6,7,8,9,11,12,13,15,16,17,18,19,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,50,51,],[12,12,-5,-8,-11,-12,12,12,-22,-23,12,12,12,12,12,12,12,12,12,12,12,-6,-7,-9,-10,-13,12,12,-16,-17,-18,-19,-20,-21,12,12,-15,-14,]),'DECIMAL':([0,3,5,6,7,8,9,11,12,13,15,16,17,18,19,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,50,51,],[13,13,-5,-8,-11,-12,13,13,-22,-23,13,13,13,13,13,13,13,13,13,13,13,-6,-7,-9,-10,-13,13,13,-16,-17,-18,-19,-20,-21,13,13,-15,-14,]),'$end':([1,2,3,4,5,6,7,8,12,13,29,30,31,32,33,34,50,51,],[0,-1,-2,-4,-5,-8,-11,-12,-22,-23,-3,-6,-7,-9,-10,-13,-15,-14,]),'ELSE':([2,3,4,5,6,7,8,12,13,29,30,31,32,33,34,44,50,51,],[-1,-2,-4,-5,-8,-11,-12,-22,-23,-3,-6,-7,-9,-10,-13,46,-15,-14,]),'ENDLET':([2,3,4,5,6,7,8,12,13,29,30,31,32,33,34,47,50,51,],[-1,-2,-4,-5,-8,-11,-12,-22,-23,-3,-6,-7,-9,-10,-13,49,-15,-14,]),'ENDIF':([2,3,4,5,6,7,8,12,13,29,30,31,32,33,34,48,50,51,],[-1,-2,-4,-5,-8,-11,-12,-22,-23,-3,-6,-7,-9,-10,-13,50,-15,-14,]),'THEN':([3,4,5,6,7,8,12,13,22,29,30,31,32,33,34,50,51,],[-2,-4,-5,-8,-11,-12,-22,-23,36,-3,-6,-7,-9,-10,-13,-15,-14,]),'MAYOR':([5,6,7,8,12,13,14,30,31,32,33,34,50,51,],[-5,-8,-11,-12,-22,-23,23,-6,-7,-9,-10,-13,-15,-14,]),'MENOR':([5,6,7,8,12,13,14,30,31,32,33,34,50,51,],[-5,-8,-11,-12,-22,-23,24,-6,-7,-9,-10,-13,-15,-14,]),'MAYORIGUAL':([5,6,7,8,12,13,14,30,31,32,33,34,50,51,],[-5,-8,-11,-12,-22,-23,25,-6,-7,-9,-10,-13,-15,-14,]),'MENORIGUAL':([5,6,7,8,12,13,14,30,31,32,33,34,50,51,],[-5,-8,-11,-12,-22,-23,26,-6,-7,-9,-10,-13,-15,-14,]),'IGUALIGUAL':([5,6,7,8,12,13,14,30,31,32,33,34,50,51,],[-5,-8,-11,-12,-22,-23,27,-6,-7,-9,-10,-13,-15,-14,]),'DIFERENTE':([5,6,7,8,12,13,14,30,31,32,33,34,50,51,],[-5,-8,-11,-12,-22,-23,28,-6,-7,-9,-10,-13,-15,-14,]),'PARDER':([5,6,7,8,12,13,20,30,31,32,33,34,50,51,],[-5,-8,-11,-12,-22,-23,34,-6,-7,-9,-10,-13,-15,-14,]),'MAS':([5,6,7,8,12,13,30,31,32,33,34,50,51,],[16,-8,-11,-12,-22,-23,-6,-7,-9,-10,-13,-15,-14,]),'MENOS':([5,6,7,8,12,13,30,31,32,33,34,50,51,],[17,-8,-11,-12,-22,-23,-6,-7,-9,-10,-13,-15,-14,]),'IN':([5,6,7,8,12,13,30,31,32,33,34,43,50,51,],[-5,-8,-11,-12,-22,-23,-6,-7,-9,-10,-13,45,-15,-14,]),'MULTIPLICACION':([6,7,8,12,13,34,50,51,],[18,-11,-12,-22,-23,-13,-15,-14,]),'DIVISION':([6,7,8,12,13,34,50,51,],[19,-11,-12,-22,-23,-13,-15,-14,]),'IGUAL':([21,],[35,]),'PTCOMA':([49,],[51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,36,45,46,],[1,44,47,48,]),'condicion':([0,11,36,45,46,],[2,22,2,2,2,]),'expresion':([0,3,9,11,15,16,17,18,19,23,24,25,26,27,28,35,36,45,46,],[3,14,20,3,29,30,31,32,33,37,38,39,40,41,42,43,3,3,3,]),'termino':([0,3,9,11,15,16,17,18,19,23,24,25,26,27,28,35,36,45,46,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'factor':([0,3,9,11,15,16,17,18,19,23,24,25,26,27,28,35,36,45,46,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'numero':([0,3,9,11,15,16,17,18,19,23,24,25,26,27,28,35,36,45,46,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'op_relacional':([3,],[15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> condicion','programa',1,'p_programa','ParserLetError.py',22),
  ('condicion -> expresion','condicion',1,'p_condicion','ParserLetError.py',26),
  ('condicion -> expresion op_relacional expresion','condicion',3,'p_condicion','ParserLetError.py',27),
  ('condicion -> COMENTARIO','condicion',1,'p_condicion','ParserLetError.py',28),
  ('expresion -> termino','expresion',1,'p_expresion','ParserLetError.py',32),
  ('expresion -> termino MAS expresion','expresion',3,'p_expresion','ParserLetError.py',33),
  ('expresion -> termino MENOS expresion','expresion',3,'p_expresion','ParserLetError.py',34),
  ('termino -> factor','termino',1,'p_termino','ParserLetError.py',39),
  ('termino -> factor MULTIPLICACION expresion','termino',3,'p_termino','ParserLetError.py',40),
  ('termino -> factor DIVISION expresion','termino',3,'p_termino','ParserLetError.py',41),
  ('factor -> ID','factor',1,'p_factor','ParserLetError.py',46),
  ('factor -> numero','factor',1,'p_factor','ParserLetError.py',47),
  ('factor -> PARIZQ expresion PARDER','factor',3,'p_factor','ParserLetError.py',48),
  ('factor -> LET ID IGUAL expresion IN programa ENDLET PTCOMA','factor',8,'p_factor','ParserLetError.py',49),
  ('factor -> IF condicion THEN programa ELSE programa ENDIF','factor',7,'p_factor','ParserLetError.py',50),
  ('op_relacional -> expresion MAYOR expresion','op_relacional',3,'p_op_relacional','ParserLetError.py',55),
  ('op_relacional -> expresion MENOR expresion','op_relacional',3,'p_op_relacional','ParserLetError.py',56),
  ('op_relacional -> expresion MAYORIGUAL expresion','op_relacional',3,'p_op_relacional','ParserLetError.py',57),
  ('op_relacional -> expresion MENORIGUAL expresion','op_relacional',3,'p_op_relacional','ParserLetError.py',58),
  ('op_relacional -> expresion IGUALIGUAL expresion','op_relacional',3,'p_op_relacional','ParserLetError.py',59),
  ('op_relacional -> expresion DIFERENTE expresion','op_relacional',3,'p_op_relacional','ParserLetError.py',60),
  ('numero -> ENTERO','numero',1,'p_numero','ParserLetError.py',64),
  ('numero -> DECIMAL','numero',1,'p_numero','ParserLetError.py',65),
]