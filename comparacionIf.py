numero1 = int(input("- Escriba un primer número: "))
numero2 = int(input("- Escriba un segundo número y le diré cuál es mayor: "))

    # En los ciclos es obligatorio la separación de bloques con tabulador,
    # es decir, debe haber jerarquía en la estructura del código. Todo lo
    # que esté dentro del "if" debe ir un espacio de (tecla) tabulador adelante.
# Ejemplo
#  if (numero1>numero2):  # En Python no se usa llave "{}" sino dos puntos ":"
#      pass  # Esto es para tener la estructura sin tener que poner código
#  else:
#      pass

# Ejemplo 1
if (numero1 > numero2): 
    print(f"-> El número {numero1} es mayor que el número {numero2}")
elif (numero1 < numero2):    # El elif es un else if, para indicar otra condición que debe cumplirse
    print(f"-> El número {numero2} es mayor que el número {numero1}") # Esta sería la forma correcta para indicar únicamente el número mayor
    #print(f"-> El número {numero1} es menor que el número {numero2}") # Esta es la forma que se explica para identificar fácilmente en qué 
                                                                      # parte del código está entrando el input.
else:
    print("-> las dos cifras son iguales")
    
print("Ha finalizado la comparación\n")

# Ejemplo 2, edades para tarifa
print(" Ejemplo #2, edades para tarifa\n")
print("Tarifas:")
print("Menores de 5 años no pagan")
print("Menores de 15 años $5")
print("Menores de 65 años $20")
print("Mayores de 65 años $15")

edad = int(input("- Dime tu edad y te indicaré tu tarifa: "))
if edad < 5:  # No es necesario utilizar paréntesis como en el ejemplo anterior, también funciona sin ellos.
    precio = 0
elif edad < 15:
    precio = 5
elif edad < 65:
    precio = 20
else :
    precio = 15

print("-> Tu tarifa para entrar es de $"+str(precio))