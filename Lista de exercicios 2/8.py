# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 30/04/2022

# 8- Faca um programa que leia 2 notas de um aluno, verifique se as notas sao validas e
# exiba na tela a media destas notas. Uma nota valida deve ser, obrigatoriamente, um
# valor entre 0.0 e 10.0, onde caso a nota nao possua um valor valido, este fato deve ser
# informado ao usuario e o programa termina.

# Input
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
# Processing and Output
if(nota1 >= 0.0) and (nota1 <= 10.0) and (nota2 >= 0.0) and (nota2 <= 10.0):
    media = (nota1 + nota2) /2
    print("A média desse aluno é de: %.2f" %(media))
else:
    print("Notas inválidas!")
