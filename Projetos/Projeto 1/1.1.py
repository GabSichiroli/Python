#Aleatorizador;

base=9824
num=int(input("\n\tInsira o seu chute:"))

#Confere os numeros;

b1=base//1000
base=base-(b1*1000)
b2=base//100
base=base-(b2*100)
b3=base//10
b4=base%10

print(b1,b2,b3,b4)


