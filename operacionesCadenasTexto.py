# Se crea una cadena de ejemplo para trabajar con ella
cadena = "EjEmplO dE CaDENa de tExtos"

# Convertir a minúsculas
print(cadena.lower())
# Convertir a mayúsculas
print(cadena.upper())
# Letra inicial en mayus
print(cadena.capitalize())
# Poner todas las primeras letras de cada palabra en mayus
print(cadena.title())
# Cambiar letras minúsculas a mayúsculas y viceversa
print(cadena.swapcase())
# Ejemplo con booleano (True/False): saber si está en mayúscula
print(cadena.isupper())
cadena = "MAYUSCULAS"   # Convertimos la cadena a mayuculas para probar nuevamente el booleano
print(cadena.isupper())
# saber si está en minúsculas
print(cadena.islower())
cadena = "minusculas"   # Convertimos la cadena nuevamente para probar el booleano
print(cadena.islower())
# Comprobar si la cadena es numérica
print(cadena.isnumeric())
cadena = "1234"     # Volvemos a convertir la cadena para probar el booleano
print(cadena.isnumeric())
# Comprobar si la cadena es alfanumérica
print(cadena.isalnum())
cadena = "#-+*"
print(cadena.isalnum())
# Comprobar si es un título
cadena = "Titulo 1"
print(cadena.istitle())
cadena = "esto no es titulo"
print(cadena.istitle())
