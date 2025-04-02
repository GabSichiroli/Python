#Bibliotecas;

import random

#Aleatorizador;

numero_aleatorio = random.randint(1000, 9999)
print(f"Número aleatório gerado: {numero_aleatorio}") #Manter para controle


#Confere os numeros;

b1=numero_aleatorio//1000
b2=(numero_aleatorio%1000)//100
b3=(numero_aleatorio%100)//10
b4=numero_aleatorio%10

c1="_"
c2="_"
c3="_"
c4="_"

print(b1,b2,b3,b4) #Controle

#Tentativas e Chutes
for tent in range(10,-1,-1):
    print('voce tem', tent, 'tentativas')

    acertos_digitos=0

    num=int(input("\n\tInsira o seu chute:"))

    #Validacao do chute
    while (1000>=num>=9999):

        print(f'\n\tTome cuidado!!!')
        print(f'\tNumero invalido')
        num=int(input("\n\tInsira o seu chute:"))

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

    if num==numero_aleatorio:
        print('Você acertou!')
        break
    else:
        if (tent==0):
            print (f'\nVocê perdeu!')
            print(f'O codigo era {numero_aleatorio}')