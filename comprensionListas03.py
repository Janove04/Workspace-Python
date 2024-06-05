# Ejemplo para convertir una lista de string a MAYÚSCULAS
palabras = ["hola", "sebas", "python"]
mayusculas = []
for palabra in palabras:
    mayusculas.append(palabra.upper())
print(palabras) # Muestra la lista normal
print(mayusculas) # Muestra la lista convertida a mayúsculas
print("*"*30)
# Ahora con comprensión de listas
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)
