unidade = int (input("quantas unidades?: "))

if unidade <= 10:
 print("preço normal")
elif unidade <= 20:
 print("10% de desconto")
elif unidade > 20:
 print("20% de desconto")
