from Token import *


# ADRIANA GÒMEZ
# 201504236
# COMPILADORES 1


class AnalizadorCSS(object):
    PalabrasReservadas = ['color', 'background-color', 'background-image', 
                            'border', 'Opacity', 'background', 'text-align', 'font-family', 
                            'font-style', 'font-weight', 'font-size', 'font', 'padding-left', 
                            'padding-right', 'padding-bottom', 'padding-top', 'padding', 'display', 
                            'line-height', 'width', 'height', 'margin-top', 'margin-right', 
                            'margin-bottom', 'margin-left', 'margin', 'border-style', 'display', 
                            'position', 'bottom', 'top', 'right', 'left', 'float', 'clear', 
                            'max-width', 'min-width', 'max-height', 'min-height']
    TokenS = list()

    
    def AnalisisCSS(self, palabra):
