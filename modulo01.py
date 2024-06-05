# Importamos un modulo (o también conocido como librerías)
import math
# Si se quiere importar algo específico, por decir, solo la raíz cuadrada se haría así:
# from math import sqrt

numero = int(input("- Escribe un número y te indico su raíz: "))
print("* La raíz cuadrada de "+ str(numero)+" es "+ str(math.sqrt(numero)))