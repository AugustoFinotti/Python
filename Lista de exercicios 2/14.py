# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 14- A nota final de um estudante e calculada a partir de tres notas atribuıdas entre o intervalo de 0 ate 10, respectivamente,
# a um trabalho de laboratorio, a uma avaliacao semestral e a um exame final. A media das tres notas mencionadas anteriormente obedece aos pesos:
# Trabalho de Laboratorio: 2; Avaliacao Semestral: 3; Exame Final: 5.
# De acordo com o resultado, mostre na tela se o aluno esta reprovado (media entre 0 e 2,9)
# de recuperacao (entre 3 e 4,9) ou se foi aprovado. Faca todas as verificacoes necessarias. 

# Input
p1 = float(input("Digite a nota do trabalho de laboratório: "))
p2 = float(input("Digite a nota da avaliação semestral: "))
p3 = float(input("Digite a nota do exame final: "))
# Processing and Output
media = ((p1*2)+ (p2*3) + (p3*5)) /10
if(media >= 5.0):
    print("Aluno(a) aprovado(a)!")
elif(media >= 3) and (media <= 4.9):
    print("Aluno(a) de recuperação!")
else:
    print("Aluno(a) reprovado(a)")