#Exemplo do uso do Input dado em aula:
#O uso de Input tem a seguinte semantica, Input(Mensagem) porem, para podermos atribuir o valor inserido, 
#temos que declarar aquele tipo de variavel, se é um float, um int ou um string

nota1=float(input("\n\tDigite a primeira nota:"))
nota2=float(input("\n\tDigite a segunda nota:"))
media=(nota1+nota2)/2                    #Ao usar o barra você faz uma divisão em floar, caso // dara apenas numeros inteiros.
print("\n\t A media é:", media)