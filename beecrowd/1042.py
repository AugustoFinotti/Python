v1, v2, v3 = input().split()
v1 = int(v1)
v2 = int(v2)
v3 = int(v3)
# 1 2 3
if(v1>v2) and (v2>v3):
    print(v3)
    print(v2)
    print(v1)
    print()
    print(v1)
    print(v2)
    print(v3)
# 2 1 3
elif(v2>v1) and (v1>v3):
    print(v3)
    print(v1)
    print(v2)
    print()
    print(v1)
    print(v2)
    print(v3)
# 1 3 2
elif(v1>v3) and (v3>v2):
    print(v2)
    print(v3)
    print(v1)
    print()
    print(v1)
    print(v2)
    print(v3)
# 2 3 1
elif(v2>v3) and (v3>v1):
    print(v1)
    print(v3)
    print(v2)
    print()
    print(v1)
    print(v2)
    print(v3)
# 3 1 2
elif(v3>v1) and (v1>v2):
    print(v2)
    print(v1)
    print(v3)
    print()
    print(v1)
    print(v2)
    print(v3)
# 3 2 1
else:
    print(v1)
    print(v2)
    print(v3)
    print()
    print(v1)
    print(v2)
    print(v3)