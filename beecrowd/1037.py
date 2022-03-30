N = float(input())

# fora do intervalo
if N<0 or N>100:
    print("Fora de intervalo")
else:
    # entre 0 e 25
    if N>=0 and N<=25.0:
        print("Intervalo [0,25]")
    
    # entre 25 e 50
    elif N>25 and N<=50.0:
        print("Intervalo (25,50]")

    # entre 50 e 75
    elif N>50 and N<=75.0:
        print("Intervalo (50,75]")

    # entre 75 e 100
    elif N>75 and N<=100.0:
        print("Intervalo (75,100]")