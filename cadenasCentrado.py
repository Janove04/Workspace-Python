texto = "Este texto es para el ejemplo a realizar"

# Empieza y termina con
print(" La cadena empieza con ", texto.startswith("Este"))
print(" La cadena termina con ", texto.endswith("realizar"))

# Para alinear el texto:
# - Centrado
print(texto.center(80, '+')) # 80 son el número de caracteres en los que se centrar el texto
                             # y el + es con lo que se llena el resto de espacio para tener 80.
                             # Solo se acepta un caracter para poder centrar los textos.
# Saber la longitud de la cadena
longitudCadena = len(texto)
print(longitudCadena)  # Muestra que la cadena tiene 40 caracteres
print(texto.center(longitudCadena + 10, '-'))   # Aquí le añadimos 10 espacios más, los cuales 
                                                # se van a llenar con guiones, como se especifica en el segundo parámetro.    
# Cómo añadir caracteres por la izquierda y derecha de la cadena
print(texto.ljust(60, '-'))    # Imprime la cadena a la izquierda (l de left y just de justify) y rellena a la derecha con caracteres.
# Ahora imprime a la derecha y añade caracteres por la izquierda      
print(texto.rjust(60, '0'))

# Eliminar espacios en blanco
texto = "   Esto es una cadena con espacios en blanco y algunos caracteres raros *-$/-&3-\\j     "
print(texto)
print("- Cadena sin espacios: ")
print(texto.strip()) # Con strip se eliminan los espacios en blanco

# Sustituir algún carcter de la cadena
print(texto.replace("-", "hello")) # El primer parámetro es para indicar qué queremos 
                                   # sustituir y el segundo parámetro es con lo que 
                                   # lo vamos a sustituir, en este caso los - por un hello.
print(texto) # Aquí se imprime igual la cadena porque a pesar de haberla sustituido en la línea
             # anterior(29), no se afecta porque no se ha guardado la modificación en la variable.

textoModificado = texto.replace("-", "hey")    # Aquí ya se guardan directamente las modificaciones.
print(textoModificado)



                                        
                   