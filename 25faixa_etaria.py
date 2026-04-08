nome = input ("informe sue nome: ")
idade = int(input("digite sua idade: "))
if idade < 12:
    print ("criança")
elif idade < 18:
 print("adolescente")
elif idade < 60:
 print ("adulto")
elif idade > 59:
  print("idoso")