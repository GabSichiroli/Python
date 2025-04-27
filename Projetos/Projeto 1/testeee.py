#Bibliotecas;

import random
import os 

jn=0 #Variavel controle para se jogar novamente(jn=jogar novamente)

while(jn<=9999): #Admistrador "Jogar novamente";


    #tela de entrada
    print(f"\n\t\t\t-----------Bem vindo ao jogo de adivinhação!!----------\n")
    print(f"\n\t\t     Você terá 10 tentativas para acertar a numeração correta!")
    print(f"\n\t\tMas não se preocupe, caso haja dificuldade da partir da 5° tentativa,")
    print(f"\n\t\t\t\tdicas serão disponibilizadas!\n")
    print(f"\n\t\t\t-------------------Boa sorte!-----------------------\n")
    input(f"\n\t\t\t          Aperte enter para continuar!\n")
    os.system('cls')

    #Aleatorizador;

    numero_aleatorio = random.randint(1000, 9999)
    print(f"\nNúmero aleatório gerado: {numero_aleatorio}") #O comando foi mantido para maiores manutenções do codigo;

    #Separa os números em receptiva ordem(numgerado_1=Unidade de milhar, numgerado_2= Unidade de centena e por assim sucessivamente);

    num_gerado1=numero_aleatorio//1000
    num_gerado2=(numero_aleatorio%1000)//100
    num_gerado3=(numero_aleatorio%100)//10
    num_gerado4=numero_aleatorio%10

    num_correto=numero_aleatorio #Guarda o valor por completo do numero aleatorizado;

    #"c" se refere a palavra certo e seus numeros se referem a mesma logica do separador, cada um em sua receptiva casa;
    num_saida1=-1
    num_saida2=-2
    num_saida3=-3
    num_saida4=-4
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
            input(f"\n\t\t\t\t<<Clique ENTER>>")
            os.system('cls')
        else:
            print(f'\nVocê acertou {acertos_digitos} digito(s) desta vez.')
            input(f"\n\t\t\t\t<<Clique ENTER>>")
            os.system('cls')


        #Dicas
        if(tent==6):
            print(f'\nA partir dessa sua tentativa, te darei dicas agora!!')
        if (tent<=6):
            numero_aleatorio = random.randint(1,4)
            posicao_dica=numero_aleatorio*-1
            while True:
        
                if(posicao_dica==num_saida1):
                    posicao_dica=num_gerado1

                if(posicao_dica==num_saida2):
                    posicao_dica=num_gerado2
                
                if(posicao_dica==num_saida3):
                    posicao_dica=num_gerado3
                
                if(posicao_dica==num_saida4):
                    posicao_dica=num_gerado4
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
                    print(f"\nO numero da posição {numero_aleatorio} é maior que 5")   
                else:
                    print(f"\nO numero da posição {numero_aleatorio} é menor que 5")        
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
            print(f" {num_gerado1} ", end=" ")
        if(num_saida2==-2):
            print(" _ ", end=" ")
        else:
            print(f" {num_gerado2} ", end=" ")
        if(num_saida3==-3):
            print(" _ ", end=" ")
        else:
            print(f" {num_gerado3} ", end=" ")
        if(num_saida4==-4):
            print(" _ ")
        else:
            print(f" {num_gerado4} ")
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