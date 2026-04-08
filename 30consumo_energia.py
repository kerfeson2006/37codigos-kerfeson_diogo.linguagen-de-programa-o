consumo = float(input("informe o consumo? "))
if consumo <=100:
    print("tarifa básica")
elif consumo <=200:
    print("tarifa média")
else:
    print("tarifa alta")