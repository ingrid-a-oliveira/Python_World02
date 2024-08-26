#Dados
import datetime
print("Vamos verificar sua situação com relação ao alistamento militar!!!")
ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = datetime.datetime.now().year
idade = (ano_atual-ano_nascimento)
if idade < 18:
    print(f"Você tem {idade} anos, ainda faltam {18-idade} ano(s) para o período de alistamento.")
elif idade == 18:
    print(f"Você tem {idade} anos, deverá comparecer com os documentos solicitados para realizar o alistamento!")
else:
    print(f"Você tem {idade}, faz {idade-18} ano(s) que você deveria ter comparecido para o alistamento. Busque o setor responsável para verificar sua situação!")