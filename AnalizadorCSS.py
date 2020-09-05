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
    entrada = str(parrafo)
    linea = entrada.split('\n')
    fila = 0
    control =0
    #---- RECORRIENDO POR FILAS EL PARRAFO ----#
    while control < len(linea):
        primero = ""
        columna = 0
        letra = list(linea[fila])

        if estado is 0:
            if letra[columna] == "/":
                control+=1
                estado = 1
                numerotk += 1
                columna += 1
                palabra = "/"
                #listaTokens.append(AgregarTk(numerotk,fila,columna,palabra,"token /"))
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"token /")
                listaTokens.append(nuevo)
                    
                
        elif estado is 1:
            if letra[columna] == "*":
                control+=1
                estado = 6
                numerotk += 1
                columna += 1
                palabra = "*"
                #listaTokens.append(AgregarTk(numerotk,fila,columna,palabra,"token *"))
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"token *")
                listaTokens.append(nuevo)

        elif estado is 6:
            if letra[columna] == "*":
                control+=1
                estado = 7
                numerotk += 1
                columna += 1
                palabra = "*"
                #listaTokens.append(AgregarTk(numerotk,fila,columna,palabra,"token *"))
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"token *")
                listaTokens.append(nuevo)

        elif estado is 7:
            if letra[columna] == "/":
                control+=1
                estado = 100
                numerotk += 1
                columna += 100
                fila = 200
                palabra = "/"
                #listaTokens.append(AgregarTk(numerotk,fila,columna,palabra,"token /"))
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"token /")
                listaTokens.append(nuevo)
                
    print("\nAqui la lista: ")
    imprimejiji(listaTokens)
    
def imprimejiji(listaT):
    j=0
    while j<len(listaTokens):
        #print(listaTokens[j].lexema)
        print(listaTokens[j].numeroToken,listaTokens[j].linea,listaTokens[j].columna,listaTokens[j].lexema,listaTokens[j].descripcion)
        j+=1
   