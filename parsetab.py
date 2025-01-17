
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CHAINE CRD CRG DEB_SI DEB_SNK ENTIER FIN_I FIN_SI FIN_SNK FROM GET IMPRIMER OPERATEUR REEL SET SI SINON VIR chaine commentaire entier id newline reelS : DEB_SNK newline Code FIN_SNK\n|Code : Instructions newline Code\n|Instructions :  Declaration FIN_I\n| Affectation FIN_I\n| Affichage FIN_I\n| commentaire\n| ConditionDeclaration : ENTIER Ids\n| REEL Ids\n| CHAINE IdsIds : id VIR Ids\n| idAffectation : SET id entier\n| SET id reel\n| GET id FROM idAffichage : IMPRIMER Ids\n| IMPRIMER chaineCondition : Si\n| Si SinonSi : SI CRG Comparaison CRD newline CodeSiCodeSi : DEB_SI newline Code FIN_SISinon : SINON newline CodeSiComparaison : Operande OPERATEUR OperandeOperande : id\n| entier\n| reel\n| chaine'
    
_lr_action_items = {'DEB_SNK':([0,],[2,]),'$end':([0,1,19,],[-2,0,-1,]),'newline':([2,5,9,10,17,21,22,23,32,33,49,50,51,57,58,],[3,20,-8,-9,-20,-5,-6,-7,-21,40,-24,53,54,-22,-23,]),'FIN_SNK':([3,4,20,35,],[-4,19,-4,-3,]),'commentaire':([3,20,53,],[9,9,9,]),'ENTIER':([3,20,53,],[11,11,11,]),'REEL':([3,20,53,],[12,12,12,]),'CHAINE':([3,20,53,],[13,13,13,]),'SET':([3,20,53,],[14,14,14,]),'GET':([3,20,53,],[15,15,15,]),'IMPRIMER':([3,20,53,],[16,16,16,]),'SI':([3,20,53,],[18,18,18,]),'FIN_I':([6,7,8,24,25,26,27,30,31,37,38,47,48,],[21,22,23,-10,-14,-11,-12,-18,-19,-15,-16,-13,-17,]),'id':([11,12,13,14,15,16,34,36,39,52,],[25,25,25,28,29,25,43,25,48,43,]),'chaine':([16,34,52,],[31,46,46,]),'SINON':([17,57,58,],[33,-22,-23,]),'CRG':([18,],[34,]),'FIN_SI':([20,35,53,56,],[-4,-3,-4,58,]),'VIR':([25,],[36,]),'entier':([28,34,52,],[37,44,44,]),'reel':([28,34,52,],[38,45,45,]),'FROM':([29,],[39,]),'DEB_SI':([40,54,],[50,50,]),'CRD':([41,43,44,45,46,55,],[51,-26,-27,-28,-29,-25,]),'OPERATEUR':([42,43,44,45,46,],[52,-26,-27,-28,-29,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'Code':([3,20,53,],[4,35,56,]),'Instructions':([3,20,53,],[5,5,5,]),'Declaration':([3,20,53,],[6,6,6,]),'Affectation':([3,20,53,],[7,7,7,]),'Affichage':([3,20,53,],[8,8,8,]),'Condition':([3,20,53,],[10,10,10,]),'Si':([3,20,53,],[17,17,17,]),'Ids':([11,12,13,16,36,],[24,26,27,30,47,]),'Sinon':([17,],[32,]),'Comparaison':([34,],[41,]),'Operande':([34,52,],[42,55,]),'CodeSi':([40,54,],[49,57,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> DEB_SNK newline Code FIN_SNK','S',4,'p_S','attempt1.py',52),
  ('S -> <empty>','S',0,'p_S','attempt1.py',53),
  ('Code -> Instructions newline Code','Code',3,'p_Code','attempt1.py',56),
  ('Code -> <empty>','Code',0,'p_Code','attempt1.py',57),
  ('Instructions -> Declaration FIN_I','Instructions',2,'p_Instructions','attempt1.py',60),
  ('Instructions -> Affectation FIN_I','Instructions',2,'p_Instructions','attempt1.py',61),
  ('Instructions -> Affichage FIN_I','Instructions',2,'p_Instructions','attempt1.py',62),
  ('Instructions -> commentaire','Instructions',1,'p_Instructions','attempt1.py',63),
  ('Instructions -> Condition','Instructions',1,'p_Instructions','attempt1.py',64),
  ('Declaration -> ENTIER Ids','Declaration',2,'p_Declaration','attempt1.py',68),
  ('Declaration -> REEL Ids','Declaration',2,'p_Declaration','attempt1.py',69),
  ('Declaration -> CHAINE Ids','Declaration',2,'p_Declaration','attempt1.py',70),
  ('Ids -> id VIR Ids','Ids',3,'p_Ids','attempt1.py',74),
  ('Ids -> id','Ids',1,'p_Ids','attempt1.py',75),
  ('Affectation -> SET id entier','Affectation',3,'p_Affectation','attempt1.py',79),
  ('Affectation -> SET id reel','Affectation',3,'p_Affectation','attempt1.py',80),
  ('Affectation -> GET id FROM id','Affectation',4,'p_Affectation','attempt1.py',81),
  ('Affichage -> IMPRIMER Ids','Affichage',2,'p_Affichage','attempt1.py',85),
  ('Affichage -> IMPRIMER chaine','Affichage',2,'p_Affichage','attempt1.py',86),
  ('Condition -> Si','Condition',1,'p_Condition','attempt1.py',89),
  ('Condition -> Si Sinon','Condition',2,'p_Condition','attempt1.py',90),
  ('Si -> SI CRG Comparaison CRD newline CodeSi','Si',6,'p_Si','attempt1.py',94),
  ('CodeSi -> DEB_SI newline Code FIN_SI','CodeSi',4,'p_CodeSi','attempt1.py',98),
  ('Sinon -> SINON newline CodeSi','Sinon',3,'p_Sinon','attempt1.py',101),
  ('Comparaison -> Operande OPERATEUR Operande','Comparaison',3,'p_Comparaison','attempt1.py',104),
  ('Operande -> id','Operande',1,'p_Operande','attempt1.py',108),
  ('Operande -> entier','Operande',1,'p_Operande','attempt1.py',109),
  ('Operande -> reel','Operande',1,'p_Operande','attempt1.py',110),
  ('Operande -> chaine','Operande',1,'p_Operande','attempt1.py',111),
]
