# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 05/05/2022

# 34 - Leia a nota e o numero de faltas de um aluno, e escreva seu conceito. De acordo com a tabela abaixo,
# quando o aluno tem mais de 20 faltas ocorre uma reduco de conceito.
#
#     NOTA       |   CONCEITO (ATE 20 FALTAS)    |   CONCEITO (MAIS DE 20 FALTAS)
#  9.0 ate 10.0                A                                 B
#  7.5 ate 8.9                 B                                 C
#  5.0 ate 7.4                 C                                 D
#  4.0 ate 4.9                 D                                 E
#  0.0 ate 3.9                 E                                 E

# Input
nota_ini = float(input("Digite a nota de um aluno: "))
faltas = int(input("Digite o número de faltas: "))
# Processing and Output
if(faltas>20):    #  caso as faltas sejam maiores q 20 (reduz a nota)

    if(nota_ini>=9) and (nota_ini<=10):      #  9.0 ate 10.0
        nota_fin = "B"
    elif(nota_ini>=7.5) and (nota_ini<=8.9): #  7.5 ate 8.9
        nota_fin = "C"
    elif(nota_ini>=5.0) and (nota_ini<=7.4): #  5.0 ate 7.4
        nota_fin = "D"
    elif(nota_ini>=4.0) and (nota_ini<=4.9): #  4.0 ate 4.9
        nota_fin = "E"
    elif(nota_ini>=3.9) and (nota_ini<=0.0): #  0.0 ate 3.9
        nota_fin = "E"
    else: # nota_ini < 0 (não existe nota negativa)
        print("Nota inválida!")

elif(faltas<=20) and (faltas>=0): #  caso as faltas sejam menores q 20 (não reduz a nota)

    if(nota_ini>=9) and (nota_ini<=10):      #  9.0 ate 10.0
        nota_fin = "A"
    elif(nota_ini>=7.5) and (nota_ini<=8.9): #  7.5 ate 8.9
        nota_fin = "B"
    elif(nota_ini>=5.0) and (nota_ini<=7.4): #  5.0 ate 7.4
        nota_fin = "C"
    elif(nota_ini>=4.0) and (nota_ini<=4.9): #  4.0 ate 4.9
        nota_fin = "D"
    elif(nota_ini>=3.9) and (nota_ini<=0.0): #  0.0 ate 3.9
        nota_fin = "E"
else: # faltas < 0 (não existe número de falta negativa)
    print("Números de faltas inválido!")

print("Conceito Final: %s" %(nota_fin))