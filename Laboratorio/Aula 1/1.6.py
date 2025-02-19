#Dadas a medidas de uma sala, comprimento e largura e falor do metro quadrado do carpete, quando que daria para forar o ambiente

comp=float(input("\n\tInsira o comprimento da ambiente:"))
lar=float(input("\n\tInsira a largura do seu ambiente:"))
preço=float(input("\n\tInsira o preço do do metro quadrado do carpete:"))
area=comp*lar
preço=area*preço
print("\n\n\tO consumo de gasolina é de:",preço)