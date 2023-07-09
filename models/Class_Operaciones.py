from datetime import date


resultado = ""

def asignarSedeTabla(id_sede):

    if id_sede == 1 or id_sede == 11:
        resultado = "ILO"
    elif id_sede == 2 or id_sede == 13:
        resultado = "CAMANA"
    elif id_sede == 3 or id_sede == 12:
        resultado = "MOLLENDO"
    elif id_sede == 4 or id_sede == 10:
        resultado = "MOQUEGUA"
    elif id_sede == 5:
        resultado = "TOQUEPALA"
    elif id_sede == 6:
        resultado = "CUAJONE"
    elif id_sede == 7 or id_sede == 9:
        resultado = "TACNA"
    else:
        resultado = "NO IDENTIFICADO"

    return resultado


def asignarPeriodo(fecha_ult_pago):
    
    anio = str(fecha_ult_pago.year)
    mes = str(fecha_ult_pago.month).zfill(2)
    concatenado = anio + mes

    return concatenado

def asignarOperador(nom_sede):
    validarTextoFibwi = "Fibwi" in nom_sede
    operador = ""
    if validarTextoFibwi:
        operador = "Fibwi"
    else:
       operador = "Cable Club"    

    return operador




















