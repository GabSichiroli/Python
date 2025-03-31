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

print(b1,b2,b3,b4) #Controle

#Tentativas e Chutes
for i in range(1,10):
    num=int(input("\n\tInsira o seu chute:"))
    num1=num//1000
    if(b1==num1):
        print(f"sim né pae?")
    if(b2==num1 or b3==num1 or b4==num1):
            print(f"Sim mai ta na posição errada")
    else:
        print(f"ta errado")
    num2=(num%1000)//100
    num3=(num%100)//10
    num4=num%10
    
