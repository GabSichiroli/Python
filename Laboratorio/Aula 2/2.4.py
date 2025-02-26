dias=int(input("\n\tInsira a quantidades de dias trabalhados:"))
valorbruto=dias*30
valorliquido=valorbruto-(valorbruto*(8/100))
print("\n\t O valor bruto seria de {:2} e o valor liquído é de {:.2f}".format(valorbruto,valorliquido))