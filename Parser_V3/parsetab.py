
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIFLETrightENDLETENDIFINleftMASMENOSleftMULTIPLICACIONDIVISIONrightIGUALCOMENTARIO DECIMAL DIFERENTE DIVISION ELSE ENDIF ENDLET ENTERO ID IF IGUAL IGUALIGUAL IN LET MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MULTIPLICACION PARDER PARIZQ PTCOMA THEN programa : condicion condicion : expresion                   \n     expresion : termino                    \n     termino : factor \n     factor : PARIZQ expresion PARDER         \n                | IF condicion  THEN programa ELSE programa  ENDIF\n     factor : IDfactor : LET ID IGUAL expresion  IN programa ENDLET\n                | LET ID ENTERO IGUAL expresion IN programa ENDLETexpresion : expresion MAS terminoexpresion : expresion MENOS terminotermino : factor MULTIPLICACION expresion\n              | factor DIVISION expresion expresion : COMENTARIOcondicion : expresion MAYOR expresion\n                | expresion MENOR expresion\n                | expresion MAYORIGUAL expresion  \n                | expresion MENORIGUAL expresion\n                | expresion IGUALIGUAL expresion\n                | expresion DIFERENTE expresion \n    factor : ENTEROfactor : DECIMALexpresion : expresion PTCOMA'
    
_lr_action_items = {'COMENTARIO':([0,7,8,13,14,15,16,17,18,22,23,38,39,43,44,45,49,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'PARIZQ':([0,7,8,13,14,15,16,17,18,19,20,22,23,38,39,43,44,45,49,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'IF':([0,7,8,13,14,15,16,17,18,19,20,22,23,38,39,43,44,45,49,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'ID':([0,7,8,10,13,14,15,16,17,18,19,20,22,23,38,39,43,44,45,49,],[9,9,9,26,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'LET':([0,7,8,13,14,15,16,17,18,19,20,22,23,38,39,43,44,45,49,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'ENTERO':([0,7,8,13,14,15,16,17,18,19,20,22,23,26,38,39,43,44,45,49,],[11,11,11,11,11,11,11,11,11,11,11,11,11,40,11,11,11,11,11,11,]),'DECIMAL':([0,7,8,13,14,15,16,17,18,19,20,22,23,38,39,43,44,45,49,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'$end':([1,2,3,4,5,6,9,11,12,21,27,28,29,30,31,32,33,34,35,36,37,50,51,53,],[0,-1,-2,-3,-14,-4,-7,-21,-22,-23,-15,-16,-17,-18,-19,-20,-10,-11,-12,-13,-5,-6,-8,-9,]),'ELSE':([2,3,4,5,6,9,11,12,21,27,28,29,30,31,32,33,34,35,36,37,41,50,51,53,],[-1,-2,-3,-14,-4,-7,-21,-22,-23,-15,-16,-17,-18,-19,-20,-10,-11,-12,-13,-5,44,-6,-8,-9,]),'ENDIF':([2,3,4,5,6,9,11,12,21,27,28,29,30,31,32,33,34,35,36,37,47,50,51,53,],[-1,-2,-3,-14,-4,-7,-21,-22,-23,-15,-16,-17,-18,-19,-20,-10,-11,-12,-13,-5,50,-6,-8,-9,]),'ENDLET':([2,3,4,5,6,9,11,12,21,27,28,29,30,31,32,33,34,35,36,37,48,50,51,52,53,],[-1,-2,-3,-14,-4,-7,-21,-22,-23,-15,-16,-17,-18,-19,-20,-10,-11,-12,-13,-5,51,-6,-8,53,-9,]),'THEN':([3,4,5,6,9,11,12,21,25,27,28,29,30,31,32,33,34,35,36,37,50,51,53,],[-2,-3,-14,-4,-7,-21,-22,-23,38,-15,-16,-17,-18,-19,-20,-10,-11,-12,-13,-5,-6,-8,-9,]),'MAYOR':([3,4,5,6,9,11,12,21,33,34,35,36,37,50,51,53,],[13,-3,-14,-4,-7,-21,-22,-23,-10,-11,-12,-13,-5,-6,-8,-9,]),'MENOR':([3,4,5,6,9,11,12,21,33,34,35,36,37,50,51,53,],[14,-3,-14,-4,-7,-21,-22,-23,-10,-11,-12,-13,-5,-6,-8,-9,]),'MAYORIGUAL':([3,4,5,6,9,11,12,21,33,34,35,36,37,50,51,53,],[15,-3,-14,-4,-7,-21,-22,-23,-10,-11,-12,-13,-5,-6,-8,-9,]),'MENORIGUAL':([3,4,5,6,9,11,12,21,33,34,35,36,37,50,51,53,],[16,-3,-14,-4,-7,-21,-22,-23,-10,-11,-12,-13,-5,-6,-8,-9,]),'IGUALIGUAL':([3,4,5,6,9,11,12,21,33,34,35,36,37,50,51,53,],[17,-3,-14,-4,-7,-21,-22,-23,-10,-11,-12,-13,-5,-6,-8,-9,]),'DIFERENTE':([3,4,5,6,9,11,12,21,33,34,35,36,37,50,51,53,],[18,-3,-14,-4,-7,-21,-22,-23,-10,-11,-12,-13,-5,-6,-8,-9,]),'MAS':([3,4,5,6,9,11,12,21,24,27,28,29,30,31,32,33,34,35,36,37,42,46,50,51,53,],[19,-3,-14,-4,-7,-21,-22,-23,19,19,19,19,19,19,19,-10,-11,-12,-13,-5,19,19,-6,-8,-9,]),'MENOS':([3,4,5,6,9,11,12,21,24,27,28,29,30,31,32,33,34,35,36,37,42,46,50,51,53,],[20,-3,-14,-4,-7,-21,-22,-23,20,20,20,20,20,20,20,-10,-11,-12,-13,-5,20,20,-6,-8,-9,]),'PTCOMA':([3,4,5,6,9,11,12,21,24,27,28,29,30,31,32,33,34,35,36,37,42,46,50,51,53,],[21,-3,-14,-4,-7,-21,-22,-23,21,21,21,21,21,21,21,-10,-11,-12,-13,-5,21,21,-6,-8,-9,]),'PARDER':([4,5,6,9,11,12,21,24,33,34,35,36,37,50,51,53,],[-3,-14,-4,-7,-21,-22,-23,37,-10,-11,-12,-13,-5,-6,-8,-9,]),'IN':([4,5,6,9,11,12,21,33,34,35,36,37,42,46,50,51,53,],[-3,-14,-4,-7,-21,-22,-23,-10,-11,-12,-13,-5,45,49,-6,-8,-9,]),'MULTIPLICACION':([6,9,11,12,37,50,51,53,],[22,-7,-21,-22,-5,-6,-8,-9,]),'DIVISION':([6,9,11,12,37,50,51,53,],[23,-7,-21,-22,-5,-6,-8,-9,]),'IGUAL':([26,40,],[39,43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,38,44,45,49,],[1,41,47,48,52,]),'condicion':([0,8,38,44,45,49,],[2,25,2,2,2,2,]),'expresion':([0,7,8,13,14,15,16,17,18,22,23,38,39,43,44,45,49,],[3,24,3,27,28,29,30,31,32,35,36,3,42,46,3,3,3,]),'termino':([0,7,8,13,14,15,16,17,18,19,20,22,23,38,39,43,44,45,49,],[4,4,4,4,4,4,4,4,4,33,34,4,4,4,4,4,4,4,4,]),'factor':([0,7,8,13,14,15,16,17,18,19,20,22,23,38,39,43,44,45,49,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> condicion','programa',1,'p_programa','ParserLet.py',23),
  ('condicion -> expresion','condicion',1,'p_condicion','ParserLet.py',27),
  ('expresion -> termino','expresion',1,'p_expresion','ParserLet.py',33),
  ('termino -> factor','termino',1,'p_termino','ParserLet.py',38),
  ('factor -> PARIZQ expresion PARDER','factor',3,'p_factor','ParserLet.py',43),
  ('factor -> IF condicion THEN programa ELSE programa ENDIF','factor',7,'p_factor','ParserLet.py',44),
  ('factor -> ID','factor',1,'p_factor_ID','ParserLet.py',49),
  ('factor -> LET ID IGUAL expresion IN programa ENDLET','factor',7,'p_factor_LET','ParserLet.py',53),
  ('factor -> LET ID ENTERO IGUAL expresion IN programa ENDLET','factor',8,'p_factor_LET','ParserLet.py',54),
  ('expresion -> expresion MAS termino','expresion',3,'p_expresion_MAS','ParserLet.py',60),
  ('expresion -> expresion MENOS termino','expresion',3,'p_expresion_MENOS','ParserLet.py',64),
  ('termino -> factor MULTIPLICACION expresion','termino',3,'p_termino_MULTIPLICACION','ParserLet.py',68),
  ('termino -> factor DIVISION expresion','termino',3,'p_termino_MULTIPLICACION','ParserLet.py',69),
  ('expresion -> COMENTARIO','expresion',1,'p_expresion_Comentario','ParserLet.py',74),
  ('condicion -> expresion MAYOR expresion','condicion',3,'p_condicion_Relacional','ParserLet.py',78),
  ('condicion -> expresion MENOR expresion','condicion',3,'p_condicion_Relacional','ParserLet.py',79),
  ('condicion -> expresion MAYORIGUAL expresion','condicion',3,'p_condicion_Relacional','ParserLet.py',80),
  ('condicion -> expresion MENORIGUAL expresion','condicion',3,'p_condicion_Relacional','ParserLet.py',81),
  ('condicion -> expresion IGUALIGUAL expresion','condicion',3,'p_condicion_Relacional','ParserLet.py',82),
  ('condicion -> expresion DIFERENTE expresion','condicion',3,'p_condicion_Relacional','ParserLet.py',83),
  ('factor -> ENTERO','factor',1,'p_factor_ENTERO','ParserLet.py',96),
  ('factor -> DECIMAL','factor',1,'p_factor_DECIMAL','ParserLet.py',100),
  ('expresion -> expresion PTCOMA','expresion',2,'p_expresion_SignosPuntuacion','ParserLet.py',104),
]