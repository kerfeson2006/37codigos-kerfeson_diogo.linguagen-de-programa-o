nome = input("digite seu nome: ")
idade = int(input("informe sua idade:"))
valor_emprest = float(input("qual o valor do emprestimo? "))
renda_mensal = float(input("qual o valor da sua renda mensal? "))
parcelas = int(input("em quantas parcelas pretende pagar? "))
valor_parcelas = valor_emprest / parcelas
if idade <18:
    print("emprestimo negado, idade minima exigida não atendida!")
elif parcelas > 22:
    print("emprestimo negado, quantidades de parcelas muito longp")
elif valor_parcelas > (renda_mensal/2):
    print(valor_parcelas,"emprestimo negado, tente um valor menor!")
else:
    print("emprestimo aprovado!, valor da parcela",valor_parcelas)