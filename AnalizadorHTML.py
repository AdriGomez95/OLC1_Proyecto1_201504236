import string
from Token import ClaseToken
import os

# ADRIANA GÒMEZ
# 201504236
# COMPILADORES 1



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
            elif parrafo[control] == ">":
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
            elif parrafo[control] != "<":
                    #if parrafo[control] == "\n":
                    #    fila += 1
                    #    break
                    #else:
                    #    break
                    control+=1
                    columna += 1
                    estado = 3
            elif parrafo[control] == "\n":
                control+=1 
                fila += 1
                estado = 3



        if estado == 4:
            columna += 1
            estado = 0
            #print("Analizado correctamente")



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
            #print("Analizado correctamente")




    print("\nAqui la lista de errores: ")
    imprimeerror()

    if listaError:
        codigoERRORES()
    else:
        print("\nlista de errores vacia")
    


def imprimeerror():
    j=0
    while j<len(listaError):
        print(listaError[j].numeroToken,listaError[j].linea,listaError[j].columna,listaError[j].lexema,listaError[j].descripcion)
        j+=1
    



def codigoERRORES():
    
    cadenaMensaje = ""
    contenidoer = ""
    cadenaMensaje += "<!DOCTYPE html>\n"
    cadenaMensaje += "<html>\n"
    cadenaMensaje += "  <head>\n"
    cadenaMensaje += "      <title> Listado de errores lexicos HTML </title>"
    cadenaMensaje += "      <style>\n"

    cadenaMensaje += "      html{\n"
    cadenaMensaje += "          min-height: 100%;\n"
    cadenaMensaje += "      }\n"

    cadenaMensaje += "      body{\n"
    cadenaMensaje += "          background: -webkit-linear-gradient(left, #93B874, #C9DCB9);\n"
    cadenaMensaje += "          background: -o-linear-gradient(right, #93B874, #C9DCB9);\n"
    cadenaMensaje += "          background: -moz-linear-gradient(right, #93B874, #C9DCB9);\n"
    cadenaMensaje += "          background: linear-gradient(to right, #93B874, #C9DCB9);\n"
    cadenaMensaje += "          background-color: #93B874;\n"
    cadenaMensaje += "      }\n"       
    
    cadenaMensaje += "      </style>\n"
    cadenaMensaje += "  </head>\n"
    cadenaMensaje += "  <body>\n"
    cadenaMensaje += "  <center>\n"
    
    cadenaMensaje += "  <br><h1> Listado de errores HTML </h1><br><br>\n"
    cadenaMensaje += "  <table border=\"\">\n"
    cadenaMensaje += "      <thead>\n"
    cadenaMensaje += "          <tr>\n"
    cadenaMensaje += "              <td> No. </td>\n"
    cadenaMensaje += "              <td> Linea </td>\n"
    cadenaMensaje += "              <td> Columna </td>\n"
    cadenaMensaje += "              <td> Lexema </td>\n"
    cadenaMensaje += "              <td> Descripción </td>\n"
    cadenaMensaje += "          </tr>\n"
    cadenaMensaje += "      </thead>\n"
    cadenaMensaje += "erroresTable\n"
    cadenaMensaje += "  </table>\n"


    cadenaMensaje += "  </center>\n"
    cadenaMensaje += "  </body>\n"
    cadenaMensaje += "</html>\n"

    u=0
    while u<len(listaError):
        contenidoer += "        <tr>\n"
        contenidoer += "            <td>" +str(listaError[u].numeroToken)+ "</td>\n"
        contenidoer += "            <td>" +str(listaError[u].linea)+ "</td>\n"
        contenidoer += "            <td>" +str(listaError[u].columna)+ "</td>\n"
        contenidoer += "            <td>" +listaError[u].lexema+ "</td>\n"
        contenidoer += "            <td>" +listaError[u].descripcion+ "</td>\n"
        contenidoer += "        </tr>\n"
        u+=1

    contenido = cadenaMensaje.replace("erroresTable",contenidoer)
    cadenaMensaje=""
    contenidoer=""
    Guarda(contenido)


def Guarda(reporte):
    arch = open("erroresHTML.html","w+")
    arch.write(reporte)
    arch.close()
    os.startfile("erroresHTML.html")
