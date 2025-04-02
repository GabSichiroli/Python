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
for i in range(1,10):
    poserrada=0
    
    num=int(input("\n\tInsira o seu chute:"))
    num1=num//1000
    if(b1==num1):
        print(f"sim né pae?")
        c1=num1
    if(b2==num1 or b3==num1 or b4==num1):
            print(f"Sim mai ta na posição errada")
            poserrada+=1
    num2=(num%1000)//100
    if(b2==num2):
        print(f"sim né pae?")
        c2=num2
    if(b1==num2 or b3==num2 or b4==num2):
            print(f"Sim mai ta na posição errada")
            poserrada+=1
    num3=(num%100)//10
    if(b3==num3):
        print(f"sim né pae?")
        c3=num3
    if(b2==num3 or b1==num3 or b4==num3):
            print(f"Sim mai ta na posição errada")
            poserrada+=1
    num4=num%10
    if(b4==num4):
        print(f"sim né pae?")
        c4=num4
    if(b2==num4 or b1==num4 or b3==num4):
            print(f"Sim mai ta na posição errada")
            poserrada+=1
    print(poserrada)
    print(c1,c2,c3,c4)