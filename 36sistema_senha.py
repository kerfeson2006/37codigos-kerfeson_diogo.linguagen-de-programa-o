senha_correta = "1234"
tentativas = 3

while tentativas > 0:
    senha = input("digite a senha: ")

    if senha == senha_correta:
        print("acesso liberado")
        break
    else:
        tentativas -= 1
        print(f" senha incorreta! tentativas restantes : {tentativas}")

if tentativas == 0:
    print("acesso bloqueado")