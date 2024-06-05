# Ejemplo 2: Crear una función que sume dos valores
def suma(num1, num2):
    resultado = num1 + num2
    return resultado

num1 = int(input("- Dime el primer número: "))
num2 = int(input("- Dime el segundo número: "))
# Se llama la funcion
resultado = suma(num1, num2)
# Se muestra el resultado
print("--> La suma es igual a "+ str(resultado)) # De esta forma es para convertir el int en string y poder mostrarlo como número
print(f"--> La suma es igual a {resultado}") # Con el 'print f' se puede poner directamente el valor