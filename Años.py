# coding: UTF-8 

# Daniel A Rodas
# Fecha de creación:  12/02/2018
import time





print "Hola buenas a este nuevo programa. "
time.sleep (2)

anyo1 = input( "Introduzca el año en el que estamos: " )
time.sleep(1)
anyo2 = input( "Introduzca cualquier año: " ) 

sumar = anyo2 - anyo1

resta = anyo1 - anyo2

if ( sumar == 1):
			
	print "Falta un año exacto"

elif ( anyo1 > anyo2 ) :
	
	print "Dese el año ", anyo2 , "han pasado ", resta , " años."
	

else: 
	
	if ( anyo1 < anyo2 ):
		
		print "Para llegar al año ", anyo2 , " faltan ", sumar , " años."
	
	else:
		
		if ( anyo1 == anyo2 ) :
			print "¡Son el mismo año!"
		
		if ( sumar == anyo1+1):
			
			print "Falta un año exacto"
