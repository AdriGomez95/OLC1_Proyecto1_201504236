class ClaseToken:
    numeroToken=0
    linea=0
    columna=0
    lexema=""
    descripcion=""

    def __init__(self,numeroToken,linea,columna,lexema,descripcion):
        self.numeroToken=numeroToken
        self.linea=linea
        self.columna=columna
        self.lexema=lexema
        self.descripcion=descripcion

    ####-------------- SETERS Y GETERS 
    def __str__(self):
        return "Numero=%s Linea=%s Columna=%s Lexema=%s Descripcion=%s" % (self.numeroToken,self.linea,self.columna,self.lexema,self.descripcion)
    