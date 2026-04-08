ano_atual = 2026
ano = int(input("que ano voçê nasceu? "))
ja_fez = str(input("voçê ja fez aniversario esse ano? (s/n) "))
idade = ano_atual - ano
if ja_fez =="n":
    idade -=1
    print (" sua idade é ",idade,"anos")
else:
    print("sua idade é",idade,"anos")