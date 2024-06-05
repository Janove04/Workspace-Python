# Operadores lógicos
    # Suma  +
    # Resta -
    # Multiplicación *
    # División Entera //  (da como resultado la parte entera de la cifra)
    # Exponencial 5**3 cinco elevado a la 3 = 125 (cinco al cubo)
    # Módulo %    ej: 5%2 = 1
    # Igual(comparación)  ==  Hay que poner doble igual para referirse a una comparación
                            # ya que con un solo igual se estaría asignando valor a lo anterior.
    # Distinto ó Diferente (diferencia)   !=
    # Mayor/Menor o igual   <=  >=
# NOTA!: Para concatenar string y enteros (int) se usa str() pero convierte el int en un string.
#        Literalmente pone el número.    


a = 1; b = 7; c = 4

print("Suma")
print(a+b)
print("Resta")
print(b-c)
print("Multiplicación")
print(c*b)
print("División")
print(b/c)
print("División Entera")
print(b//c)
print("Exponencial")
print(c**3)
print("Mayor/Menor o igual qué")
print(a<b, c>b)
print("Diferente de")
print(a!=c)
print("Condicionales (and, or)")
print(a>c and a<b)
print(b==c or c<b)
print("Concatenar string y enteros (int)")
print("hola "+str(c))