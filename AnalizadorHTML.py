import string
from Token import ClaseToken

listaError = list()

def AnalizaHTML(parrafo):
    estado = 0
    numerotk = 1
    palabra = ""
    control =0
    columna = 0
    fila = 0
    listaError.clear()
    #---- RECORRIENDO EL PARRAFO ----#
    while control < len(parrafo):


        if estado == 0:
            if parrafo[control] == "\n":
                control+=1
                fila += 1
                estado = 0
            elif parrafo[control] == " " or parrafo[control] =="\t":
                control += 1
                columna += 1
                estado = 0
            elif parrafo[control] == "<":
                control+=1
                columna += 1
                estado = 1
            elif parrafo[control] == "/":
                control+=1
                columna += 1
                estado = 1
            elif parrafo[control].isalpha():
                control+=1
                columna += 1
                estado = 1
            elif parrafo[control].isnumeric():
                control+=1
                columna += 1
                estado = 1
            elif parrafo[control] == "=":
                control+=1
                columna += 1
                estado = 1
            elif parrafo[control] == ",":
                control+=1
                columna += 1
                estado = 1
            elif parrafo[control] == "\"":
                control+=1
                columna += 1
                estado = 6
            elif parrafo[control] == "'":
                control+=1
                columna += 1
                estado = 5
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listaError.append(nuevo)
                control += 1
                columna += 1
                estado = 0
                numerotk += 1



        if estado == 1:
            if parrafo[control] == "\n":
                control+=1
                fila += 1
                estado = 1
            elif parrafo[control] == " " or parrafo[control] =="\t":
                control += 1
                columna += 1
                estado = 1
            elif parrafo[control] == "/":
                control+=1
                columna += 1
                estado = 1
            elif parrafo[control].isalpha():
                control+=1
                columna += 1
                estado = 1
            elif parrafo[control].isnumeric():
                control+=1
                columna += 1
                estado = 1
            elif parrafo[control] == "=":
                control+=1
                columna += 1
                estado = 1
            elif parrafo[control] == ",":
                control+=1
                columna += 1
                estado = 1
            elif parrafo[control] == ">":
                control+=1
                columna += 1
                estado = 3
            elif parrafo[control] == "\"":
                control+=1
                columna += 1
                estado = 2
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listaError.append(nuevo)
                control += 1
                columna += 1
                estado = 1
                numerotk += 1
        


        if estado == 2:
            if parrafo[control] == "\"":
                control+=1
                columna += 1
                estado = 1
            else:
                while parrafo[control] != "\"":
                    control+=1
                    columna += 1



        if estado == 3:
            if parrafo[control] == "<":
                control+=1
                columna += 1
                estado = 4
            else:
                while parrafo[control] != "<":
                    #if parrafo[control] == "\n":
                    #    fila += 1
                    #    break
                    #else:
                    #    break
                    control+=1
                    columna += 1



        if estado == 4:
            control+=1
            columna += 1
            estado = 0
            print("Analizado correctamente")



        if estado == 5:
            if parrafo[control] == "'":
                control+=1
                columna += 1
                estado = 7
            else:
                while parrafo[control] != "'":
                    control+=1
                    columna += 1



        if estado == 6:
            if parrafo[control] == "\"":
                control+=1
                columna += 1
                estado = 7
            else:
                while parrafo[control] != "\"":
                    control+=1
                    columna += 1
 


        if estado == 7:
            control+=1
            columna += 1
            estado = 0
            print("Analizado correctamente")


    imprimeerror()


def imprimeerror():
    j=0
    while j<len(listaError):
        print(listaError[j].numeroToken,listaError[j].linea,listaError[j].columna,listaError[j].lexema,listaError[j].descripcion)
        j+=1
    