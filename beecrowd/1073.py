n = int(input())
if(n%2==0):
    final = n+1
else:
    final = n
for x in range(2,final,2):
    print("%d^2 = %d" %(x, x*x))