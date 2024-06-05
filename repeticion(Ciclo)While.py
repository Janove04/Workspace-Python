        # Ejemplo: tabla de multiplicar
from operator import contains


tabla = int(input("- Escriba un número para calcular su tabla de multiplicar: "))
# Creamos variable contador (será la que cuente hasta 10)
contador = 1
print(f"Tabla del {tabla}")
# Ahora la repetición
while (contador < 11):
    resultado = tabla * contador
    # Se muestra la tabla
    print(f"- {tabla} por {contador} es igual a {resultado}\n")
    # Ahora se debe incrementar el contador para el siguiente ciclo hasta que llegue a 10
    contador = contador + 1
print(" - Final de la tabla - ")