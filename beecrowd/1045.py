V1, V2, V3 = input().split()
V1 = float(V1)
V2 = float(V2)
V3 = float(V3)
# colocando em ordem
# 1 2 3
if (V1>V2 and V2>V3):
    A = V1
    B = V2
    C = V3
# 1 3 2
elif (V1>V3 and V3>V2):
    A = V1
    B = V3
    C = V2
# 2 3 1 
elif (V2>V3 and V3>V1):
    A = V2
    B = V3
    C = V1
# 2 1 3
elif (V2>V1 and V1>V3):
    A = V2
    B = V1
    C = V3
# 3 1 2
elif (V3>V1 and V1>V2):
    A = V3
    B = V1
    C = V2
# 3 2 1
elif (V3>V2 and V2>V1):
    A = V3
    B = V2
    C = V1

# números repetidos
# 1 1 1 ou 3 3 3
elif(V1==V2)and(V1==V3):
    A = V3
    B = V2
    C = V1
# 3 3 1
elif(V1==V2) and (V1>V3):
    A = V1
    B = V2
    C = V3
# 3 1 3
elif(V3==V1) and (V3>V2):
    A = V3
    B = V1
    C = V2
# 1 3 3
elif(V3==V2) and (V3>V1):
    A = V3
    B = V2
    C = V1
# 3 1 1
elif(V2==V3) and (V1>V2):
    A = V1
    B = V2
    C = V3
# 1 3 1
elif(V1==V3) and (V2>V1):
    A = V2
    B = V1
    C = V3
# 1 1 3
elif(V1==V2) and (V3>V1):
    A = V3
    B = V1
    C = V2
    
# formando triangulos
if (A >= (B+C)):
    print("NAO FORMA TRIANGULO")
else:
    if (A**2 == B**2 + C**2):
        print("TRIANGULO RETANGULO")
    if(A**2 > B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
    if(A**2 < B**2 + C**2):
        print("TRIANGULO ACUTANGULO")
    if(A==B) and (A==C):
        print("TRIANGULO EQUILATERO")
    elif (A==B) or (B==C) or (C==A):
        print("TRIANGULO ISOSCELES")