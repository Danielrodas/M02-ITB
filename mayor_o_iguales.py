#encoding: UTF-8 

# Daniel A Rodas
# Fecha de creación:  09/02/2018
import time

numero1 = input ( "Introduzca un número: " )

time.sleep (1)

numero2 = input ( "Introduzca otro número : " )


# Primero compruebo que la variable: ( numero1 ) sea mayor que la variable ( numero2 )
if ( numero1 > numero2 ) :

	print  "El número " , numero1 , " es el mayor" 
	
else:
	
	# Segundo compruebo que la variable: ( numero2 ) sea mayor que la variable ( numero1 )
	if ( numero2 > numero1 ) :
		
		print  "El número " , numero2 , " es el mayor" 
	
	else: 
		
		# Por ultimo compruebo que la variable: ( numero1 ) sean iguales que la variable ( numero2 )
		print "Ambos números son iguales" 
	 
