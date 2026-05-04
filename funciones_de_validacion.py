# Datos numericos 
def validacion_porcentaje_numerico(num):
    if num =="":
        return False
    num = int(num)
    if num <= 0 or num > 100:
        return False
    
    else:
        return True
def validacion_numerico(num):
    if num == "":
        return False
    num = int(num)
    if num >= 0:
        return True
    else:
        return False

def validacion_datos_categoricos(dato, tipo):
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
    
def validacion_cadena(cadena):
    if cadena == "":
        return False    
    else:  
        return True