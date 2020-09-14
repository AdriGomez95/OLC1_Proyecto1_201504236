class ClaseTokenSintactico:
    lex=""
    des=""

    def __init__(self,lex,des):
        self.lex=lex
        self.des=des

    ####-------------- SETERS Y GETERS 
    def __str__(self):
        return "Lexema=%s Descripcion=%s" % (self.lex,self.des)
    