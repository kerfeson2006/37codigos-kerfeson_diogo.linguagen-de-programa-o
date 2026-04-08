nome = input("digite seu nome: ")
nota = float(input("digite sua nota: "))
if nota >=9:
    print ("aprovado com exeslencia")
elif nota >=6:
    print("aprovado")
elif nota >= 4:
    print("recuperação")
else:
    print("reprovado")