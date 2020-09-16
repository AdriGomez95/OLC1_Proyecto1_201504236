
from tkinter import*
from tkinter import ttk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
import sys
import os
import string
import array as ar
from AnalizadorCSS import Analisis
from Token import ClaseToken
from AnalizadorHTML import AnalizaHTML
from AnalizadorJS import AnalizaJS
from Sintactico import AnalizaSintactico 

# ADRIANA GÒMEZ
# 201504236
# COMPILADORES 1


class interfaz:

	MisTokens = list()
	def __init__(self, window):
		self.ventana = window
		self.ventana.geometry("840x600")
		self.ventana.title("proyecto 1 - Adriana Gòmez")
		self.ventana.configure(background='black')#'pale violet red')
		

		####--------------AQUI VAN LOS BOTONES
		self.boton1 = Button(self.ventana, text="Nuevo", bg="pink", command=self.eliminaTexto)
		self.boton2 = Button(self.ventana, text="Abrir", bg="pink", command=self.abrirArchivo)
		self.boton3 = Button(self.ventana, text="Guardar", bg="pink", command=self.guardarArchivo)
		self.boton4 = Button(self.ventana, text="Guardar como", bg="pink", command=self.guardarArchivo)
		self.boton6 = Button(self.ventana, text="Salir", bg="pink", command=self.ventana.destroy)
		self.boton5 = Button(self.ventana, text="Analizar JS", bg="pink", command=self.compilandoJS)
		self.boton7 = Button(self.ventana, text="Analizar CSS", bg="pink", command=self.compilandoCSS)
		self.boton8 = Button(self.ventana, text="Analizar HTML", bg="pink", command=self.compilandoHTML)
		self.boton9 = Button(self.ventana, text="Sintactico", bg="pink", command=self.compilandoSintactico)

		self.boton1.pack(side=TOP,fill=X)
		self.boton2.pack(side=TOP,fill=X)
		self.boton3.pack(side=TOP,fill=X)
		self.boton4.pack(side=TOP,fill=X)
		self.boton6.pack(side=TOP,fill=X)
		self.boton9.pack(side=BOTTOM,fill=X)
		self.boton8.pack(side=BOTTOM,fill=X)
		self.boton7.pack(side=BOTTOM,fill=X)
		self.boton5.pack(side=BOTTOM,fill=X)



		####-------------- AREAS DE TEXTO 
		self.areaTexto = Text(self.ventana, height=40, width=50)
		self.areaTexto.pack(side=LEFT)
		self.scrol = Scrollbar(self.ventana)
		self.scrol.pack(side=LEFT,fill=Y)
		self.scrol.config(command=self.areaTexto.yview)
		self.areaTexto.config(yscrollcommand=self.scrol.set)


		self.areaTexto2 = Text(self.ventana, height=40, width=50, background='pale violet red')
		self.areaTexto2.pack(side=RIGHT)
		self.scrol2 = Scrollbar(self.ventana)
		self.scrol2.pack(side=RIGHT,fill=Y)
		self.scrol2.config(command=self.areaTexto2.yview)
		self.areaTexto2.config(yscrollcommand=self.scrol2.set)
		


		####-------------- POSICION DEL CURSOR 
		self.label5 = Label(self.ventana,text='Posiciòn del cursor',  bg="pale violet red")
		self.label3 = Label(self.ventana,text='Fila:',  bg="pale violet red")
		self.label4 = Label(self.ventana,text='Columna:',  bg="pale violet red")
		self.posFila = Label(self.ventana, text=self.areaTexto.index(INSERT),  bg="lemon chiffon")#.grid(row=2,column=3)
		self.posColumna = Label(self.ventana, text=self.areaTexto.index(INSERT),  bg="lemon chiffon")#.grid(row=3,column=3)
		#me quede en posicionar el cursor
		#self.label5.grid(row=1,column=2)
		#self.label3.grid(row=2,column=2)
		#self.label4.grid(row=3,column=2)





	####-------------- METODO PARA LIMPIAR --------------####
	def eliminaTexto(self):
		self.areaTexto.delete("1.0",END)
		self.areaTexto2.delete("1.0",END)

	####-------------- METODO PARA ABRIR --------------####
	def abrirArchivo(self):
		archivito = filedialog.askopenfilename(title="abrir")
		if archivito!=' ':
			archi=open(archivito, "r", encoding="utf-8")
			contenido=archi.read()
			self.areaTexto.delete("1.0",END)
			self.areaTexto2.delete("1.0",END)
			self.areaTexto.insert("1.0",contenido)
			archi.close()
		
	####-------------- METODO PARA GUARDAR --------------####
	def guardarArchivo(self):
		archivito = filedialog.asksaveasfilename(title="abrir", filetypes=(("archivos de texto","*.txt"),("archivos pdf","*.pdf")))
		if archivito!=' ':
			archi=open(archivito, "w", encoding="utf-8")
			archi.write(str(self.areaTexto.get("1.0", END)))
			archi.close()
			messagebox.showinfo("Informacion","los datos han sido guardados correctamente")





	####-------------- METODO PARA ANALIZAR --------------####
	def compilando(self):
		StringPalabras = StringVar()
		etiquetas = ['<table>', '<th>', '<tr>', '<td>', '<caption>', '<colgroup>', '<col>', '<thead>', '<tbody>']
		palabra = self.areaTexto.get("1.0", "end-1c")
		separador = " "
		StringPalabras = palabra.split(separador)
		#StringPalabras = ','.join(palabra.split())
		miLista = set()
		#miLista.add('\''+palabra.split(separador)+'\'')
		self.areaTexto2.insert(INSERT, 'imprimiendo tamaño del stringvar: ')
		self.areaTexto2.insert(INSERT, len(StringPalabras))
		self.areaTexto2.insert(INSERT, '\n')
		self.areaTexto2.insert(INSERT, 'imprimiendo el stringvar: ')
		self.areaTexto2.insert(INSERT, StringPalabras)
		self.areaTexto2.insert(INSERT, '\n')
		#self.areaTexto2.insert(INSERT, 'imprimiendo tamaño de miLista: ')
		#self.areaTexto2.insert(INSERT, len(miLista))

		#if StringPalabras in etiquetas:
		#	self.areaTexto2.insert(INSERT, "\n Compilado correctamente")
		#else:
		#	self.areaTexto2.insert(INSERT, "\n Palabra no reconocida")
		

		#for k in StringPalabras:
		#	self.areaTexto2.insert(INSERT, 'Entro al for')
		#	self.areaTexto2.insert(INSERT, "\n")
		#	self.areaTexto2.insert(INSERT, palabra.split(separador) )
		#	if palabra.split(separador) in etiquetas:
		#		self.areaTexto2.insert(INSERT, "\n Compilado correctamente")
		#	else:
		#		self.areaTexto2.insert(INSERT, "\n Palabra no reconocida")

		#if palabra in etiquetas:
		#	self.areaTexto2.insert(INSERT, "Compilado correctamente")
		#else:
		#	self.areaTexto2.insert(INSERT, "Palabra no reconocida")
			#tokensMalos = ar.array()	








	####-------------- METODO PARA ANALIZAR CSS --------------####
	def compilandoCSS(self):
		parrafoentrada = str(self.areaTexto.get("1.0","end-1c"))
		getpar = Analisis(parrafoentrada)
		
		self.areaTexto2.delete("1.0",END)
		self.areaTexto2.insert(INSERT, getpar)
		


	####-------------- METODO PARA ANALIZAR HTML --------------####
	def compilandoHTML(self):
		parrafoentrada2 = str(self.areaTexto.get("1.0","end-1c"))
		AnalizaHTML(parrafoentrada2)



	####-------------- METODO PARA ANALIZAR JS --------------####
	def compilandoJS(self):
		parrafoentrada3 = str(self.areaTexto.get("1.0","end-1c"))
		AnalizaJS(parrafoentrada3)



	####-------------- METODO PARA ANALIZAR Sintactico --------------####
	def compilandoSintactico(self):
		parrafoentrada4 = str(self.areaTexto.get("1.0","end-1c"))
		AnalizaSintactico(parrafoentrada4)




if __name__=='__main__':
	window = Tk()
	app = interfaz(window)
	window.mainloop()
