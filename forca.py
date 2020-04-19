import re
import random
# import androidhelper
# droid = androidhelper.Android()

iniciar=1

while(iniciar==1):


    palavra =['bola','canguru','girafa','espanha','espaguete','sapo','casa','foca','biscoito','pato','luva','mula','anel','lona','toca','abacaxi','olho','rato','nhoque','gravata','dado','mala','vaca','celular','gato','jaca','hamburguer','mola','lama','alho']


    contt=len(palavra)
    #print (contt)

    num = (random.randrange(0,contt-1))


    palavra =palavra[num]
    palavra=palavra.upper()

    conta=(len(palavra))

    print (conta,'letras')
    certas=[]
    erradas=[]
    todas=[]

    a=0
    ok=0
    tam=1

    while(ok<conta):
        #letra=(input('\ndigite uma letra: '))
  
  
        while True and (tam == 1):
        
        
            letra=(input('\nDigite uma letra: '))
            #Se for letra, segue   
            if(letra.isalpha()):
                #droid.ttsSpeak(letra)
                break

        
        tam=(int(len(letra)))

        while (tam > 1):
            letra=(input('\nDigite uma letra: '))
            tam=(int(len(letra)))

  
  
  
  
  
  
        n=0
        ok=0
        letra=letra.upper()
#Identifica se acertou ou errou
#e coloca letras nos arrays, sem repetir

        if re.search(letra, palavra, re.IGNORECASE):
            if(todas.count(letra))<1:
                certas.append(letra)
                todas.append(letra)
        else:
            #print("A string não tem o nome Ana")
            if(todas.count(letra))<1:
                erradas.append(letra)
                todas.append(letra)



        
        while (n<conta):
            if(certas.count(palavra[n]))>0:
                print (palavra[n],end=" ")
                ok=ok+1
            else:
                print('_',end=" ")
            
            #if(certas.count(letra))<1:
                #print ('_',end=" ")
            n=(n+1)
        
            #print (ok)
            if(ok == conta):
                print ('\nFIM DE JOGO')
                #droid.ttsSpeak("Parabéns! Você acertou!")
                xcontinue=(input('\nContinuar? S ou N? '))
                if(xcontinue=='S'):
                    iniciar=1
                elif(xcontinue=='s'):
                    iniciar=1
                else:
                    iniciar=0
                        
                        
        #print('\ncertas:',len(certas),'-',certas)
        #print('erradas:',len(erradas),'-',erradas)
        #print('todas:',len(todas),'-',todas)
    
        print('\n\nCertas:(',len(certas),')',end=" ")
        print(*certas, sep = " ")
    
        print('Erradas:(',len(erradas),')',end=" ")
        print(*erradas, sep = " ")
    
        print('Todas:(',len(todas),')',end=" ")
        print(*todas, sep = " ")
        print ('-'*35)
        e=(len(erradas))
    
    #print (iniciar)