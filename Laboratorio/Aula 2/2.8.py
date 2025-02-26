num=int(input("\n\tInsira o numero desejado de 3 casas:"))
parte1=num//100
num=num-(parte1*100)
parte2=num//10
parte3=num%10
print("\n\tResultado:{:}{:}{:}".format(parte3,parte2,parte1))