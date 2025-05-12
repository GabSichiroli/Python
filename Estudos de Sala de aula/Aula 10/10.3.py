def ler(nome):
    tipo="Digite o valor da "+nome+": "
    x=float(input(tipo))
    return x
def somaimposto(taxa,custo):
    aux=((taxa/100)+1)*custo
    return custo
#Main
taxaimposto=ler("Taxa")
custo=ler("Custo")
print(f"{somaimposto(taxaimposto,custo)}")