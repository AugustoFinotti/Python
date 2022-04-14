bruto = float(input())

if (bruto <= 2000.00):
    imp_total = 0
    print('Isento')
    
if (2000.00 < bruto) and (bruto <= 3000.00):
    imp_total = (bruto - 2000.00) * (8 / 100)
    
if (3000.00 < bruto) and (bruto <= 4500.00):
    imp8 = (8 / 100) * (1000.00)
    imp_total = (bruto - 3000.00) * (18 / 100) + imp8
    
if (bruto > 4500.00):
    imp8 = (8 / 100) * (1000.00)
    imp18 = (18 / 100) * (1500.00)
    imp_total = (bruto - 4500.00) * (28 / 100) + imp8 + imp18

if bruto > 2000.00:
    print("R$ %.2f" %(imp_total))