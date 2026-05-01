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
    if num <= 0:
        return False
    else:
        return True
        