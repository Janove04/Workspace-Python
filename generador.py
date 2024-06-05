# Crear mis propios generadores
def impares():      # Con este comando se crea una función
    for numero in range(1, 50, 2): # Rango de 1 al 49, cada dos números (porque se busca los impares)
        yield numero # Es como un "return". Devuelve uno a uno el número en el rango, depende del que 
                     # uno le inidque con el next.
             
generador = impares()
print(next(generador))  # El comando next sirve para llamar la función y se imprime uno a uno el 
print(next(generador))  # siguiente número del generador con ayuda del yield
print(next(generador))
print(next(generador))
print(next(generador))
print("Terminando next uno a uno y pasamos a bucle for")
for numero in generador:  # Aquí el ciclo for continúa con el siguiente número después de la última
    print(numero)         # llamada del next, esto también gracias al yield.