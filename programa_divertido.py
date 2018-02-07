#encoding: utf-8 -*-
import time
# Daniel Rodas Flores
# 6/2/2018
import time

#La siguiente linea sirve para darle valor a la variable: numero_de_dias
numero_de_dias=input("Número de días : ")


#La siguiente linea pregunto si la variable: numero_de_dias tiene un valor entre 0 y 89 que el mafioso le de unas pequeña sanción
if ( numero_de_dias > 0 and numero_de_dias < 90 ):
	
	print ( "No pasa nada, pero tu cuota va aumentando" )


else:
	
	#La siguiente linea pregunto si la variable: numero_de_dias tiene un valor entre 90 y 91 que el mafioso le da una advertencia
	if ( numero_de_dias >=90 and numero_de_dias < 92 ):
	
		print ( "Venga, porque estoy de buenas no haré nada, pero págame" )
		
		time.sleep(3)
				
		print ( "XD" )
		
	else:
		
		#La siguiente linea pregunto si la variable: numero_de_dias tiene un valor de 92  el mafioso rompe piernas
		if ( numero_de_dias == 92 ):
			
			print ( "Corre que si te pillo te romo las piernas" ) 
			
			time.sleep(3)
				
			print ( "XD" )
			
			
		else: 
			
			#La siguiente linea pregunto si la variable: numero_de_dias tiene un valor mayor a 100 días el mafioso armó la de troya
			if ( numero_de_dias >=100):
				
				print ( "Se armó la balazera, pinche wey!!!!!" )
				
				time.sleep(3)
				
				print ( "XD" )
				
			else:
				
				#La siguiente linea pregunto si la variable: numero_de_dias tiene un valor entre 93 y 99 que el mafioso le da otra advertencia
				print ( "¡¡Pagame o te balazeo!!" )
				
				time.sleep(3)
				
				print ( "XD" )
