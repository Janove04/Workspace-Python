# Importamos una función del módulo random
from random import randint as azar # azar es un alias que le asignamos por comodidad
from random import * # Con el asterisco se importan todas las funciones de la librería random
continua = "s"
while(continua == "s" or continua == "S"):
    lanzaDado = azar(1, 6) # Aca se indica que genere un número al azar entre 1 y 6
    print("- Has sacado un " + str(lanzaDado))
    continua = input(" Continuar lanzando? (s/n):")
print(" Ya no se lanzará más el dado, fin ")
    