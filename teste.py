from rich import print
import os
#Constantes
Votos_Bolsonaro = 0
Votos_Lula = 0
#Loop
while True:
    print('*'*20)
    print(f'TOTAL BOLSONARO:{Votos_Bolsonaro}{os.linesep}TOTAL LULA:{Votos_Lula}')
    print('*'*20)
    #Menu de Votação
    try:
     Voto = int(input(f'Para quem gostaria de votar?{os.linesep}22- Bolsonaro{os.linesep}13- Lula{os.linesep}seu voto:')) 
     if Voto ==22:
          Votos_Bolsonaro +=1
     elif Voto ==13:
          Votos_Lula +=1
     else:
      pass    
    except:
      print('Digite Apenas 13 ou 22')    
    os.system('cls')   
   