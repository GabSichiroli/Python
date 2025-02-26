tempo=int(input("\n\tInsira o valor de minutos de viagem:"))
autonomia=float(input("\n\tInsira o valor da autonomia do carro:"))
velocidade=float(input("\n\tInsira a velociade média:"))
tempo=tempo/60
dis=velocidade*tempo
consu=dis/autonomia
print("\n\t A distância percorida é de {:.2f} KMs e o consume é de {:.2f} Litros".format(dis,consu))

