# -*- coding: cp1252 -*-
################################################################################
#AUTORES:
   #Eddy Omar Castro Jauregui - 11032
   #Cristian Gustavo Castro Xum - 11129
   #Andres Ricardo Leandro Castillo
#proyecto3.py
#objetivo: Realizar una interfaz grafica que consiste en una ventana con tres botones.
#19 de mayo de 2011 --- ultima modificacion 21 de mayo de 2011
#eddy.castro.q7i@gmail.com
#realizado en Mac OS X, 2011
#indentado para Python IDLE
################################################################################

#importar modulos a utilizar
from Tkinter import*
from pytesser import *
from reportlab.pdfgen import canvas
import tkFileDialog
import tkMessageBox
#import tkSimpleDialog
#import random
import Tkinter as tk

############################FUNCIONES DE OCR#####################################

##def funcion1():
 ## x = 0

def funcion2():
    root = tk.Tk()
    root.withdraw()
    lista=[]
    while True:
        filename = tkFileDialog.askopenfilename()
        try: 
            im = Image.open(filename)
            text=image_to_string(im)
            f=open("temporal.txt","w")
            f.write(text)
            f.close()
            break
        except:
            tkMessageBox.showwarning("Open file","Ingrese un archivo de imagen")
    x = 0

def funcion3():
    root = tk.Tk()
    root.withdraw()
    lista=[]
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
            c=canvas.Canvas("hello.pdf")        
            contador=0
            k=0
            for elemento in lista:          
               x=elemento
               c.drawString(25,800-contador,x[0:len(x)-1])
               x=""
               contador = contador + 12        
            c.showPage()
            c.save()
            """f=open("temporal.txt","w")
            f.write(text)
            f.close()"""
            break
        except:
            tkMessageBox.showwarning("Open file","Ingrese un archivo de imagen")

############################VENTANA PRINCIPAL####################################

#funcion para definir la ventana principal
#crea la ventana principal
#fecha de ultima actualizacion: 21 de mayo de 2011
def ventanap():
    ventana = Tk(className = 'Proyecto No. 3')
    ventana.minsize(570,150)
    ventana.maxsize(570,150)
    #creacion de label
    l = Label(text = 'LECTOR DE OCR')
    l.pack()
    #creacion de botones
##    b1 = Button(text = 'Seleccionar imagen', width = 20, command = funcion1)
##    b1.pack(side = LEFT, padx=2, pady=2)
    b2 = Button(text = 'Convertir a texto (.txt)', width = 20, command = funcion2)
    b2.pack(side = LEFT, padx=2, pady=2)
    b3 = Button(text = 'Convertir a pdf (.pdf)', width = 20, command = funcion3)
    b3.pack(side = LEFT, padx=2, pady=2)
    ventana.mainloop()
    

########################P R O G R A M A  P R I N C I P A L##################################

#debido a la necesidad de eliminar la ventana principal y luego volverla a cargar, solamente se llama a
#la funcion en el programa principal

ventanap()



