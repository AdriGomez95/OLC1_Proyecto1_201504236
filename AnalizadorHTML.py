import string
from Token import ClaseToken

listaError = list()

def AnalizaHTML(parrafo):
    estado = 0
    numerotk = 0
    palabra = ""
    control =0
    columna = 0
    fila = 0
    #---- RECORRIENDO EL PARRAFO ----#
    while control < len(parrafo):


        if estado == 0:
            if parrafo[control] == "\n":
                #nuevo=ClaseToken(numerotk,fila,columna,palabra,"token /")
                #listaTokens.append(nuevo)
                control+=1
                fila += 1
                estado = 0

            elif parrafo[control] == " " or parrafo[control] =="\t":
                control += 1
                columna += 1
                estado = 0

            elif parrafo[control] == "<" or parrafo[control] == "/" or parrafo[control].isalpha():  