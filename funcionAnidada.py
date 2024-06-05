# Ejercicio sobre funciones anidadas
def calcular(num1, num2, operacion = 'sumar'):  # Por defecto se deja la suma si no se le pasa ese
                                                # parámetro operación a la funcion al momento de llamarla   
    def sumar(num1, num2):
        return num1 + num2
    def restar(num1, num2):
        return num1 - num2
    def multiplicar(num1, num2):
        return num1 * num2
    def dividir(num1, num2):
        return num1 / num2
    if operacion == 'sumar':
        print(f'{num1} + {num2} = {sumar(num1, num2)}')
    elif operacion == 'restar':
        print(f'{num1} - {num2} = {restar(num1, num2)}')
    elif operacion == 'multiplicar':
        print(f'{num1} * {num2} = {multiplicar(num1, num2)}')
    elif operacion == 'dividir':
        print(f'{num1} / {num2} = {dividir(num1, num2)}')
    return "- Operación: "  # Retorno ese string solo para que no muestre None por el return de las
                            # funciones anidadas.
print(calcular(4, 9))
print(calcular(4, 456, 'multiplicar'))
print(calcular(45, 78, 'sumar'))
print(calcular(823, 465, 'restar'))
print(calcular(80, 4, 'dividir'))