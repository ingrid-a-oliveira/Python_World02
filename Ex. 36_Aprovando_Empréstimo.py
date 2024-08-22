#Avaliação de empréstimo para compra de casa

#Informações para Análise
print("Vamos simular o empréstimo para a realização de um sonho?\nPrecisamos de poucas informações para dar andamento no seu pedido!")
valor_casa = float(input("Digite o valor da casa que deseja comprar: R$"))
anos_pagamento = int(input("Em quantos anos deseja pagar o empréstimo? "))
salario_base = float(input("Qual sua renda mensal? R$ "))
valor_parcela = valor_casa/(anos_pagamento*12)
valor_maximo_parcela = salario_base*0.3

#Condições Aninhadas
if valor_parcela <= valor_maximo_parcela:
    print(f"O empréstimo pode ser concedido.\nO valor da parcela será de R${valor_parcela:.2f} em {anos_pagamento*12} meses")
else:
    print(f"Infelizmente o empréstimo não poderá ser liberado nessas condições.\nA parcela ficaria com o valor de {valor_parcela:.2f} e excede 30% de sua renda bruta.")
