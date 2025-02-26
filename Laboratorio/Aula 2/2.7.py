comprimento=float(input("\n\tInsira o comprimento do tereno:"))
largura=float(input("\n\tInsira a largura do mesmo:"))
valordatela=float(input("\n\tInsira o valor do metro da tela:"))
p=comprimento*2+largura*2
valordatela=valordatela*p
print("\n\t O valor será de: {:.2f}".format(valordatela))