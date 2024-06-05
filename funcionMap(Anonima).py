# Función Map:
# Esta función Map va iterando uno por uno los números de la lista (en este caso)
# obteniendo el valor en cada iteración y aplicando la fórmula indicada, para
# devolverlo en forma de lista (donde está contenida la funcion Map).
lista = [12, 4, 65, 77, 34, 73, 87, 15, 67, 73]
print(list(map((lambda valor: valor * valor), lista))) # La funcion lambda es una función Anónima
                                                        # y por lo tanto no es necesario ponerle 
                                                        # ningún nombre. Son funciones que se hacen 
                                                        # en una sola línea por lo general y
                                                        # técnicamente no se va a repetir de nuevo
                                                        # en el código.
                                                        
# Función Filter (ej. con la misma lista)                                                        
print(list(filter((lambda valor: valor %2 == 0), lista))) # Esta función filter es como aplicarle 
                                                          # un filtro (en este caso) a la lista.
                                                          # Devuelve solo los valores que cumplan 
                                                          # con la condición dada, a diferencia de 
                                                          # la función Map que devuelve todos.
                                                    
# Función Reduce: Esta función a diferencia de las otras devuelve un valor
import functools # Se debe importar este módulo para poder usar la función reduce. 
print(str(functools.reduce((lambda x, resultado: x + resultado), lista))) # Se debe convertir a string para
                                                                          # visualizar el valor numérico dado.
# En este caso con reduce se muestra la suma de todos los valores de la lista.






                                                    