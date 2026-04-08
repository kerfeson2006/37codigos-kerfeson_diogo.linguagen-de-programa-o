km_corrida = float(input("quantos quilometros foram percorridos? "))
if km_corrida <= 5:
    print("valor da corrida é 10 reais")
elif km_corrida <= 10:
    print("o valor da corrida é 20 reais")
elif km_corrida <= 20:
    print("o valor da corrida é 30 reais")
elif km_corrida > 20:
    print("o valor da corrida é 50 reais")