n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

Media = (n1*2 + n2*3 + n3*4 + n4*1) / 10

# aprovado com media igual ou maior que 7.0
if Media>=7 :
    print("Media: %.1f" %(Media))
    print("Aluno aprovado.")
else:
    # reprovado com media inferior a 5.0
    if Media<5.0:
        print("Media: %.1f" %(Media))
        print("Aluno reprovado.")

    # ficou de exame (nota entre 5.0 e 6.9)
    elif (5.0<=Media) and (Media<=6.9):
        # recebendo nota do examepr
        print("Media: %.1f" %(Media))
        print("Aluno em exame.")
        n_exam = float(input())
        print("Nota do exame: %.1f" %(n_exam))
        # recalculando media
        Media_Final = (Media + n_exam) / 2
        # reprovou mesmo com exame
        if(Media_Final>=5.0):
            print("Aluno aprovado.")
            print("Media final: %.1f" %(Media_Final))
        elif(Media_Final<=4.9):
            print("Aluno reprovado.")
            print("Media final: %.1f" %(Media_Final))