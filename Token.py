class Token(object):
    fila=0
    columna=0
    lexema=""

    def __init__(self,fila,columna,lexema):
        self.fila=fila
        self.columna=columna
        self.lexema=lexema

    ####-------------- SETERS Y GETERS 
    def set_Fila(self,fila):
        self.fila=fila

    def get_Fila(self):
        return self.fila

    def set_Columna(self,columna):
        self.columna=columna

    def get_Columna(self):
        return self.columna

    def set_Lexema(self,lexema):
        self.lexema=lexema

    def get_Lexema(self):
        return self.lexema

    