    # Algunos ejemplos extra con ciclo For
lista_colores = ['Rojo','Amarillo','Azul','Verde']
mi_color = 'Azul'  # Esto es por si quiero encontrar un color en específico
for color in lista_colores:
    print(color)
    if color == mi_color:
        print(' ¡Color encontrado!')
        break # Para salir del bucle una vez haya encontrado el color
    else:
        print(' El color indicado no está en la lista')
else:
    print(' He terminado de recorrer la lista')

rango_largo = range(1, 10000)
print(rango_largo)
for numero in rango_largo:
    print(numero)
    if numero == 8:
        print(f' Encontrado el número {numero}')
        break
else:
    print(' No he encontrado el número indicado')