A, B, C = input().split()
A = float(A)

if(A==0):
    print("Impossivel calcular")
else:
    B = float(B)
    C = float(C)

    delta = B**2 - (4*A*C)
    
    if(delta<0):
        print("Impossivel calcular")
    else:
    
        R1 = (-B + delta**0.5) / (2*A)
        R2 = (-B - delta**0.5) / (2*A)

        print("R1 = %.5f" %(R1))
        print("R2 = %.5f" %(R2))