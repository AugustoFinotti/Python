sal_ini = float(input())

if (0 < sal_ini <= 400.00):
    reaj_perc = 15
elif(400.01 <= sal_ini <= 800.00):
    reaj_perc = 0.12
elif(800.01 <= sal_ini <= 1200.00):
    reaj_perc = 10
elif(1200.01 <= sal_ini <= 2000.00):
    reaj_perc = 7
else:
    reaj_perc = 4

reaj_liq = sal_ini * (reaj_perc/100)
sal_fin = sal_ini + reaj_liq

print("Novo salario: %.2f" %(sal_fin))
print("Reajuste ganho: %.2f" %(reaj_liq))
perc_simb = "%"
print("Em percentual: %d %s" %(reaj_perc, perc_simb))