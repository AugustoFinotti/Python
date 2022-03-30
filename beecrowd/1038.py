cod, qua = input().split()
cod = int(cod)
qua = int(qua)

if(cod == 1):
    T = qua * 4
    
elif(cod == 2):
    T = qua * 4.5
    
elif(cod == 3):
    T = qua * 5
    
elif(cod == 4):
    T = qua * 2
    
elif(cod == 5):
    T = qua * 1.5

print("Total: R$ %.2f" %(T))