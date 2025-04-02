#Bibliotecas;

import random

jn=0 #Variavel controle para se jogar novamente(jn=jogar novamente)

while(jn<=9999):

    #Aleatorizador;
    numero_aleatorio = random.randint(1000, 9999)
    print(f"Número aleatório gerado: {numero_aleatorio}") #O comando foi mantido para maiores manutenções do codigo;

    #Separa os números em receptiva ordem(b1=Unidade de milhar, b2= Unidade de centena e por assim sucessivamente);

    b1=numero_aleatorio//1000
    b2=(numero_aleatorio%1000)//100
    b3=(numero_aleatorio%100)//10
    b4=numero_aleatorio%10

    #"c" se refere a palavra certo e seus numeros se referem a mesma logica do separador, cada um em sua receptiva casa;
    c1="_"
    c2="_"
    c3="_"
    c4="_"

    #print(b1,b2,b3,b4) #Controle

    #Tentativas e Chutes
    for tent in range(10,-1,-1):
        print('voce tem', tent, 'tentativas')

        acertos_digitos=0 #Por rodada;

        num=int(input("\n\tInsira o seu chute:"))

        #Validação do chute

        while (1000>=num>=9999):

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
    
        print(c1,c2,c3,c4)

    #Define vitoria ou derota:

        if (num==numero_aleatorio):
            print('Você acertou!')
            tent=11-tent
            print(f"Acertou em {tent} tentativas, muito bem!")
            break
        else:
            if (tent==0):
                print (f'\nVocê perdeu!')
                print(f'O codigo era {numero_aleatorio}')

    #Pergunta se o usuario deseja jogar novamente:

    print(f"\t\nDeseja jogar novamente?")
    cont=int(input(f"\t\nPresione 1 para SIM e 0 para NÃO\t\n"))
    if(cont==1):
        jn+=1
    else:
        jn+=10000