# -*- coding: cp1252 -*-
################################################################################
#AUTORES:
   #Eddy Omar Castro Jauregui - 11032
   #Cristian Gustavo Castro Xum - 11129
   #Andres Ricardo Leandro Castillo
#proyecto3.py
#Universidad del Valle de Guatemala
#Algoritmos y programacion basica
#LECTOR DE OCR
#objetivo: Realizar una interfaz grafica que consiste en una ventana con tres botones.
#Por medio de los botones se selecciona el tipo de archivo o la salida.
#El programa convierte una imagen en texto editable
#19 de mayo de 2011 --- ultima modificacion 23 de mayo de 2011
#eddy.castro.q7i@gmail.com
#cris7ian.gus7avo@gmail.com
#elandrewlenadro@gmail.com
#realizado en Windows Vista Home Basic, 2011
#indentado para Python IDLE
################################################################################

#importar modulos a utilizar
from Tkinter import*
from pytesser import *
from reportlab.pdfgen import canvas
import tkFileDialog
import tkMessageBox
import tkSimpleDialog
import Tkinter as tk

############################FUNCIONES DE OCR#####################################

#Esta funcion realiza la conversion de un archivo de imagen a un archivo .txt
#no recibe parametros
#se ejecuta al presionar el boton No. 1
def funciontxt():
    #Pedir nombre de archivo, no puede ser nulo
    nombre = tkSimpleDialog.askstring('Archivo','Ingrese el nombre con el que desea guardar su archivo: ')
    while nombre == "":
        nombre = tkSimpleDialog.askstring('Archivo','Ingrese un nombre. No se pueden nombres vacios.')
    #concatena la extension de archivo
    nombre = nombre + '.txt'
    root = tk.Tk()
    root.withdraw()
    lista=[]
    #conversion de archivo a documento de texto
    while True:
        filename = tkFileDialog.askopenfilename()
        try:
            im = Image.open(filename)
            text=image_to_string(im)
            f=open(nombre,"w")
            f.write(text)
            f.close()
            tkMessageBox.showinfo('INFORMACION', 'Su archivo con el nombre "'+nombre+'". Se ha creado con exito')
            break
        except:
            tkMessageBox.showwarning("Open file","Ingrese un archivo de imagen")
            break
    x = 0

#Esta funcion realiza la conversion de un archivo de imagen a un archivo .pdf
#no recibe parametros
#se ejecuta al presionar el boton No. 2
def funcionpdf():
    #Pedir nombre de archivo a usuario, no puede ser nulo
    nombre2 = tkSimpleDialog.askstring('Archivo','Ingrese el nombre con el que desea guardar su archivo: ')
    while nombre2 == "":
        nombre2 = tkSimpleDialog.askstring('Archivo','Ingrese un nombre. No se pueden nombres vacios.')
    #concatena la extension del archivo
    nombre2= nombre2+".pdf"
    root = tk.Tk()
    root.withdraw()
    lista=[]
    #conversion de archivo a pdf
    while True:
        filename = tkFileDialog.askopenfilename()
        try: 
            im = Image.open(filename)
            text=image_to_string(im)
            text=text+"\n"
            temporal = ""
            x=""
            for palabra in text:
                temporal = temporal + palabra
                if palabra == "\n":
                    lista.append(temporal)
                    temporal=""              
            c=canvas.Canvas(nombre2)        
            contador=0
            k=0
            for elemento in lista:          
               x=elemento
               c.drawString(25,800-contador,x[0:len(x)-1])
               x=""
               contador = contador + 12        
            c.showPage()
            c.save()
            tkMessageBox.showinfo('INFORMACION', 'Su archivo con el nombre "'+nombre2+'". Se ha creado con exito')
            break
        except:
            tkMessageBox.showwarning("Open file","Ingrese un archivo de imagen")
            break

############################VENTANA PRINCIPAL####################################

#funcion para definir la ventana principal
#crea la ventana principal
#no recibe parametros
#fecha de ultima actualizacion: 21 de mayo de 2011
def ventanap():
    ventana = tk.Tk(className = 'Proy. No. 3')
    ventana.minsize(600,150)
    ventana.maxsize(600,150)
    #creacion de label
    l = Label(text = 'LECTOR DE OCR')
    l.pack()
    #creacion de botones
    b1 = Button(text = 'Convertir a texto (.txt)', width = 30, command = funciontxt)
    b1.pack(side = LEFT, padx=2, pady=2)
    b2 = Button(text = 'Convertir a pdf (.pdf)', width = 30, command = funcionpdf)
    b2.pack(side = LEFT, padx=2, pady=2)
    b3 = Button(text = 'Salir', width = 30, command = exit)
    b3.pack(side = LEFT, padx=2, pady=2)
    ventana.mainloop()

########################P R O G R A M A  P R I N C I P A L##################################

#debido a la necesidad de eliminar la ventana principal y luego volverla a cargar, solamente se llama a
#la funcion en el programa principal, ya que la ventana principal se encuentra dentro de una funcion.

ventanap()



