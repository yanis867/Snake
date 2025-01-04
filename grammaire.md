# Les Tokens
```
tout : .*
id : [a-zA-Z][a-zA-Z0-9]*
entier : [0-9]+
reel : [0-9]+\.[0-9]+
chaine : \"[^\"]*\"
DEB_C : \#\#
FIN_I : \#
SI : "If"
SINON : "Else"
DEB_SI : "Begin"
FIN_SI : "End"
IMPRIMER : "Snk_Print"
DEB_SNK : "Snk_Begin"
FIN_SNK : "Snk_End"
ENTIER : "Snk_Int"
REEL : "Snk_Real"
CHAINE : "Snk_Strg"
SET : "Set"
GET : "Get"
FROM : "From"
VIR : ","
CRG : "["
CRD : "]"
OPERATEUR : <=|>=|!=|[<>]|==
```
# Les Règles de Production
```
S ::= DEB_SNK SAUT Code FIN_SNK
Code ::= Instructions SAUT Code
Instructions ::=  Declaration FIN_I
                | Affectation FIN_I
                | Affichage FIN_I
                | DEB_C Commentaire
                | Condition
Declaration ::=  ENTIER Ids 
               | REEL Ids 
               | CHAINE Ids
Ids ::= id VIR Ids | id
Affectation ::= SET id entier
              | SET id reel
              | GET id FROM id
Commentaire ::= tout
Affichage ::= IMPRIMER Ids
            | IMPRIMER chaine
Condition ::= Si | Si Sinon
Si ::= SI CRG Comparaison CRD SAUT CodeSi
CodeSi ::= DEB_SI SAUT Code FIN_SI
         | Instructions
Sinon ::= SINON SAUT CodeSi
Comparaison ::= Operande OPERATEUR Operande
Operande ::= id | reel | entire
```

