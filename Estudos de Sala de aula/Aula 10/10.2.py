def ler( ):
    x=int(input("Insira:"))
    return x
def somar (x,y,z):
    soma=x+y+z
    return soma
#Main
a=ler()
b=ler()
c=ler()
print(f"{somar(a,b,c)}")