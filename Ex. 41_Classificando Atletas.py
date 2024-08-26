#Estrutura
print("Bem vindo à Confederação Nacional de Natação!\nVamos verificar em que categoria você se enquadra?")
nome = input("Digite seu nome completo: ").title().split()
primeiro_nome = nome[0]
print(f"Seja muito bem vindo(a) {primeiro_nome}!")
idade = int(input("Digite sua idade: "))

#Condições
if idade <= 9:
    print(f"{primeiro_nome}, você faz parte da categoria ''MIRIM''! Será necessária a presença de um responsável para sua inscrição!")
elif idade <= 14:
    print(f"{primeiro_nome}, você faz parte da categoria ''INFANTIL''! Será necessária a presença de um responsável para sua inscrição!")
elif idade <= 19:
    print(f"{primeiro_nome}, você faz parte da categoria ''JÚNIOR''! Verifique em nosso site os documentos necessários para sua inscrição!")
elif idade <= 25:
    print(f"{primeiro_nome}, você faz parte da categoria ''SÊNIOR''! Verifique em nosso site os documentos necessários para sua inscrioão!")
elif idade > 25:
    print(f"{primeiro_nome}, você faz parte da categoria ''MASTER''! Verifique em nosso site os documentos necessários para sua inscrição!")
else:
    print(f"{primeiro_nome}, tivemos um problema! Verifique se a idade inserida consta apenas valores numéricos e tente novamente!")