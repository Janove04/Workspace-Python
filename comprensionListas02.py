# Creamos la lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filtramos los números pares de la lista (manera tradicional)
pares = []
for numero in numeros:
    if numero % 2 == 0: # Este cálculo es para saber si es par
        pares.append(numero)
print(pares)
print("*"*20) # Separación 
# Ahora con comprensión de lista
pares = [numero for numero in numeros if numero % 2 == 0] # Si quisieramos los impares sería numero % 2 != 0
print(pares)
