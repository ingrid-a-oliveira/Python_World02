#Conversor de Bases Numéricas(Binário, octal e hexadecimal)
opcao = int(input("Escolha uma das opções para conversão: \n1- Binário\n2- Octal\n3- Hexadecimal\n4- Todas\nDigite sua escolha para conversão: "))
numero = int(input("Digite o número inteiro que deseja converter: "))

#Condições
if opcao == 1:
    print(f"O valor {numero} convertido para número binário é {bin(numero)[2:]}.")

elif opcao == 2:
    print(f"O valor {numero} convertido para octal é {oct(numero)[2:]}.")

elif opcao == 3:
    print(f"O valor {numero} convertido para hexadecimal é {hex(numero)[2:]}.")
    
elif opcao == 4:
    print(f'''O valor {numero} convertido em:
          Binário é {bin(numero)[2:]}
          Octal é {oct(numero)[2:]}
          Hexadecimal é {hex(numero)[2:]}''')

else:
    print("Opção inválida. Tente Novamente.")