# Decorador para autenticar usuario
usuario_autenticado = True
def autenticacion(funcion):
    def envolver(*args, **kwargs):
        if not usuario_autenticado:
            raise PermissionError("Usuario no autenticado") # Error de permiso
        return funcion(*args, **kwargs)
    return envolver

@autenticacion # Usamos el decorador
def acceder(): # Hacemos una llamada válida
    print("Accediendo a la cuenta")
    
acceder()

# Ahora una llamada inválida, simulamos ususario no autenticado
usuario_autenticado = False
acceder()