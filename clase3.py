# import sys

# if len(sys.argv) == 3:
#     text=sys.argv[1]
#     rep=int(sys.argv[2])

#     for r in range(rep):
#         print(text)

# else:
#     print('Error cantidad insuficiente argumentos')



# nombre=input('ingrese nombre: ')
# edad=int(input('ingrese edad: '))

# try:

#     if edad <18:
#         print(f'{nombre} eres menor de edad')
#     else:
#         print(f'{nombre} eres mayor de edad')

# except:
#     print('Error en dato ingresado')



# num1=int(input('ingrese un número: '))
# num2=int(input('ingrese otro número: '))

# def sum(a,b):
#     try:
#         res=a+b
#         return res
#     except:
#         return print('error en dato ingresado')


# print(sum(num1,num2))

# vi=int(input('ingrese velocidad inicial: '))
# t=float(input('ingrese tiempo en segundos: '))


# def vf(v,t):
#     g=9.8
#     vf=vi+g*t
#     return vf

# print('La velocidad final es: ', vf(vi,t))



# num1=int(input('ingrese un número: '))
# num2=int(input('ingrese otro número: '))

# def oper(a,b):
#     suma=a+b
#     resta=a-b
#     mult=a*b
#     return f'suma: {suma} - resta: {resta} - multiplicación: {mult}'

# print(oper(num1,num2))

# lpp=[5.5,4,7]
# ep=float(input('ingrese nota examen parcial: '))
# ef=float(input('ingrese nota examen final: '))

# def notaf(lpp,ep,ef):
#     sum=0
#     for i in lpp:
#         sum += i
#     pp=sum/len(lpp)

#     nf=(pp+2*ep+3*ef)/6

#     return f'la nota final es: {nf}'

# print(notaf(lpp,ep,ef))


# num1=int(input('ingrese un número: '))
# num2=int(input('ingrese otro número: '))

# def div(a,b):
#     if b>0:
#         res=a/b
#     elif b==0:
#         return 'Error: num2 no puede ser cero'
#     return res

# print(div(num1,num2))



    
# num1=int(input('ingrese id dato buscado: '))
# lista=[1,2,3,4,5]


# def dato(lista,a):   
#     datos=len(lista)
#     if a <= datos:
#         res=lista[num1]
#     else:
#         return 'Id no existe'
#     return res

# print(dato(lista, num1))

from modulo.operaciones import *

try:
    num1=int(input('ingrese un número: '))
    num2=int(input('ingrese otro número: '))
    print(sumar(num1,num2))
    print('--------------------------')
    print(resta(num1,num2))
    print('--------------------------')
    print(multiplicar(num1,num2))
    print('--------------------------')
    print(dividir(num1,num2))
    print('--------------------------')

except ValueError:
    print('Error sólo admite números')



