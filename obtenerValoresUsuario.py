# Obtener datos desde consola
nombre = input("Escriba su nombre: ")
print("Hola, " + nombre) 
print("Hola, " + nombre, end=" ") # Para que termine con un espacio 
print("Hola, ", nombre)  # También se puede concatenar con "coma"
print("Hola, ", nombre+"\n\n\n") # Para añadir saltos de línea 
print(f"Hola, {nombre}") # Otra manera de mostrarlo, se insertan directamente las variables en los corchetes
print(f"Hola, {nombre}"+"\t\t\testo está separado por tabulador")  # Para separar con espacios de tabulador

# Ejemplo con números
numero1 = int(input("Escriba un número: ")) # Se especifica que es un int para que haga la suma matemática y no de strings
numero2 = int(input("Escriba un segundo número: "))
resultado = numero1 + numero2
print(f"La suma de {numero1} mas {numero2} es igual a {resultado}")