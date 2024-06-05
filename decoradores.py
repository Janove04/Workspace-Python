# Los decoradores son funciones especiales que se usan para agregar funcionalidades
# adicionales o extender el comportamiento de otras funciones o métodos sin modificar 
# su código interno.
# Permiten la reutilización de código al aplicar el mismo comportamiento a varias funciones.

# Ejemplo de uso: Registro de tiempo de ejecución de una función
import time

def calcular_tiempo(funcion): # Función decoradora
    def envuelve(*args, **kwargs): 
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"- Teimpo de ejecución de {funcion.__name__}: {round(fin - inicio, 2)}") # __name__ toma el nombre de la funcion que se da. Round 2 es para que solo muestre 2 decimales.
    return envuelve # wrapper
    
@calcular_tiempo # Aqui con el arroba usamos el decorador en la función que sigue en las líneas de abajo
# Esta es la función a decorar
def operacion():
    time.sleep(4) # Simula que toma un tiempo de ejecución, en este caso de 4 segundos
    print(" Operación realizada")
operacion()
