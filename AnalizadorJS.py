import string
from Token import ClaseToken
import os
from graphviz import Digraph
import webbrowser

# ADRIANA GÒMEZ
# 201504236
# COMPILADORES 1




listitaError= list()

def AnalizaJS(parrafo):
    estado = 0
    numerotk = 1
    palabra = ""
    p=""
    control =0
    columna = 0
    fila = 0
    listitaError.clear()
    #---- RECORRIENDO EL PARRAFO ----#
    while control < len(parrafo):


        if estado == 0:
            if parrafo[control] == "\n":
                control+=1
                fila += 1
                estado = 0
                palabra+="\nS0 -> S0: salto de linea"
            elif parrafo[control] == " " or parrafo[control] =="\t":
                control += 1
                columna += 1
                estado = 0
                palabra+="\nS0 -> S0: espacio"
            elif parrafo[control] == "/":
                control += 1
                columna += 1
                estado = 1
                palabra+="\nS0 -> S1: token /"
            elif parrafo[control].isalpha():
                p=parrafo[control]
                control += 1
                columna += 1
                estado = 7
                palabra+="\nS0 -> S7: token "+p
            elif parrafo[control].isnumeric():
                p=parrafo[control]
                control += 1
                columna += 1
                estado = 8
                palabra+="\nS0 -> S8: token "+p
            elif parrafo[control] == "(" or parrafo[control] == ")" or parrafo[control] == "{" or parrafo[control] == "}":
                p=parrafo[control]
                control += 1
                columna += 1
                estado = 9
                palabra+="\nS0 -> S9: token "+p
            elif parrafo[control] == "." or parrafo[control] == "," or parrafo[control] == ";" or parrafo[control] == ":" or parrafo[control] == "_":
                p=parrafo[control]
                control += 1
                columna += 1
                estado = 10
                palabra+="\nS0 -> S10: token "+p
            elif parrafo[control] == ">" or parrafo[control] == "<" or parrafo[control] == "!" or parrafo[control] == "-" or parrafo[control] == "+" or parrafo[control] == "*" or parrafo[control] == "=":
                p=parrafo[control]
                control += 1
                columna += 1
                estado = 11
                palabra+="\nS0 -> S11: token "+p
            elif parrafo[control] == "'":
                control += 1
                columna += 1
                estado = 12
                palabra+="\nS0 -> S12: token '"
            elif parrafo[control] == "\"":
                control += 1
                columna += 1
                estado = 14
                palabra+="\nS0 -> S14: token \""
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listitaError.append(nuevo)
                control += 1
                columna += 1
                estado = 0
                numerotk += 1


        if estado == 1:
            if parrafo[control] == "/":
                control += 1
                columna += 1
                estado = 2
                palabra+="\nS1 -> S2: token /"
            elif parrafo[control] == "*":
                control += 1
                columna += 1
                estado = 4
                palabra+="\nS1 -> S4: token *"
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listitaError.append(nuevo)
                control += 1
                columna += 1
                estado = 0
                numerotk += 1



        if estado == 2:
            if parrafo[control] == "\n":
                estado = 3
                columna += 1
                palabra+="\nS2 -> S3: salto de linea"
            else:
                while parrafo[control] != "\n":
                    columna += 1
                    palabra+="\nS2 -> S2: '"+parrafo[control]+"' comentario unilinea"
                    control += 1

        
        if estado == 3:
            control+=1
            estado = 0
            fila += 1
            columna = 0
            palabra+="\nS3 -> S0: estado aceptacion"
                 


        if estado == 4:
            if parrafo[control] == "*":
                control+=1
                estado = 5
                columna += 1
                palabra +="\nS4 -> S5: token *"
            else:
                while parrafo[control] != "*":
                    columna += 1
                    palabra+="\nS4 -> S4: '"+parrafo[control]+"' comentario multilinea"
                    control += 1

        
        if estado == 5:
            if parrafo[control] == "/":
                control+=1
                estado = 6
                columna += 1
                palabra +="\nS5 -> S6: token /"
            else:
                #----- ERROR LEXICO ----#
                palabra = parrafo[control]
                control+=1
                estado = 0
                numerotk += 1
                columna += 1
                nuevo=ClaseToken(numerotk,fila,columna,palabra,"error lexico")
                listitaError.append(nuevo)

        if estado == 6:
            control+=1
            estado = 0
            fila += 1
            columna = 0
            palabra+="\nS6 -> S0: estado aceptacion"
                 
        if estado == 7:
            estado = 0
                 
        if estado == 8:
            estado = 0
                 
        if estado == 9:
            estado = 0
                 
        if estado == 10:
            estado = 0
                 
        if estado == 11:
            estado = 0
                 


        if estado == 12:
            if parrafo[control] == "'":
                control+=1
                estado = 13
                columna += 1
                palabra+="\nS12 -> S13: token '"
            else:
                while parrafo[control] != "'":
                    columna += 1
                    palabra+="\nS12 -> S12: '"+parrafo[control]+"' comentario"
                    control += 1

        
        if estado == 13:
            control+=1
            estado = 0
            columna = 0
            palabra+="\nS13 -> S0: estado aceptacion"
                 

        if estado == 14:
            if parrafo[control] == "\"":
                control+=1
                estado = 13
                columna += 1
                palabra+="\nS14 -> S15: token \""
            else:
                while parrafo[control] != "\"":
                    columna += 1
                    palabra+="\nS14 -> S14: '"+parrafo[control]+"' comentario"
                    control += 1

        
        if estado == 15:
            control+=1
            estado = 0
            columna = 0
            palabra+="\nS15 -> S0: estado aceptacion"
                 




    print("\n\n\nAqui la lista de errores: ")
    imprimeerror()
    grafo()

    if listitaError:
        codigoERRORES()
    else:
        print("\nlista de errores vacia")
    




def imprimeerror():
    j=0
    while j<len(listitaError):
        print(listitaError[j].numeroToken,listitaError[j].linea,listitaError[j].columna,listitaError[j].lexema,listitaError[j].descripcion)
        j+=1



def codigoERRORES():
    
    cadenaMensaje = ""
    contenidoer = ""
    cadenaMensaje += "<!DOCTYPE html>\n"
    cadenaMensaje += "<html>\n"
    cadenaMensaje += "  <head>\n"
    cadenaMensaje += "      <title> Listado de errores lexicos JS </title>"
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
    
    cadenaMensaje += "  <br><h1> Listado de errores JS </h1><br><br>\n"
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
    while u<len(listitaError):
        contenidoer += "        <tr>\n"
        contenidoer += "            <td>" +str(listitaError[u].numeroToken)+ "</td>\n"
        contenidoer += "            <td>" +str(listitaError[u].linea)+ "</td>\n"
        contenidoer += "            <td>" +str(listitaError[u].columna)+ "</td>\n"
        contenidoer += "            <td>" +listitaError[u].lexema+ "</td>\n"
        contenidoer += "            <td>" +listitaError[u].descripcion+ "</td>\n"
        contenidoer += "        </tr>\n"
        u+=1

    contenido = cadenaMensaje.replace("erroresTable",contenidoer)
    cadenaMensaje=""
    contenidoer=""
    Guarda(contenido)


def Guarda(reporte):
    arch = open("erroresJS.html","w+")
    arch.write(reporte)
    arch.close()
    os.startfile("erroresJS.html")








def grafo():
    #dot = Digraph(comment='Estados')
    #dot.attr('node',shape='circle')

    #dot.node('A','S1')
    #dot.node('B','S2')
    #dot.node('A', shape='doublecircle')
    #dot.edges(['AB','BB'])

    #dot.render("ID.gv",view=False)
    #os.startfile("ID.gv"+".pdf")

    os.system("dot -Tjpg automatas.dot -o automatas.jpg")

    automata = "digraph g{ \n"
    automata += "rankdir=LR; \n"
    automata += "node[shape=circle, color=\"pink\",]; S0, S1, S2, S4; \n"    
    automata += "node[shape=doublecircle, color=\"pink\", style=\"filled\"]; S3, S5, S7, S8; \n \n"
    
    automata += "S0 -> S1 [label = \" / \", color=\"pink\"];\n"
    automata += "S1 -> S2 [label = \" / \", color=\"pink\"];\n"
    automata += "S2 -> S2 [label = \" T \", color=\"pink\"];\n"
    automata += "S2 -> S3 [label = \" /n \", color=\"pink\"];\n"
    automata += "S1 -> S4 [label = \" * \", color=\"pink\"];\n"
    automata += "S4 -> S4 [label = \" T \", color=\"pink\"];\n"
    automata += "S4 -> S5 [label = \" / \", color=\"pink\"];\n\n"
    
    automata += "S0 -> S7 [label = \" L \", color=\"pink\"];\n"
    automata += "S7 -> S7 [label = \" (L|_|D) \", color=\"pink\"];\n"
    automata += "S0 -> S8 [label = \" D \", color=\"pink\"];\n"
    automata += "S8 -> S8 [label = \" D \", color=\"pink\"];\n"
    
    
    automata += "} \n"

    
    escribir2 = open("automatas.dot", "w", encoding="utf-8")
    escribir2.write(automata)
    escribir2.close()
    
