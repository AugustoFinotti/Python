# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 02/05/2022

# 7- Faca um programa que leia 10 inteiros positivos, ignorando nao positivos, e imprima sua media. 

i = 1
q_pos = 0
soma = 0
while(i<=10):
    n = int(input("Digite um número inteiro: "))
    if(n>0):
        soma = soma + n
        q_pos += 1
    i +=1
media = soma / q_pos
print("A média dos números positivos resulta em: %.2f" %(media))