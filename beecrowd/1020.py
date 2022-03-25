N = int(input())

A = N // 365
N = N % 365
M = N // 30
N = N % 30
D = N

print("%d ano(s)"  %(A))
print("%d mes(es)" %(M))
print("%d dia(s)" %(D))