#Faça um programa que um programa que faz a leitura de três número inteiros e imprime o maior

a=int(input("\n\tInsira o valor de a:"))
b=int(input("\n\tInsira o valor de b:"))
c=int(input("\n\tInsira o valor de c:"))

maior=a
if maior<=b:
    maior=b
if maior<=c:
    maior=c

print(f"\n\t O valor maior entre {a} {b} {c} é {maior}.")
