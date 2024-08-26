#Estrutura
from datetime import datetime
print("Bem vindo à Confederação Nacional de Natação!\nVamos verificar em que categoria você se enquadra?")
nome = input("Digite seu nome completo: ").title().split()
primeiro_nome = nome[0]
print(f"Seja muito bem vindo(a) {primeiro_nome}!")

#idade
# idade = int(input("Digite sua idade: "))
while True:
    try:     
        ano_nascimento = int(input("Digite o ano do seu nascimento: "))
        if ano_nascimento > 1 and ano_nascimento < datetime.now().year:
            idade = datetime.now().year - ano_nascimento
            break
        else: 
            print(f"{primeiro_nome}, o ano de nascimento deve ser um número válido entre 1 e {datetime.now().year - 1}.")
    except ValueError:
        print(f"{primeiro_nome}, o ano de nascimento deve ser composto apenas por números inteiros. Tente novamente!")

#Condições
if idade <= 9:
    print(f"{primeiro_nome}, você faz parte da categoria ''MIRIM''! Será necessária a presença de um responsável para sua inscrição!")
elif idade <= 14:
    print(f"{primeiro_nome}, você faz parte da categoria ''INFANTIL''! Será necessária a presença de um responsável para sua inscrição!")
elif idade <= 19:
    print(f"{primeiro_nome}, você faz parte da categoria ''JÚNIOR''! Verifique em nosso site os documentos necessários para sua inscrição!")
elif idade <= 25:
    print(f"{primeiro_nome}, você faz parte da categoria ''SÊNIOR''! Verifique em nosso site os documentos necessários para sua inscrioão!")
else:
    print(f"{primeiro_nome}, você faz parte da categoria ''MASTER''! Verifique em nosso site os documentos necessários para sua inscrição!")