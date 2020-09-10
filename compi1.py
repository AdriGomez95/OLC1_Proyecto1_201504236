
from tkinter import*
from tkinter import ttk
from tkinter import filedialog, messagebox
import sys
import os
import string
import array as ar
from AnalizadorCSS import Analisis
from AnalizadorCSS import imprimejiji
from AnalizadorCSS import imprimebitacora
from Token import ClaseToken
from AnalizadorHTML import AnalizaHTML

# ADRIANA GÒMEZ
# 201504236
# COMPILADORES 1


class interfaz:

	MisTokens = list()
	def __init__(self, window):
		self.ventana = window
		self.ventana.geometry("840x600")
		self.ventana.title("proyecto 1 - Adriana Gòmez")
		self.ventana.configure(background='pale violet red')



		####--------------AQUI VAN LOS BOTONES
		self.boton1 = Button(self.ventana, text="Nuevo", bg="pink")
		self.boton2 = Button(self.ventana, text="Abrir", bg="pink", command=self.abrirArchivo)
		self.boton3 = Button(self.ventana, text="Guardar", bg="pink", command=self.guardarArchivo)
		self.boton4 = Button(self.ventana, text="Guardar como", bg="pink")
		self.boton5 = Button(self.ventana, text="Analizar JSon", bg="pink")#, command=self.compilando)
		self.boton7 = Button(self.ventana, text="Analizar CSS", bg="pink", command=self.compilandoCSS)
		self.boton8 = Button(self.ventana, text="Analizar HTML", bg="pink", command=self.compilandoHTML)
		self.boton6 = Button(self.ventana, text="Salir", bg="pink", command=self.ventana.destroy)

		self.boton1.grid(row=0,column=4)
		self.boton2.grid(row=0,column=5)
		self.boton3.grid(row=0,column=6)
		self.boton4.grid(row=0,column=7)
		self.boton5.grid(row=0,column=8)
		self.boton6.grid(row=0,column=9)
		self.boton7.grid(row=1,column=8)
		self.boton8.grid(row=2,column=8)


		####-------------- AREAS DE TEXTO 
		self.label1 = Label(self.ventana,text='Còdigo entrada:',  bg="pink")
		self.areaTexto = Text(self.ventana, height=40, width=50)
		self.label2 = Label(self.ventana,text='Còdigo salida:',  bg="pink")
		self.areaTexto2 = Text(self.ventana, height=40, width=50)

		self.label1.grid(row=3,column=0)
		self.areaTexto.grid(row=4,column=0)
		self.label2.grid(row=3,column=10)
		self.areaTexto2.grid(row=4,column=10)


		####-------------- POSICION DEL CURSOR 
		self.label5 = Label(self.ventana,text='Posiciòn del cursor',  bg="pale violet red")
		self.label3 = Label(self.ventana,text='Fila:',  bg="pale violet red")
		self.label4 = Label(self.ventana,text='Columna:',  bg="pale violet red")
		self.posFila = Label(self.ventana, text=self.areaTexto.index(INSERT),  bg="lemon chiffon").grid(row=2,column=3)
		self.posColumna = Label(self.ventana, text=self.areaTexto.index(INSERT),  bg="lemon chiffon").grid(row=3,column=3)
		#me quede en posicionar el cursor
		self.label5.grid(row=1,column=2)
		self.label3.grid(row=2,column=2)
		self.label4.grid(row=3,column=2)


	####-------------- METODO PARA GUARDAR --------------####
	#def abrirArchivo(self):
	#	archivito = filedialog.askopenfilename(title="abrir")
	#	self.areaTexto(archivito)
		#print(archivito)
      
	####-------------- METODO PARA ABRIR --------------####
	def abrirArchivo(self):
		archivito = filedialog.askopenfilename(title="abrir", filetypes=(("archivos de texto","*.txt"),("archivos pdf","*.pdf")))
		if archivito!=' ':
			archi=open(archivito, "r", encoding="utf-8")
			contenido=archi.read()
			archi.close()
			self.areaTexto.delete("1.0",END)
			self.areaTexto.insert("1.0",contenido)
		#print(archivito)
      
	
	####-------------- METODO PARA GUARDAR --------------####
	def guardarArchivo(self):
		archivito = filedialog.asksaveasfilename(title="abrir", filetypes=(("archivos de texto","*.txt"),("archivos pdf","*.pdf")))
		if archivito!=' ':
			archi=open(archivito, "w", encoding="utf-8")
			archi.write(self.areaTexto.get("1.0", END))
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
		Analisis(parrafoentrada)
		#print(parrafoentrada)
		#self.MisTokens = AgregarTK()

		#p = imprimebitacora
		#for j in self.MisTokens:
		#	p += j + '\n'

		#self.areaTexto2.delete("1.0",END)
		#self.areaTexto2.insert(INSERT, p)
		

	def compilandoHTML(self):
		parrafoentrada2 = str(self.areaTexto.get("1.0","end-1c"))
		AnalizaHTML(parrafoentrada2)






if __name__=='__main__':
	window = Tk()
	app = interfaz(window)
	window.mainloop()
