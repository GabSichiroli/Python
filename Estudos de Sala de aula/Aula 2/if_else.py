#Comando de de if e else
#Calcule a área do um quadrilátero e informe se é um quadrado ou retângulo
base=float(input("\n\tInsira o valor da base do quadrilátero em questão:"))
altura=float(input("\n\tInsira o valor da altura do quadrilátero em questão:"))
res=base*altura
if altura==base:
    print(f"\n\tA área do quadrado é de: {res:.2f}")
else:
    print(f"\n\tA área do retângulo é de: {res:.2f}")