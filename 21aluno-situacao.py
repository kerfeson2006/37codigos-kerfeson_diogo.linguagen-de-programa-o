nome = input("informe seu nome: ")
nota1 = float(input("informe sua primeira nota: "))
nota2 = float(input("informe sua segunda nota: "))
nota3 = float(input("informe sua terceira nota: "))
media = (nota1 + nota2 + nota3)/3
if media >= 7:
 print ("sua media é",media)
 print (nome," voçê está aprovado")
elif media >=4:
 print ("sua media é",media)
 print (nome,"voçê esta em recuperação")
else:
 print ("sua media é",media)
 print(nome," voçê está reprovado")