n = int(input())
final = n+1
for x in range(1,final):
    v1, v2, v3 = input().split()
    v1, v2, v3 = float(v1), float(v2), float(v3)
    media = (v1*2 + v2*3 + v3*5)/10
    print("%.1f" %(media))