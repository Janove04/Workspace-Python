# Crearemos una lista de vocales extraidas de una cadena string
frase = "Python es un lenguaje de programacion" # Cadena para extraer las vocales
vocales = [letra for letra in frase if letra in 'aeiouAEIOU']
print(frase)
print(vocales)