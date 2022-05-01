# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 30/04/2022

# 13- Faca um algoritmo que calcule a media ponderada das notas de 3 provas.
# A primeira e a segunda prova tem peso 1 e a terceira tem peso 2.
# Ao final, mostrar a media do aluno e indicar se o aluno foi aprovado ou reprovado.
# A nota para aprovacao deve ser igual ou superior a 60 pontos.

# Input
p1 = float(input("Digite a nota da prova 1: "))
p2 = float(input("Digite a nota da prova 2: "))
p3 = float(input("Digite a nota da prova 3: "))
# Processing and Output
media = (p1 + p2 + (p3 * 2)) / 4
if(media >= 60):
    print("A média final do aluno(a) foi de %.2f, logo está aprovado(a)" %(media))
else:
    print("A média final do aluno(a) foi de %.2f, logo está reprovado(a)" %(media))