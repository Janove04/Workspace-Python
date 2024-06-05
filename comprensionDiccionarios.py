# Ejemplo de la sintaxis que se usa para la comprension de diccionarios,
# a diferencia de las listas que usan [], para los diccionarios se usa {}
#nuevo_diccionario = {clave: valor for elemento in secuancia} --> clave es la clave del diccionario que vamos a crear y valor es el valor asociado a cada clave.
                                                    #   elemento es un elemento de la secuencia que proporcia las claves y valores.
                                                    #   secuencia es la fuente de los datos (lista, dupla o rango), en este caso una lista.
                                                    
# Vamos a crear un diccionario de cuadrados de los números de una lista
numeros = [1, 2, 3, 4, 5] # Creamos la lista
diccionario_cuadrados = {num: num**2 for num in numeros} # num es la clave, num**2 es el valor(en este caso al cuadrado usando **2)
print(numeros)
print(diccionario_cuadrados) # Muestra cada número y su cuadrado
print("*"*30)
# Ahora otro ejemplo de un diccionario para numeros pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
diccionario_pares = {num: num for num in numeros if num % 2 == 0}
print(numeros)
print(diccionario_pares)
print("*"*30)
# Ahora un ejemplo con cadenas de texto. Crear un diccionario de longitud de palabras de una lista de palabras
palabras = ["pyton", "sebas", "programacion"]
diccionario_longitudes = {palabra: len(palabra) for palabra in palabras}
print(diccionario_longitudes)
