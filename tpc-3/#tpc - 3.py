#tpc - 3 
inicio = int ( input (" Quer que eu tente adivinhar o número que pensou (1)? Ou quer tentar adivinhar o número que eu pensei(2)?"))
tentativas = 0
if inicio == 1:
 import random
 mínimo = 0
 máximo = 100
 pergunta= int (input (" pense num número  entre 0 e 100"))
 palpite = random. randrange(1,100)
 print( palpite)
 tentativas = tentativas + 1 
 resultado = 0
 while resultado!= 3 :
  resultado = int (input (" este número é muito grande (1), muito pequeno (2) ou acertei (3)?") )
  if resultado == 2:
   if palpite > mínimo:
    mínimo = palpite + 1
   palpite = random.randint( mínimo, máximo)
   print( palpite)
  if resultado == 1:
   if palpite < máximo:
    máximo = palpite- 1 
   palpite = random.randint(mínimo, máximo)
   print ( palpite )
   tentativas = tentativas + 1
 if resultado == 3:
   print ( "Acertei no teu número em "+str(tentativas)+" tentativas")


if  inicio == 2 :
  import random 
  n= random. randrange (1,100)
  tentativas = 1
  palpite = int (input (" tente adivinhar o número que estou a pensar"))
  while n!= palpite :
   if palpite < n :
    palpite = int(input (" baixo, tenta outro número"))
    tentativas = tentativas + 1 
   elif palpite > n :
    palpite = int (input(" alto, tenta outro número")) 
   tentativas = tentativas + 1 
   if palpite == n :
    print (" Parabéns acertaste no número em ",tentativas," tentativas!!!")
 
 
   


