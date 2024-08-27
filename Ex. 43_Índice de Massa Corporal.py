#Estrutura
print("Vamos calcular seu Índice de Massa Corporal (IMC)?\nLembre-se sempre de consultar um especialista para confirmar sua condição!!!")

while True:
    try:
        peso = float(input("Digite seu peso em kg (Ex.: 65.2): "))
        altura = float(input("Digite sua altura em metros (Ex.: 1.65): "))
        if isinstance(peso,float) and isinstance(altura,float):
            imc = peso / (altura**2)
            if imc <= 18.5:
                print(f"Seu IMC é {imc:.2f} e indica que você está abaixo do peso ideal.")
            elif imc <= 24.9:
                print(f"Seu IMC é {imc:.2f} e indica que você está com o peso ideal.")
            elif imc <= 29.9:
                print(f"Seu IMC é {imc:.2f} e indica sobrepeso.")
            elif imc <= 34.9:
                print(f"Seu IMC é {imc:.2f} e indica obesidade grau I")
            elif imc <= 39.9:
                print(f"Seu IMC é {imc:.2f} e indica obesidade grau II")
            else:
                print(f"Seu IMC é {imc:.2f} e indica obesidade grau III")
            break
    except ValueError:
        print("Os valores inseridos são inválidos. Confirme as informações e tente novamente!")