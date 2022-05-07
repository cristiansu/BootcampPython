def leer_numero(ini,fin,msj,num):
    try: 
        continuar=True
        while (continuar):
            num=int(input('Ingrese número: '))
            if num>=ini and num<=fin:
                print(f'{num}-{msj}') 
                continuar = True
            else: 
                print(f'{num} está fuera de rango')
                continuar = False
    except ValueError:
        print('Debe ingresar sólo números')



    
    
    

        

