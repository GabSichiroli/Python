import random
import os 
jn=0

while(jn<=9999):


    #tela de entrada
    print(f"\n\t\t\t-----------Bem vindo ao jogo de adivinhação!!----------\n")
    print(f"\n\t\t     Você terá 10 tentativas para acertar a numeração correta!")
    print(f"\n\t\tMas não se preocupe, caso haja dificuldade da partir da 5° tentativa,")
    print(f"\n\t\t\t\tdicas serão disponibilizadas!\n")
    print(f"\n\t\t\t-------------------Boa sorte!-----------------------\n")
    input(f"\n\t\t\t          Aperte enter para continuar!\n")
    os.system('cls')

    numero_aleatorio = random.randint(1000, 9999)
    num_gerado1=numero_aleatorio//1000
    num_gerado2=(numero_aleatorio%1000)//100
    num_gerado3=(numero_aleatorio%100)//10
    num_gerado4=numero_aleatorio%10
    num_correto=numero_aleatorio
    num_saida1=-1
    num_saida2=-2
    num_saida3=-3
    num_saida4=-4
    posicao_dica=0
    posicao_usuario=1
    dica=1
    impar=0
   
    for tent in range(10,0,-1):
        print(f"\n\t\tVocê tem {tent} tentativa(s)")

        acertos_digitos=0

        num=int(input("\n\tInsira o seu chute:"))
        while ((num<1000) or (num>9999)):

            print(f'\n\tTome cuidado!!!')
            print(f'\tNúmero invalido')
            num=int(input("\n\tInsira o seu chute:"))
            os.system('cls')

        num_usuario1=num//1000
        if(num_gerado1==num_usuario1):
            num_saida1=num_usuario1
            acertos_digitos+=1
            
        num_usuario2=(num%1000)//100
        if(num_gerado2==num_usuario2):
            num_saida2=num_usuario2
            acertos_digitos+=1
        
        num_usuario3=(num%100)//10
        if(num_gerado3==num_usuario3):
            num_saida3=num_usuario3
            acertos_digitos+=1
        
        num_usuario4=num%10
        if(num_gerado4==num_usuario4):
            num_saida4=num_usuario4
            acertos_digitos+=1

    
        if(acertos_digitos==0):
            print(f'\nVocê não acertou nenhum digito nesta rodada:')
            input(f"\n\t\t\t\t<<Clique em ENTER>>")
            os.system('cls')
        else:
            print(f'\nVocê acertou {acertos_digitos} digito(s) desta vez.')
            input(f"\n\t\t\t\t<<Clique em ENTER>>")
            os.system('cls')

        if(posicao_usuario==posicao_dica):
            dica-=1
        if(tent==6):
            print(f'\nA partir dessa sua tentativa, te darei dicas agora!!')
        if (tent<=6 and dica==1):
            numero_aleatorio = random.randint(1,4)
            posicao_dica=numero_aleatorio*-1
            while True:
        
                if(posicao_dica==num_saida1):
                    posicao_dica=num_gerado1
                    posicao_usuario=num_usuario1

                if(posicao_dica==num_saida2):
                    posicao_dica=num_gerado2
                    posicao_usuario=num_usuario2
                
                if(posicao_dica==num_saida3):
                    posicao_dica=num_gerado3
                    posicao_usuario=num_usuario3
                
                if(posicao_dica==num_saida4):
                    posicao_dica=num_gerado4
                    posicao_usuario=num_usuario4
                
                if posicao_dica<0: 
                    numero_aleatorio = random.randint(1,4)
                    posicao_dica=numero_aleatorio*-1
                
                if num==num_correto:
                    break
                if posicao_dica>0:
                    break
        
        if(tent<=6 or tent==4 or tent==2):
            if(dica==1) :
                if(posicao_dica==0):
                    print(f"\nO numero é nulo")
                else:
                    if(posicao_dica%2==0):
                        print(f"\nO numero da posição {numero_aleatorio} é par")
                    else:
                        print(f"O numero da posição {numero_aleatorio} é impar") 
                        impar+=1
                dica+=1 
        if((dica==2)and(tent==5 or tent==3)):
            if(impar==1):
                if(posicao_dica>5):
                    print(f"\nO numero da posição {numero_aleatorio} é maior ou igual a 5")   
                else: 
                    print(f"\nO numero da posição {numero_aleatorio} é menor ou igual a 5")        
            else:
                if(posicao_dica<4):
                    print(f"\nO numero da posição {numero_aleatorio} é maior que 4")     
                else:
                    if(posicao_dica>6):
                        print(f"\nO numero da posição {numero_aleatorio} é menor que 6")       
            dica-=1
            impar-=1
            
        print(f"\n\t\t\t\t\tTentativa anterior: {num}")
        if (num_saida1==-1):
            print(" _ ", end=" ")
        else:
            print(f" {num_saida1} ", end=" ")
        if(num_saida2==-2):
            print(" _ ", end=" ")
        else:
            print(f" {num_saida2} ", end=" ")
        if(num_saida3==-3):
            print(" _ ", end=" ")
        else:
            print(f" {num_saida3} ", end=" ")
        if(num_saida4==-4):
            print(" _ ")
        else:
            print(f" {num_saida4} ")

        if (num==num_correto):
                print('Você acertou!')
                tent=11-tent
                print(f"\n\tAcertou em {tent} tentativas, muito bem!")
                break
        else:
            if (tent==1):
                print (f'\nVocê perdeu!')
                print(f'O codigo era {num_correto}')

    print(f"\t\nDeseja jogar novamente?")
    posicao_dica=int(input(f"\t\nPresione 1< para SIM e 0 para NÃO\t\n"))
    if(posicao_dica==1):
        jn+=1
    else:
        jn+=10000