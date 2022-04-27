#  - - - - - Exercício 40 - - - - - #
custo_ini = float(input("Digite o custo: "))

# imposto
if(custo_ini <= 12000.00):
    custo_fin = custo_ini + (custo_ini * 0.05) # comissão = 0
elif(custo_ini <= 25000.00):
    custo_fin = custo_ini + (custo_ini * 0.1) + (custo_ini * 0.15)
else:
    custo_fin = custo_ini + (custo_ini * 0.15) + (custo_ini * 0.20)

print("Custo Consumidor: %.2f" %(custo_fin))