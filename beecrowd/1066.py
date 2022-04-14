# Entrada
v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())

# declarando várias variáveis de uma vez só
n_pa, n_im, n_po, n_ne = 0, 0, 0, 0

#  - - Processamento
# par ou impar
if(v1%2) == 0:
    n_pa = n_pa +1
else:
    n_im = n_im +1
if(v2%2) == 0:
    n_pa = n_pa +1
else:
    n_im = n_im +1
if(v3%2) == 0:
    n_pa = n_pa +1
else:
    n_im = n_im +1
if(v4%2) == 0:
    n_pa = n_pa +1
else:
    n_im = n_im +1
if(v5%2) == 0:
    n_pa = n_pa +1
else:
    n_im = n_im +1

# negativo ou positivo
if (v1>0) and  (v1!=0):
    n_po = n_po +1
elif(v1!=0)and(v1<0):
    n_ne = n_ne +1
if (v2>0) and  (v2!=0):
    n_po = n_po +1
elif(v2!=0)and(v2<0):
    n_ne = n_ne +1
if (v3>0) and  (v3!=0):
    n_po = n_po +1
elif(v3!=0)and(v3<0):
    n_ne = n_ne +1
if (v4>0) and  (v4!=0):
    n_po = n_po +1
elif(v4!=0)and(v4<0):
    n_ne = n_ne +1
if (v5>0) and  (v5!=0):
    n_po = n_po +1
elif(v5!=0)and(v5<0):
    n_ne = n_ne +1
# Saída
print("%d valor(es) par(es)" %(n_pa))
print("%d valor(es) impar(es)" %(n_im))
print("%d valor(es) positivo(s)" %(n_po))
print("%d valor(es) negativo(s)" %(n_ne))