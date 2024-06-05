# Decorador para verificar que los argumentos de una función cumplan ciertos criterios
# antes de ejecutarse 

def validar(funcion): # Esta es la función decoradora
    def envolver(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Solo se permiten números enteros")
        return funcion(*args, **kwargs)
    return envolver 

@validar # Usamos el decorador para la función de abajo
def suma(a, b):
    return a + b
# Realizamos una llamada válida
print(suma(4, 8))
# Ahora una llamada inválida
print(suma(4, "5"))



