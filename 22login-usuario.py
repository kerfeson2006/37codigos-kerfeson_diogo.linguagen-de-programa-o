usuario = "kerfeson123"
senha = 12345678
usuario_cadast = str(input("digite seu usuario "))
senha_cadrast = int(input("digite sua senha "))
if usuario_cadast == usuario and senha_cadrast == senha:
 print ("acesso liberado")
else:
 print("acesso negado, usuario ou senha invalido!")