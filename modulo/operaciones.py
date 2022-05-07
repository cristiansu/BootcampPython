def sumar(a,b):
    try: 
        return a+b
    except ValueError:
        return 'Debe ingresar sólo números'

def resta(a,b):
    try: 
        return a-b
    except ValueError:
        return 'Debe ingresar sólo números'

def multiplicar(a,b):
    try: 
        return a*b
    except ValueError:
        return 'Debe ingresar sólo números'

def dividir(a,b):
    try:
        if b != 0:
            return a/b
        else:
            return 'No puede dividir por cero'
    except ValueError:
        return 'Debe ingresar sólo números'

    