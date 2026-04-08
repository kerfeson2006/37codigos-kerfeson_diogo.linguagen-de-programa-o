valor = int(input("qual o valor do produto? "))
pagamento = input("qual a forma de pagamento? ")
if pagamento == "avista":
    desconto = valor * 10/100
    rest = valor - desconto
    print ("valor com desconto é;",rest,"reais")
elif pagamento == "parcelado":
    print("valor total de",valor,"reais")
elif  pagamento != "avista and parcelado":
    print ("não aceitamos esta forma de pagamento!")