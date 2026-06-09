def validacion_porcentaje_numerico(num: str) -> bool:
    """
    Valida si un string representa un número flotante o entero válido 
    y si se encuentra dentro del rango porcentual de 0 a 100.

    Args:
        num (str): El string que se desea evaluar como porcentaje.

    Returns:
        bool: True si el string es un número válido entre 0 y 100 (inclusive), 
              False en caso contrario.

    """

    if num == "":
        return False
    # creamos una variable para contar los puntos
    puntos = 0

    for i in range(len(num)):  # recorremos el string(numero)
        caracter = num[i]    # extraemos el caracter

        if caracter == ".":  # preguntamos si es un punto
            puntos += 1

            if puntos > 1:   # si hay ás de un punto
                return False
            
            if i == 0 or i == len(num) - 1:  # si es  al principio ni al final
                return False

        elif caracter < "0" or caracter > "9":  # si no es un número que esta en ese rango
            return False
        
    valor = float(num)  # convertimos el string a float
    if valor >= 0 and valor <= 100:  # si es mayor o igual a 0 y menor o igual a 100
        return True
    else:
        return False
     

def validacion_numerico(num: str) -> bool:
    """
    Valida si un string representa un número flotante o entero válido 
    y si es mayor o igual a 0.

    Args:
        num (str): El string que se desea evaluar.

    Returns:
        bool: True si el string es un número válido mayor o igual a 0, 
              False en caso contrario.
    """
    if num == "":
        return False
    
    puntos = 0

    # Primero nos aseguramos de que el string sea REALMENTE un número
    for i in range(len(num)):  
        caracter = num[i]    

        if caracter == ".":  
            puntos = puntos + 1
            if puntos > 1:   
                return False
            if i == 0 or i == len(num) - 1:  
                return False

        elif caracter < "0" or caracter > "9":  
            return False
        
    
    valor = float(num)  
    if valor >= 0: 
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
    Verifica que la cadena ingresada no esté vacía, no contenga solo espacios
    y tenga una longitud real de más de 5 caracteres válidos.

    Args:
        cadena (str): Texto a validar (nombre de administrador o servidor).

    Returns:
        bool: True si la cadena tiene más de 5 caracteres válidos, False de lo contrario.
    """

    if cadena == "":   # Si el dato esta vacío 
        return False
    
    caracteres_validos = 0 # Creamos un contador para contar los carácteres ingresados

    for i in range(len(cadena)):  # Recorremos la cadena carácter por carácter
        caracter = cadena[i]
       
        if caracter != " ":   # Si el carácter NO es un espacio, lo sumamos al contador
            caracteres_validos += 1
            
    if caracteres_validos > 5:  # verifico si la cadena tiene mas de 5 caracteres
        return True
    else:
        return False

def validadcion_de_incio_de_diagnostico(inicio_de_sistema: str) -> bool:
    """
    Valida que la respuesta de inicio del diagnóstico sea correcta.

    Args:
        inicio_de_sistema (str): Respuesta ingresada por el usuario.
        Debe ser "si" o "no".

    Returns:
        bool: True si la respuesta es válida.
    """
    if inicio_de_sistema == "si" or inicio_de_sistema == "no":
        return True
