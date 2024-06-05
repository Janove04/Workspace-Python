# Ejemplo de la sintaxis que se usa para crear las listas de comprensión
#nueva_lista = [expresion for elemento in secuancia] --> expresion es la operación o cálculo que se aplica a cada elemento.
                                                    #   elemento es la variable que representa cada elemento en la secuencia.
                                                    #   secuencia es la fuente de los datos (lista, dupla o rango), en este caso una lista.
                                                    
# Creamos una lista de los cuadrados de los números del 1 al 5 (manera tradicional y sencilla)
numeros = [1, 2, 3, 4, 5]
cuadrados = []
for numero in numeros: # Creamos este bucle para recorrer todos los números en la lista numeros
    cuadrados.append(numero**2) # **2 es para sacarle el cuadrado a los números
print('Los cuadrados son:', cuadrados)
print("*"*20) # Esto es solo para separar cómo se muestra en la consola
# Ahora el mismo ejemplo pero con comprensión de listas
cuadrados = [numero **2 for numero in numeros]
print(f"- Los cuadrados son: {cuadrados}")