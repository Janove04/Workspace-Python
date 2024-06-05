# Ejercicio: Crear una calculadora BÁSICA 
def menu():               # Se crea la función de Menú
    print("    -- Seb Calculator --")
    print(" | 1) Sumar               |")
    print(" | 2) Restar              |")
    print(" | 3) Multiplicar         |")
    print(" | 4) Dividir             |")
    print(" | 0) Salir               |")
    print(" ")
    opcion = int(input(" Elige la operación a realizar: "))
    return opcion

def solicitarDatos():     # Esta funcion es para solicitar datos al usuario
    num1 = int(input("- Dime el primer número: "))
    num2 = int(input("- Dime el segundo número: "))
    if num2 == 0:   # Este if es para solventar el error de la división por cero
        print("¡¡Este número no puede ser 0!!\n")
        num2 = int(input("- Dime el segundo número: "))
    return num1, num2

def operacion(operador, num1, num2):    # Esta funcion realiza el cálculo 
    if operador == "suma":  # Aqui entra el parámetro operador establecido en la linea anterior
        resultado = num1 + num2
    elif operador == "resta":
        resultado = num1 - num2
    elif operador == "multiplica":
        resultado = num1 * num2
    elif operador == "divide":
        resultado = num1 / num2  # Tener en cuenta que si el num2 es cero, da error porque no se puede dividir por cero (Ya lo actualicé en la función solicitarDatos)
    return resultado
    
while True:   # Se crea el bucle y se pone True para que se siga ejecutando siempre hasta que se le de la opcion de salir
    opcion = menu()
    if opcion == 1:
        num1, num2 = solicitarDatos()
        print(f"--> {num1} + {num2} = " + str(operacion("suma", num1, num2)))
    elif opcion == 2:
        num1, num2 = solicitarDatos()
        print(f"--> {num1} - {num2} = " + str(operacion("resta", num1, num2)))
    elif opcion == 3:
        num1, num2 = solicitarDatos()
        print(f"--> {num1} * {num2} = " + str(operacion("multiplica", num1, num2)))
    elif opcion == 4:
        num1, num2 = solicitarDatos()
        print(f"--> {num1} / {num2} = " + str(operacion("divide", num1, num2))) # Aqui por el momento puede mostrar error al dividir entre cero.
    elif opcion == 0:
        break
    else:
        print(" Introduce una opción válida")
    print("\n")
print(" ¡Hasta Pronto!")
