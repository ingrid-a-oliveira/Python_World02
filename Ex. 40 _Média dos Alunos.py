#Dados - Médias Anuais e possíveis dois trabalhos extras
media_01 = float(input("Digite a média do primeiro bimestre: "))
media_02 = float(input("Digite a média do segundo bimestre: "))
media_03 = float(input("Digite a média do terceiro bimestre: "))
media_04 = float(input("Digite a média do quarto bimestre: "))
trabalhos = str(input("Os alunos fizeram trabalhos extras? ")).lower()

#condições
if trabalhos == "sim":
    trabalho_01 = float(input("Digite a pontuação do trabalho 01: "))
    trabalho_02 = float(input("Digite a pontuação do trabalho 02: "))
    media_trabalhos = (trabalho_01 + trabalho_02)/2
else:
    print("Como não tivemos trabalhos extras, vamos calcular as médias!")
    media_trabalhos = 0
    
#cálculo de média
media_provas = (media_01 + media_02 + media_03 + media_04)
media_total = media_provas + media_trabalhos

#condições e resultados
if media_total < 14:
    print(f"Sua média anual foi de {media_total:.2f} e você está reprovado, deverá refazer essa matéria em DP no próximo ano!")
elif media_total > 14 and media_total < 24:
    print(f"Sua média anual foi de {media_total:.2f} e você deverá tentar recuperar sua nota com uma prova de recuperação!")
else:
    print(f"Parabéns. Sua média foi de {media_total:.2f} e você está aprovado!")