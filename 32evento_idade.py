idade = int(input("informe sua idade: "))
ingresso = input("voçê tem ingresso? sim/nao ")
if ingresso == "nao":
    print("acesso negado")
elif idade >= 18: 
     print ("acesso permitido")
else:
   print("acesso restrito")