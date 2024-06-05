# Se le asigna valor a una variable
precio = 225
cantidad = 3

# Calculamos el total
total = precio * cantidad

# Se muestra el resultado
print("El precio total es de "+str(total))  # str para poder concatenar un int a un string

# Para borrar una variable
# del precio  # del es para borrar la variable
print(precio)  # Muestra error puesto que en la línea anterior hemos borrado la variable

# Asignar otros valores
precio = 25
cantidad = 21

total = precio * cantidad

# Se muestra el resultado
print("El precio total es de "+str(total))

# Ahora queremos una variable que no cambie (constante)
PASSWORD = "123456" # Por convención, las constantes se escriben (inicializan) en mayúscula

# Asignar varios valores
a, b, c, d = 1, 4, "nombre", True  # Puede ser cualquier tipo de dato
print(a)
print(b)
print(c)
print(d)

# Asignar un mismo valor a varias variables
x = y = z = 68
print(x)
print(z)


