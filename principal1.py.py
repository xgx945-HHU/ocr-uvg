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
from pytesser import *

########################P R O G R A M A  P R I N C I P A L##################################


image = Image.open('fnord.tif') # Open image object using PIL
print image_to_string(image) # Run tesseract.exe on image
fnord
print image_file_to_string('fnord.tif')
fnord



