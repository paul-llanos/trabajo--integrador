def validacion_porcentaje_numerico(num: str) -> bool:
    """
    Valida que los datos ingresados sean un número entero entre 1 y 100.
    
    Args:
        num (str): El valor de entrada capturado habitualmente por un input().
        
    Returns:
        bool: True si el valor es un número entre 1 y 100, False si no lo es o está vacío.
        
    """
    if num == "":
        return False
    num_int = int(num)
    if num_int <= 0 or num_int > 100:
        return False
    else:
        return True

def validacion_numerico(num: str) -> bool:
    """
    Valida que el dato ingresado sea un número mayor o igual a 0.
    
    Args:
        num (str): El valor numérico en formato texto a validar.
        
    Returns:
        bool: True si el número es >= 0, False de lo contrario.
    """
    if num == "":
        return False
    num_float = float(num)
    if num_float >= 0:
        return True
    else:
        return False

def validacion_datos_categoricos(dato: str, tipo: str) -> bool:
    """
    Verifica que la cadena ingresada pertenezca a las categorías del sistema.
    
    Args:
        dato (str): El valor ingresado por el usuario (ej: 'linux', 'activo').
        tipo (str): El contexto de validación ('so', 'firewall', 'servidor').
        
    Returns:
        bool: True si el dato es una opción válida para ese tipo, False si no.
    """
    if dato == "":
        return False

    if tipo == "so":
        if dato == "linux" or dato == "windows":
            return True

    elif tipo == "firewall":
        if dato == "activo" or dato == "inactivo":
            return True

    elif tipo == "servidor":
        if dato == "web" or dato == "base de datos" or dato == "archivos":
            return True

    return False

def validacion_cadena(cadena: str) -> bool:
    """
    Verifica que la cadena ingresada no esté vacía.
    
    Args:
        cadena (str): Texto a validar (nombre de administrador o servidor).
        
    Returns:
        bool: True si la cadena tiene contenido, False si es un string vacío.
    """
    if cadena == "":
        return False    
    else:  
        return True