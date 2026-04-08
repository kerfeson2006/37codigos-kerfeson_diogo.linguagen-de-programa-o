valor = float(input("digite o valor: "))

if valor <= 100:
    print ("sem desconto")
elif valor <= 500:
    print("5% de desconto")
elif valor <= 1000:
    print("10% de desconto")
elif valor > 1000:
    print("15% de desconto")
