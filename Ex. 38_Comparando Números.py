#Comparando números entre maior, menor e igual
print("Para esse exercício precisamos digitar dois números!")
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

#Condições
if primeiro_numero > segundo_numero:
    print(f"O número {primeiro_numero} foi o maior valor inserido.")

elif segundo_numero > primeiro_numero:
    print(f"O número {segundo_numero} foi o maior valor inserido")
    
else:
    print("Ná há valor maior, os valores são iguais!")