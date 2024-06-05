# Ejemplo 1: Crear una funcion para saber si el número introducido es Par o Impar
def esPar(numero): # Recordar que las funciones se crean con def + nombre + parámetro dentro del paréntesis
    if numero %2 == 0:
        #print("-El número es Par")  # Esta sería una forma de hacer el if de la funcion
        return True # Esta sería la otra forma de hacer el if
    else:
        #print("-El número es Impar")
        return False
        
numero = int(input("- Escribe un número y te diré si es Par o Impar: "))
resultado = esPar(numero)
if resultado: # Aqui no es necesario poner ==True, cuando ponemos una variable directamente sin nada que comparar estamos indicando si esa variable es verdadera.
    print(f"- El número {numero} es Par")
else:
    print(f"- El número {numero} es Impar")