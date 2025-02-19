#Calcule o valor do premio

valor=float(input("\n\tInsira o valor do premio:"))
p1=(valor*46)/100
p2=(valor*32)/100
p3=valor-(p1+p2)
print("\n\tO primeiro recebera=",p1)
print("\n\tO segundo recebera=",p2)
print("\n\tO terceiro recebera=",p3)