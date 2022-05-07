# lista=[]
# asignatura=input('ingrese asignatura')
# lista.append(asignatura)
# print(asignatura)

#-----ejercicio2---------------------
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado 
# en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> 
# donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes 
# notas introducidas por el usuario

# asig=['matemáticas', 'física', 'program']
# notas=[]


#-------ejercicio3-------------------
# Escribir un programa que almacene en una lista los siguientes precios, 
# 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

# lista=[50, 75, 46, 22, 80, 65, 8]
# menor = min(lista)
# mayor = max(lista)
# print('menor;',menor,'y mayor: ',mayor)


#---------ejercicio 4 -----edad

# edad=int(input('Ingrese su edad: '))
# if edad >= 18:
#     print('Ud es mayor de edad')
# else:
#     print('Ud es menor de edad')

#---------ejercicio 5 -----claves

# pw = ['clave1', 'clave2', 'clave3']
# clave = input('ingrese su clave: ')

# for c in pw:
#     if c == clave.lower:
#         print('clave correcta')
#     else:
#         print('clave incorrecta')

#---------ejercicio 6 -----división

# num1 = int(input('ingrese un número: '))
# num2 = int(input('ingrese un otro número: '))

# if num2 == 0:
#     print('error')
# else:
#     resul=(num1/num2)
#     print(resul)

#-----ejercicio7-----------
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está 
# en el diccionario.

# div={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

# preg=input('Ingrese divisa: ')

# for k,v in div.items():
#     if preg == div[k]:
#         print(div[k])
#     else:
#         print('no registrado')


#----------funcion iva---

# def factura(monto, iva=19):
#     neto = monto
#     iva = monto*(iva/100)
#     bruto= monto+iva
#     return bruto

# monto = int(input('ingrese monto: '))
# iva = int(input('ingrese iva: '))

# print('el monto bruto de la factura es: ', factura(monto,iva))

#----------ejercicio funcion listas cuadrados
#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

# def cuadrados(lista):
#     lc=[]
#     for i in lista:
#         c=i**2
#         lc.append(c)
#     return lc

#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. 
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra 
# más repetida y su frecuencia.

#Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y 
# logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla 
# con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos entero

# from math import sin, cos, tan, exp, log


# def calculadora(operacion, x):
#     if operacion == 'sin':
#         res=sin(x)
#     elif operacion == 'cos':
#         res=cos(x)
#     elif operacion == 'tan':
#         res=tan(x)
#     elif operacion == 'exp':
#         res=exp(x)
#     elif operacion == 'log':
#         res=log(x) 
#     return res       



# operacion = input('ingrese operacion: ')
# x = float(input('ingrese valor: '))

# print('el resultado es: ', calculadora(operacion, x))


#Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene
#  y su longitud.

frase = input('Ingrese frase: ')
dic = {}

def palabra(frase):
    for i in frase.split():
        long=len(i)
        dic[i]=long
    return dic

print(palabra(frase))
    
