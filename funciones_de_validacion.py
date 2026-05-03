# Valida los datos ingresados sea un numero entre 1 y 
# Retorna true si es valido false si no lo es 
def validacion_porcentaje_numerico(num):
    if num =="":
        return False
    num = int(num)
    if num <= 0 or num > 100:
        return False
    
    else:
        return True
# Valida que el dato ingresado sea un numero mayo a 0
# Se utilizara para valores como de procesos, usuarios y espacio de discos
def validacion_numerico(num):
    if num == "":
        return False
    num = int(num)
    if num >= 0:
        return True
# Valida que el dato ingresado coincida con las opciones permitidas
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
# Verifica que la cadena ingresada no este vacia, se utiliza para validar nombres
def validacion_cadena(cadena):
    if cadena == "":
        return False    
    else:  
        return True