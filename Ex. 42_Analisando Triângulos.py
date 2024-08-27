#Estrutura
print("Vamos analisar um triângulo? Ele pode ser equilátero, isósceles e escaleno.\nVamos precisar inserir 3 comprimentos e verificar se eles formam um triângulo.")
lado_01 = float(input("Digite o primeiro lado do triângulo: "))
lado_02 = float(input("Digite o segundo lado do triângulo: "))
lado_03 = float(input("Digite o terceiro lado do triângulo: "))

#Verificando se os comprimentos formam um triângulo
while True:
    if lado_01 + lado_02 > lado_03 and lado_02 + lado_03 > lado_01 and lado_01 + lado_03 > lado_02:
        print("Os comprimentos formam um triângulo, podemos continuar!")
        break
    else:
        print("Os comprimentos não formam um triângulo, tente novamente!")
        lado_01 = float(input("Digite o primeiro lado do triângulo: "))
        lado_02 = float(input("Digite o segundo lado do triângulo: "))
        lado_03 = float(input("Digite o terceiro lado do triângulo: "))
        
#Verificando tipo de triângulo
if lado_01 == lado_02 == lado_03:
    print("O triângulo é EQUILÁTERO, ou seja, possui todos os lados iguais.")
elif lado_01 == lado_02 and lado_01 != lado_03 or lado_02 == lado_03 and lado_02 != lado_01 or lado_03 == lado_01 and lado_03 != lado_02:
    print("O triângulo é ISÓSCELES, ou seja, possui dois lados iguais.")
else:
    print("O triângulo é ESCALENO, ou seja, todos os lados são diferentes.")