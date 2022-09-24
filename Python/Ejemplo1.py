#Introducción Python en Sistemas de gestión empresarial

""" def hola(texto = "Juanito"):
    print('hola', texto)

hola()
print('La función se ha terminado') """

#################################################################################################################

##########Ejercicio 1

'''Pedir tres números por teclado y hacer suma resta y multiplicación usando funciones'''

def suma(a, b):
    return (a+b)
def resta(a, b):
    return (a-b)
def multiplicación(a, b):
    return (a*b)
def división(a, b):
    return (a/b)

#################################################################################################################

""" a = int(input('Introduce  1er número: ')) # Número 1
b = int(input('Introduce  2º número: ')) # Número 2

print('Suma:', suma(a, b))
print('Resta:', resta(a, b))
print('Multiplicación:', multiplicación(a, b))
print('División:', división(a, b))


if (a < b):
    print("a < b")
elif(a == b):
    print("a = b")
else:
    print("a > b") """

#################################################################################################################

'''Función fibonacci recursiva'''


def fibonacci(a):
    if(a == 0 or a == 1):
        return a
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)


a = int(input("Número al que calcularle fibonacci: "))
for i in range(a):
    print(fibonacci(i))

