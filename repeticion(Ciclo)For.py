    # Ejemplo: tabla de multiplicar con Ciclo For
tabla = int(input("- Escriba un número para calcular su tabla de multiplicar: "))
print(f"  * Tabla del {tabla}")
# Repetir mientras sea menor que 11
for contador in range(1, 11):
    resultado = tabla * contador
    print(f"{tabla} por {contador} es igual a {resultado}\n")
print("* Fin de la tabla * \n")

# Ejemplo For con lista
nombres = ["Sebas","Camila","María","Lula"]
for nombre in nombres:
    print(f"Hola, {nombre}")

# Ejemplo #3, Mostrar 100 números
for numero in range(100):
    print(numero) # muestra los números de cero a 99
    #print(numero + 1) # muestra los números de 1 a 100
