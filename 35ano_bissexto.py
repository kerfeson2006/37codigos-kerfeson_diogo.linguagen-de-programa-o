ano = int(input("digite o ano que desja verificar: "))
if (ano % 400 == 0):
  print("possivel bissexto")
elif (ano % 100 ==0):
  print(" ano não é bissexto")
elif (ano % 4 ==0):
  print ("ano é bissexto")