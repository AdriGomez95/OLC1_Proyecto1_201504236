import string
import os



def AnalizaSintactico(parrafo):
    estado = 0
    palabra = ""
    respuesta = "CORRECTO"
    control =0
    contpara=0
    contparc=0
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
                    palabra+=parrafo[control]
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
                palabra+=parrafo[control]
                control+=1
                estado = 4

        if estado == 4:
            estado = 0
        

    print(contpara, " ",contparc)
    print("\nTexto: ",palabra, " es: ",respuesta)