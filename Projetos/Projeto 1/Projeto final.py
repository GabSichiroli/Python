import random
import os 
jn=0
while(jn<=9999):
    print(f"\n\t\t\t-----------Bem vindo ao jogo de adivinhação!!----------\n")
    print(f"\n\t\t     Você terá 10 tentativas para acertar a numeração correta!")
    print(f"\n\t\tMas não se preocupe, caso haja dificuldade da partir da 5° tentativa,")
    print(f"\n\t\t\t\tdicas serão disponibilizadas!\n")
    print(f"\n\t\t\t-------------------Boa sorte!-----------------------\n")
    input(f"\n\t\t\t          Aperte enter para continuar!\n")
    os.system('cls')
    numero_aleatorio = random.randint(1000, 9999)
    b1=numero_aleatorio//1000
    b2=(numero_aleatorio%1000)//100
    b3=(numero_aleatorio%100)//10
    b4=numero_aleatorio%10
    num_correto=numero_aleatorio
    c1=-1
    c2=-2
    c3=-3
    c4=-4
    conti=0
    resp=1
    dica=1
    impar=0
    for tent in range(10,0,-1):
        print(f"\n\t\tVocê tem {tent} tentativa(s)")
        acertos_digitos=0
        num=int(input("\n\tInsira o seu chute:"))
        while ((num<1000) or (num>9999)):
            print(f'\n\tTome cuidado!!!')
            print(f'\tNúmero invalido')
            num=int(input("\n\tInsira o seu chute:"))
            os.system('cls')
        num1=num//1000
        if(b1==num1):
            c1=num1
            acertos_digitos+=1
        num2=(num%1000)//100
        if(b2==num2):
            c2=num2
            acertos_digitos+=1
        num3=(num%100)//10
        if(b3==num3):
            c3=num3
            acertos_digitos+=1
        num4=num%10
        if(b4==num4):
            c4=num4
            acertos_digitos+=1
        if(acertos_digitos==0):
            print(f'\nVocê não acertou nenhum digito nesta rodada:')
            input(f"\n\t\t\t\t<<Clique em ENTER>>")
            os.system('cls')
        else:
            print(f'\nVocê acertou {acertos_digitos} digito(s) desta vez.')
            input(f"\n\t\t\t\t<<Clique em ENTER>>")
            os.system('cls')
        if(resp==conti):
            dica-=1
        if(tent==6):
            print(f'\nA partir dessa sua tentativa, te darei dicas agora!!')
        if (tent<=6 and dica==1):
            numero_aleatorio = random.randint(1,4)
            conti=numero_aleatorio*-1
            while True:
                if(conti==c1):
                    conti=b1
                    resp=num1
                if(conti==c2):
                    conti=b2
                    resp=num2
                if(conti==c3):
                    conti=b3
                    resp=num3
                if(conti==c4):
                    conti=b4
                    resp=num4
                if conti<0: 
                    numero_aleatorio = random.randint(1,4)
                    conti=numero_aleatorio*-1
                if num==num_correto:
                    break
                if conti>0:
                    break
        if(tent<=6 or tent==4 or tent==2):
            if(dica==1) :
                if(conti==0):
                    print(f"\nO numero é nulo")
                else:
                    print(f"O numero da posição {numero_aleatorio} é par")
                dica+=1 
            if((dica==2)and (tent==4 or tent==2)):
                if(impar==1):
                    if(cont>5):
                        print(f"O numero da posição {numero_aleatorio} é maior que 5")
                    if(cont<5):
                        print(f"O numero da posição {numero_aleatorio} é menor que 5")
                    if(conti%2==0):
                        print(f"\nO numero da posição {numero_aleatorio} é par")
                    else:
                        print(f"O numero da posição {numero_aleatorio} é impar") 
                        impar+=1
                dica+=1 
        if((dica==2)and(tent==5 or tent==3)):
            if(impar==1):
                if(conti>5):
                    print(f"\nO numero da posição {numero_aleatorio} é maior que 5")   
                else:
                    print(f"\nO numero da posição {numero_aleatorio} é menor que 5")        
            else:
                if(conti<4):
                    print(f"\nO numero da posição {numero_aleatorio} é maior que 4")     
                else:
                    if(conti>6):
                        print(f"\nO numero da posição {numero_aleatorio} é menor que 6")       
            dica-=1
            impar-=1
        print(f"\n\t\t\t\t\tTentativa anterior: {num}")
        if(c1==-1):
            print(" _ ", end=" ")
        else:
            print(f" {c1} ", end=" ")
        if(c2==-2):
            print(" _ ", end=" ")
        else:
            print(f" {c2} ", end=" ")
        if(c3==-3):
            print(" _ ", end=" ")
        else:
            print(f" {c3} ", end=" ")
        if(c4==-4):
            print(" _ ")
        else:
            print(f" {c4} ")
        if (num==num_correto):
                print('Você acertou!')
                tent=11-tent
                print(f"\n\tAcertou em {tent} tentativas, muito bem!")
                break
        else:
            if (tent==1):
                print (f'\nVocê perdeu!')
                print(f'O codigo era {num_correto}')
    print(f"\t\nDeseja jogar novamente?")
    conti=int(input(f"\t\nPresione 1< para SIM e 0 para NÃO\t\n"))
    if(conti==1):
        jn+=1
    else:
        jn+=10000