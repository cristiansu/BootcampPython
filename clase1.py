#**************calcular la suma de 15 primeros números con fórmula*******************

# n = 15
# suma = (n*(n+1))/2
# print(suma)




#**************calcular la suma de 15 primeros números con listas y rangos*******************
num = []
suma = 0
for i in range(16):
    num.append(i)
for j in num:
    suma += num[j]

print(suma)