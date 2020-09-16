import string
import os
from TokenSintactico import ClaseTokenSintactico

# ADRIANA GÒMEZ
# 201504236
# COMPILADORES 1




listit= list()

def AnalizaSintactico(parrafo):
    estado = 0
    palabra = ""
    respuesta = "CORRECTO"
    control =0
    contpara=0
    contparc=0
    listit.clear()
    #---- RECORRIENDO EL PARRAFO ----#
    while control < len(parrafo):


        if estado == 0:
            if parrafo[control].isalpha():
                palabra+=parrafo[control]
                control+=1
                estado = 1
            elif parrafo[control].isnumeric():
                palabra+=parrafo[control]
                control+=1
                estado = 1
            elif parrafo[control] == ".":
                palabra+=parrafo[control]
                control+=1
                estado = 1
            elif parrafo[control] == "(":
                palabra+=parrafo[control]
                control+=1
                contpara+=1
                estado = 1
            elif parrafo[control] == "+":
                palabra+=parrafo[control]
                control+=1
                estado = 1
            elif parrafo[control] == "-":
                palabra+=parrafo[control]
                control+=1
                estado = 1
            elif parrafo[control] == " ":
                palabra+=parrafo[control]
                control+=1
                estado = 0
            else:
                #----- ERROR LEXICO ----#
                palabra+=parrafo[control]
                control += 1
                respuesta = "INCORRECTO"
                estado = 3


        if estado == 1:
            if respuesta == "CORRECTO":

                if parrafo[control].isalpha():
                    palabra+=parrafo[control]
                    control+=1
                    estado = 1

                elif parrafo[control] == "_":
                    palabra+=parrafo[control]
                    control+=1
                    estado = 1

                elif parrafo[control].isnumeric():
                    palabra+=parrafo[control]
                    control+=1
                    estado = 1

                elif parrafo[control] == ".":
                    palabra+=parrafo[control]
                    if parrafo[control+1]=="-" or parrafo[control+1]=="/" or parrafo[control+1]=="*" or parrafo[control+1]=="." or parrafo[control+1]=="+":
                        respuesta = "INCORRECTO"
                    control+=1
                    estado = 1

                elif parrafo[control] == "(":
                    palabra+=parrafo[control]
                    if parrafo[control+1]=="-" or parrafo[control+1]=="/" or parrafo[control+1]=="*" or parrafo[control+1]=="." or parrafo[control+1]=="+":
                        respuesta = "INCORRECTO"
                    control+=1
                    contpara+=1
                    estado = 1

                elif parrafo[control] == ")":
                    palabra+=parrafo[control]
                    if parrafo[control+1]==".":
                        respuesta = "INCORRECTO"
                    else:
                        respuesta = "CORRECTO"
                    control+=1
                    contparc+=1
                    estado = 1

                elif parrafo[control] == "+":
                    palabra+=parrafo[control]
                    if parrafo[control+1]=="-" or parrafo[control+1]=="/" or parrafo[control+1]=="*" or parrafo[control+1]=="." or parrafo[control+1]=="+":
                        respuesta = "INCORRECTO"
                    control+=1
                    estado = 1

                elif parrafo[control] == "-":
                    palabra+=parrafo[control]
                    if parrafo[control+1]=="-" or parrafo[control+1]=="/" or parrafo[control+1]=="*" or parrafo[control+1]=="." or parrafo[control+1]=="+":
                        respuesta = "INCORRECTO"
                    control+=1
                    estado = 1

                elif parrafo[control] == "*":
                    palabra+=parrafo[control]
                    if parrafo[control+1]=="-" or parrafo[control+1]=="/" or parrafo[control+1]=="*" or parrafo[control+1]=="." or parrafo[control+1]=="+":
                        respuesta = "INCORRECTO"
                    control+=1
                    estado = 1

                elif parrafo[control] == "/":
                    palabra+=parrafo[control]
                    if parrafo[control+1]=="-" or parrafo[control+1]=="/" or parrafo[control+1]=="*" or parrafo[control+1]=="." or parrafo[control+1]=="+":
                        respuesta = "INCORRECTO"
                    control+=1
                    estado = 1

                elif parrafo[control] == " ":
                    palabra+=parrafo[control]
                    control+=1
                    estado = 1

                elif parrafo[control] == "\n":
                    #palabra+=parrafo[control]
                    control+=1
                    estado = 2
                else:
                    #----- ERROR LEXICO ----#
                    palabra+=parrafo[control]
                    control += 1
                    respuesta = "INCORRECTO"
                    estado = 1
            else:
                estado = 3
            



        if estado == 2:
            if respuesta == "CORRECTO":
                if contpara == contparc:
                    respuesta = "CORRECTO"
                elif contpara != contparc:
                    respuesta = "INCORRECTO"
            else:
                break
            nuevo=ClaseTokenSintactico(palabra,respuesta)
            listit.append(nuevo)
            palabra=""
            respuesta="CORRECTO"
            contpara = 0
            contparc = 0
            estado=0
        
        if estado == 3:
            if parrafo[control].isalpha():
                palabra+=parrafo[control]
                control+=1
                estado = 3
            elif parrafo[control].isnumeric():
                palabra+=parrafo[control]
                control+=1
                estado = 3
            elif parrafo[control] == ".":
                palabra+=parrafo[control]
                control+=1
                estado = 3
            elif parrafo[control] == "(":
                palabra+=parrafo[control]
                control+=1
                estado = 3
            elif parrafo[control] == ")":
                palabra+=parrafo[control]
                control+=1
                estado = 3
            elif parrafo[control] == "+":
                palabra+=parrafo[control]
                control+=1
                estado = 3
            elif parrafo[control] == "-":
                palabra+=parrafo[control]
                control+=1
                estado = 3
            elif parrafo[control] == "*":
                palabra+=parrafo[control]
                control+=1
                estado = 3
            elif parrafo[control] == "/":
                palabra+=parrafo[control]
                control+=1
                estado = 3
            elif parrafo[control] == " ":
                palabra+=parrafo[control]
                control+=1
                estado = 3
            elif parrafo[control] == "\n":
                nuevo=ClaseTokenSintactico(palabra,respuesta)
                listit.append(nuevo)
                control+=1
                estado = 4

        if estado == 4:
            palabra=""
            respuesta="CORRECTO"
            contpara = 0
            contparc = 0
            estado = 0
        

    print(contpara, " ",contparc)
    #print("\nTexto: ",palabra, " es: ",respuesta)



    

    print("\n\n\nAqui la lista de errores: ")
    imprimeerror()
    codigoERRORES()



def imprimeerror():
    j=0
    while j<len(listit):
        print(listit[j].lex,listit[j].des)
        j+=1



def codigoERRORES():
    
    cadenaMensaje = ""
    contenidoer = ""
    cadenaMensaje += "<!DOCTYPE html>\n"
    cadenaMensaje += "<html>\n"
    cadenaMensaje += "  <head>\n"
    cadenaMensaje += "      <title> Reporte sintactico </title>"
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
    
    cadenaMensaje += "  <br><h1> Reporte de análisis sintáctico </h1><br><br>\n"
    cadenaMensaje += "  <table border=\"\">\n"
    cadenaMensaje += "      <thead>\n"
    cadenaMensaje += "          <tr>\n"
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
    while u<len(listit):
        contenidoer += "        <tr>\n"
        contenidoer += "            <td>" +listit[u].lex+ "</td>\n"
        contenidoer += "            <td>" +listit[u].des+ "</td>\n"
        contenidoer += "        </tr>\n"
        u+=1

    contenido = cadenaMensaje.replace("erroresTable",contenidoer)
    cadenaMensaje=""
    contenidoer=""
    Guarda(contenido)


def Guarda(reporte):
    arch = open("reportesintactico.html","w+")
    arch.write(reporte)
    arch.close()
    os.startfile("reportesintactico.html")


