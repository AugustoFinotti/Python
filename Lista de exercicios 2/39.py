# - - - - - Exercício 39 - - - - - #

sal_ini = float(input("Salário: "))
anos = float(input("Tempo: "))

# calculando o reajuste
if(sal_ini <= 500.00):
    sal_rea = sal_ini * 1.25

elif (sal_ini <= 1000.00):
    sal_rea = sal_ini * 1.20 

elif (sal_ini <= 1500.00):
    sal_rea = sal_ini * 1.15

elif (sal_ini <= 2000.00):
    sal_rea = sal_ini * 1.10

else:
    sal_rea = sal_ini

# calculando o bônus
if(anos < 1):
    bonus = 0

elif(anos <= 3):
    bonus = 100.00

elif(anos <= 6):
    bonus = 200.00

elif(anos <= 10):
    bonus = 300.00

else:       
    bonus = 500.00

sal_fin = sal_rea + bonus

# saída
if(sal_rea == sal_ini) and (bonus > 0):
    sal_fin = sal_ini + bonus
    print("Salário Reajustado: %.2f" %(sal_fin))

elif(bonus == 0) and (sal_rea == sal_ini):
    print("Funcionário não tem direito a aumento.")

elif(bonus == 0):
    print("Funcionário não tem direito a bônus.")

else:
    print("Salário Reajustado: %.2f" %(sal_fin))