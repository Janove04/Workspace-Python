print('Mi primer programa en Python')
print("     Tipos de Datos")
print("Tipo entero")
print(type(23))
print("Tipo decimal")
print(type(12.34))
print("Tipo cadena o texto")
print(type("holi"))
print("Tipo booleano")
print(type(False))
# El numeral se usa para poner comentarios.

# Ejemplos con las cadenas (texto).
print("Hola, "+" amigos!")
print("Saludo"*4) # Muestra el string 4 veces
variable = "cadena en variable"
variable = "Sumo esto a "+variable
print(variable) # ahora quedará "Sumo esto a cadena en variable"
print(variable[3]) # Muestra el índice número 3 (contando a desde el cero)
print(variable[-1]) # Empieza a contar desde el final
print(variable[2:6]) # Imprime desde el índice 2 (en este caso la letra m) hasta el 6 (letra s)
                     # pero el sexto índice (osea la letra s) no se muestra, solo imprime hasta el quinto
variable2 = "Sebastian"
print(variable2[4]) # Muestra la letra S ya que es el cuarto caracter (se cuenta desde 0 y los espacios también se cuentan)
print(variable2[-2]) # El índice negativo lo toma del final hasta el inicio
                        # en este caso sería la penúltima letra (A) de Sebastián
print(variable2[2:6])  # En este caso se imprime bast porque el índice 6 (o el final) no se incluye.                      
print(len(variable2)) # Imprime la longitud de la cadena (texto) en este caso 9 letras.
print(variable2.upper()) # Imprime todo en mayúscula.
print(variable2.lower()) # Imprime todo en minúscula.
print("Prueba".upper()) # Ejemplo poniendo un string directamente en el print.
print(variable2.capitalize()) # Imprime solo la primera en mayúscula.
cadena = "     Esto es una cadena  con      muchos   espacios  "
print(cadena)
print(cadena.strip()) # Le quita los espacios en blanco por detrás y por delante.

# Reemplazar valor
cadena2 = "Esto es un texto sin reemplazar"
print(cadena2)
print(cadena2.replace("sin reemplazar","remmplazado :)")) # Replace reemplaza el valor seleecionado específicamente por el valor deseado  

# Operadores lógicos
# Suma  +
# Resta -
# Multiplicación *
# División Entera //  (da como resultado la parte entera de la cifra)
# Exponencial 5**3 cinco elevado a la 3 = 125 (cinco al cubo)
# Módulo %    ej: 5%2 = 1
# Igual(comparación)  ==  Hay que poner doble igual para referirse a una comparación
                        # ya que con un solo igual se estaría asignando valor a lo anterior.
# Distinto ó Diferente (diferencia)   !=
# Mayor/Menor o igual   <=  >=                   
