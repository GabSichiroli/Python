#Bibliotecas;

import random
import sys

jn=0 #Variavel controle para se jogar novamente(jn=jogar novamente)

while(jn<=9999): #Admistrador "Jogar novamente";

    #Aleatorizador;

    numero_aleatorio = random.randint(1000, 9999)
    print(f"Número aleatório gerado: {numero_aleatorio}") #O comando foi mantido para maiores manutenções do codigo;

    #Separa os números em receptiva ordem(b1=Unidade de milhar, b2= Unidade de centena e por assim sucessivamente);

    b1=numero_aleatorio//1000
    b2=(numero_aleatorio%1000)//100
    b3=(numero_aleatorio%100)//10
    b4=numero_aleatorio%10

    num_correto=numero_aleatorio #Guarda o valor por completo do numero aleatorizado;

    #"c" se refere a palavra certo e seus numeros se referem a mesma logica do separador, cada um em sua receptiva casa;
    c1=-1
    c2=-2
    c3=-3
    c4=-4
    dica=1
    impar=0
    #Tentativas e Chutes
    for tent in range(10,0,-1):
        print('Você tem', tent, 'tentativas')

        acertos_digitos=0 #Por rodada;

        num=int(input("\n\tInsira o seu chute:"))

        #Validação do chute

        while ((num<1000) or (num>9999)):

            print(f'\n\tTome cuidado!!!')
            print(f'\tNúmero invalido')
            num=int(input("\n\tInsira o seu chute:"))

        #Confere se o número digitado está correto:

        num1=num//1000
        if(b1==num1):
            c1=num1
            acertos_digitos+=1
        num2=(num%1000)//100
        if(b2==num2):
            c2=num2
            acertos_digitos+=1
        num3=(num%100)//10
        if(b3==num3):
            c3=num3
            acertos_digitos+=1
        num4=num%10
        if(b4==num4):
            c4=num4
            acertos_digitos+=1

        if(acertos_digitos==0):
            print(f'\nVocê não acertou nenhum digito nesta rodada:')
        else:
            print(f'\nVocê acertou {acertos_digitos} digito(s) desta vez.')
        
        #Dicas;
        if(tent<=6):
            numero_aleatorio = random.randint(1,4)
            cont=numero_aleatorio*-1
            if(cont==c1):
                cont=b1
            if(cont==c2):
                cont=b2
            if(cont==c3):
                cont=b3
            if(cont==c4):
                cont=b4

            if(dica==1):
                if(cont==0):
                    print(f"TALVEZZZ o número seja oval.")
                if(cont%2==1):
                    print(f"O numero da posição {numero_aleatorio} é impar")
                    impar+=1
                else:
                    print(f"O numero da posição {numero_aleatorio} é par")
                dica+=1 
            if((dica==2)and (tent==4 or tent==2)):
                if(impar==1):
                    if(cont>5):
                        print(f"O numero da posição {numero_aleatorio} é maior que 5")
                    if(cont<5):
                        print(f"O numero da posição {numero_aleatorio} é menor que 5")
                else:
                    if(cont<4):
                        print(f"O numero da posição {numero_aleatorio} é maior que 4")
                    if(cont>6):
                        print(f"O numero da posição {numero_aleatorio} é menor que 6")
                dica-=1
                impar-=1

        if(c1==-1):
            print(" _ ", end=" ")
        else:
            print(f" {c1} ", end=" ")
        if(c2==-2):
            print(" _ ", end=" ")
        else:
            print(f" {c2} ", end=" ")
        if(c3==-3):
            print(" _ ", end=" ")
        else:
            print(f" {c3} ", end=" ")
        if(c4==-4):
            print(" _ ")
        else:
            print(f" {c4} ")

    #Define vitoria ou derota:

        if (num==num_correto):
            print('Você acertou!')
            tent=11-tent
            print(f"\n\tAcertou em {tent} tentativas, muito bem!")
            break
        else:
            if (tent==0):
                print (f'\nVocê perdeu!')
                print(f'O codigo era {num_correto}')

    #Pergunta se o usuario deseja jogar novamente:

    print(f"\t\nDeseja jogar novamente?")
    cont=int(input(f"\t\nPresione 1< para SIM e 0 para NÃO\t\n"))
    if(cont==1):
        jn+=1
    else:
        jn+=10000