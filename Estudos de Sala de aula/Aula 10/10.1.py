def ler( ):
    x=int(input("Insira:"))
    return x

def ant_sus(n):
    n+=1
    print(f"\t\nO sucessor é: {n}")
    n-=2
    print(f"\t\nO antecessor: {n}")
#Main
n=ler()
ant_sus(n)