import string
from Token import ClaseToken

# ADRIANA GÒMEZ
# 201504236
# COMPILADORES 1



listaTokens = list()
    
def Analisis(parrafo):
    #print(parrafo)  
    #listaTokens = list()
    listaReservada = ["color", "background-color", "background-image", "border", "Opacity", "background", "text-align", "font-family", "font-style", "font-weight", "font-size", "font", "padding-left", "padding-right", "padding-bottom", "padding-top", "padding", "display", "line-height", "width", "height", "margin-top", "margin-right", "margin-bottom", "margin-left", "margin", "border-style", "display", "position", "bottom", "top", "right", "left", "float", "clear", "max-width", "min-width", "max-height", "min-height"]
    #listaTokens.clear()
    estado = 0
    numerotk = 0
    palabra = ""
    palabra2=""
    palbrabitacora=""
    #entrada = str(parrafo)
    #linea = entrada.split('\n')
    fila = 0
    #linea = 0
    control =0
    columna = 0
    #---- RECORRIENDO POR FILAS EL PARRAFO ----#
    while control < len(parrafo):
        primero = ""
     #   letra = list(linea[fila])



        if estado == 0:
            if parrafo[control] == "\n":
                control+=1
                fila += 1
                columna = 0
                estado = 0
                palbrabitacora+="\nS0 -> S0: salto de linea"
            
            elif parrafo[control] == " " or parrafo[control] == "\t":
                control+=1
                estado = 0
                columna += 1

            elif parrafo[control] == "/":
                control+=1
                estado = 1
                numerotk += 1
                columna += 1
                palabra = "/"
                #nuevo=ClaseToken(numerotk,fila,columna,palabra,"token /")
                #listaTokens.append(nuevo)
                palbrabitacora+="\nS0 -> S1: token "+palabra

            elif parrafo[control] == "*":
                control+=1
                estado = 2
                numerotk += 1
                columna += 1
                palabra = "*"
                #nuevo=ClaseToken(numerotk,fila,columna,palabra,"token *")    
                #listaTokens.append(nuevo)
                palbrabitacora+="\nS0 -> S2: token "+palabra
            
            elif parrafo[control].isalpha() or parrafo[control].isnumeric() or parrafo[control]=="." or parrafo[control]=="#" or parrafo[control]=="-" or parrafo[control]=="%" or parrafo[control]==",":
                palabra = parrafo[control]
                control+=1
                estado = 3
                numerotk += 1
                columna += 1
                palbrabitacora+="\nS0 -> S3: token "+palabra

            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                control+=1
                estado = 0
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listaTokens.append(nuevo)

            
                


        if estado == 1:
            if parrafo[control] == "*":
                control+=1
                estado = 6
                numerotk += 1
                columna += 1
                palabra = "*"
                palbrabitacora+="\nS1 -> S6: token "+palabra
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                control+=1
                estado = 6
                numerotk += 1
                columna += 1
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listaTokens.append(nuevo)



        if estado == 2:
            if parrafo[control] == "{":
                control += 1
                estado = 9
                numerotk += 1
                columna += 1
                palabra = "{"
                palbrabitacora+="\nS2 -> S9: token "+palabra
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                control+=1
                estado = 9
                numerotk += 1
                columna += 1
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listaTokens.append(nuevo)



        if estado == 3:
            if parrafo[control].isnumeric() or parrafo[control].isalpha() or parrafo[control]=="#" or parrafo[control]==":" or parrafo[control]=="-" or parrafo[control]=="," or parrafo[control]=="." or parrafo[control]=="%" or parrafo[control]=="(" or parrafo[control]==")" or parrafo[control]=="*":
                palabra = parrafo[control]
                control+=1
                estado = 3
                numerotk += 1
                columna += 1
                palbrabitacora+="\nS3 -> S3: token "+palabra
            elif parrafo[control]==" " or parrafo[control]=="\t":
                control+=1
                estado = 3
                numerotk += 1
                columna += 1
                palbrabitacora+="\nS3 -> S3: espacio"
            elif parrafo[control]=="\n":
                control+=1
                estado = 3
                numerotk += 1
                fila += 1
                columna += 0
                palbrabitacora+="\nS3 -> S3: salto de linea"
            elif parrafo[control]=="{":
                control+=1
                estado = 9
                numerotk += 1
                columna += 1
                palabra = "{"
                palbrabitacora+="\nS3 -> S9: token "+palabra
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                control+=1
                estado = 3
                numerotk += 1
                columna += 1
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listaTokens.append(nuevo)




        if estado == 6:
            if parrafo[control] == "*":
                control+=1
                estado = 7
                numerotk += 1
                columna += 1
                palabra = "*"
                palbrabitacora+="\nS6 -> S7: token "+palabra
            else:
                while parrafo[control] != "*":
                    columna += 1
                    palbrabitacora+="\nS6 -> S6: '"+parrafo[control]+"' comentario"
                    control += 1

        

        if estado == 7:
            if parrafo[control] == "/":
                control+=1
                estado = 8
                numerotk += 1
                columna += 1
                palabra = "/"
                palbrabitacora+="\nS7 -> S8: token "+palabra
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                control+=1
                estado = 8
                numerotk += 1
                columna += 1
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listaTokens.append(nuevo)

        if estado == 8:
            control+=1
            estado = 0
            fila += 1
            columna = 0
            palbrabitacora+="\nS8 -> S0: estado aceptacion"
                 


        if estado == 9:#----- ACEPTA PALABRAS ----#
            if parrafo[control] == ":":
                control+=1
                estado = 15
                numerotk += 1
                columna += 1
                palabra = ":"
                palbrabitacora+="\nS9 -> S15: token "+palabra
            
            elif parrafo[control] == " " or parrafo[control] == "\t":
                control += 1
                estado = 9
                columna += 1
                palbrabitacora+="\nS9 -> S9: espacio"
            elif parrafo[control] == "\n":
                control += 1
                estado = 9
                fila += 1
                columna=0
                palbrabitacora+="\nS9 -> S9: salto de linea"
            elif parrafo[control] == "}":
                control += 1
                estado = 18
                numerotk += 1
                columna += 1
                palabra = "}"
                palbrabitacora+="\nS9 -> S18: token "+palabra
            elif parrafo[control].isalpha() or parrafo[control].isnumeric() or parrafo[control]=="." or parrafo[control]=="-" or parrafo[control]=="%" or parrafo[control]=="," or parrafo[control]=="(" or parrafo[control]=="*" or parrafo[control]=="#" or parrafo[control]==")":
                palabra=parrafo[control]
                control+=1
                columna += 1
                estado = 9
                numerotk += 1
                palbrabitacora+="\nS9 -> S9: token "+palabra
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                control+=1 
                estado = 15
                numerotk += 1
                columna += 1
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listaTokens.append(nuevo)# ------ AQUI PARA DE BORRAR 




        if estado == 10:
            if parrafo[control] == "*":
                control+=1
                estado = 11
                numerotk += 1
                columna += 1
                palabra = "*"
                palbrabitacora+="\nS10 -> S11: token "+palabra
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                control+=1
                estado = 11
                numerotk += 1
                columna += 1
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listaTokens.append(nuevo)


        if estado == 11:
            if parrafo[control] == "*":
                control+=1
                estado = 12
                numerotk += 1
                columna += 1
                palabra = "*"
                palbrabitacora+="\nS11 -> S12: token "+palabra
            else:
                columna += 1
                palbrabitacora+="\nS11 -> S11: '"+parrafo[control]+"' comentario"
                control += 1

        

        if estado == 12:
            if parrafo[control] == "/":
                control+=1
                estado = 15
                numerotk += 1
                columna += 1
                palabra = "/"
                palbrabitacora+="\nS12 -> S15: token "+palabra
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                control+=1
                estado = 8
                numerotk += 1
                columna += 1
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listaTokens.append(nuevo)







        if estado == 15:
            if parrafo[control].isalpha() or parrafo[control].isnumeric() or parrafo[control]==" " or parrafo[control]=="\t" or parrafo[control]=="." or parrafo[control]=="-" or parrafo[control]=="%" or parrafo[control]=="," or parrafo[control]=="(" or parrafo[control]=="*" or parrafo[control]=="#" or parrafo[control]==":"or parrafo[control]==";":
                palabra = parrafo[control]
                control += 1
                estado = 15
                numerotk += 1
                columna += 1
                palbrabitacora+="\nS15 -> S15: token "+palabra
            elif parrafo[control]=="\n":
                control += 1
                estado = 15
                numerotk += 1
                columna = 0
                fila += 1
                palbrabitacora+="\nS15 -> S15: salto de linea"
            elif parrafo[control] == "/" and parrafo[control+1] == "*":
                control += 1
                estado = 10
                numerotk += 1
                columna += 1
                palabra = "/"
                palbrabitacora+="\nS15 -> S10: token "+palabra
            elif parrafo[control] == "/":
                control += 1
                estado = 15
                numerotk += 1
                columna += 1
                palabra = "/"
                palbrabitacora+="\nS15 -> S15: token "+palabra
########################################################################




            elif parrafo[control] == "\"":
                control += 1
                estado = 16
                numerotk += 1
                columna += 1
                palabra = "\""
                palbrabitacora+="\nS15 -> S16: token "+palabra
            elif parrafo[control] == "}":
                control += 1
                estado = 18
                palbrabitacora+="\nS15 -> S18: token }"
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                control+=1
                estado = 15
                numerotk += 1
                columna += 1
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listaTokens.append(nuevo)



        if estado == 16:
            if parrafo[control] == "\"":
                control+=1
                estado = 17
                numerotk += 1
                columna += 1
                palabra = "\""
                palbrabitacora+="\nS16 -> S17: token "+palabra
            else:
                while parrafo[control] != "\"":
                    control += 1
                    columna += 1
                    palabra += parrafo[control]
                palbrabitacora+="\nS16 -> S16: '"+palabra+"' comentario"


        if estado == 17:
            if parrafo[control] == ")":
                control+=1
                estado = 17
                numerotk += 1
                columna += 1
                palabra = ")"
                palbrabitacora+="\nS17 -> S17: token "+palabra
            elif parrafo[control] == ";":
                control+=1
                estado = 17
                numerotk += 1
                columna += 1
                palabra = ";"
                palbrabitacora+="\nS17 -> S17: token "+palabra
                
            elif parrafo[control] == " " or parrafo[control] == "\t":
                control += 1
                estado = 17
                columna += 1
                palbrabitacora+="\nS17 -> S17: espacio"
            elif parrafo[control] == "\n":
                control += 1
                estado = 17
                fila += 1
                columna=0
                palbrabitacora+="\nS17 -> S17: salto de linea"
            elif parrafo[control].isalpha() or parrafo[control].isnumeric():
                palabra=parrafo[control]
                control+=1
                columna += 1
                estado = 9
                numerotk += 1
                palbrabitacora+="\nS17 -> S9: token "+palabra

            elif parrafo[control] == "}":
                control+=1
                estado = 18
                numerotk += 1
                columna += 1
                palabra = "}"
                palbrabitacora+="\nS17 -> S18: token "+palabra
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                control+=1
                estado = 17
                numerotk += 1
                columna += 1
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listaTokens.append(nuevo)

        if estado == 18:
            control+=1
            estado = 0
            fila += 1
            columna = 0
            palbrabitacora+="\nS18 -> S0: estado aceptacion"




    print("bitacora: ",palbrabitacora)
    print("\nAqui la lista de errores: ")
    imprimejiji()
    imprimebitacora(palbrabitacora)
    

def imprimebitacora(palbrabitacora):
    return palbrabitacora


def imprimejiji():
    j=0
    while j<len(listaTokens):
        print(listaTokens[j].numeroToken,listaTokens[j].linea,listaTokens[j].columna,listaTokens[j].lexema,listaTokens[j].descripcion)
        j+=1
    