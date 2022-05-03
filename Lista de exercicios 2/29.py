# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 03/05/2022

# 29 - Faca uma prova de matematica para criancas que estao aprendendo a somar numeros
# inteiros menores do que 100. Escolha numeros aleatorios entre 1 e 100, e mostre na tela a pergunta:
# qual e a soma de a + b, onde a e b sao os numeros aleatorios.
# Peca a resposta. Faca cinco perguntas ao aluno,
# e mostre para ele as perguntas e as respostas
# corretas, alem de quantas vezes o aluno acertou.

# Libraries
import random

# Processing and Output
i = 1
acertos = 0
print(" - - - Início da Prova - - -")
print("Boa prova!")
while(i<=5):
    print()
    a = random.randint(1,100) # função importada de uma biblioteca externapara gerar números inteiros aleatórioa té 100
    b = random.randint(1,100)
    soma =  a+b
    print("Quanto é %.2f + %.2f ?" %(a, b))
    resp = float(input("%.2f + %.2f = " %(a, b)))
    print()
    if(resp==soma):
        print("Parabéns você acertou!")
        print()
        acertos += 1 # incremento para somar os acertos depois
    else:
        print("Que pena, resposta errada!")
        print("A resposta correta era: %.2f" %(soma))
        print()
    i+=1 # incremento para o while
print("Fim da prova")
print("De 5 questões você acertou: %d" %(acertos))
print()