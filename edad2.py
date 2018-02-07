# encoding: utf-8
# Daniel Rodas
# Fecha de creación 07/02/2018

edad=input("¿Que edad tiene usted?  ")

if ( edad >= 15 and edad <= 17 ) :
	
	print ( "Usted solo puede entrar a las sesiones de las tardes " )
else: 
	
	if ( edad >= 18 and edad <= 23 ) :
		
		print ( "Usted solo puede entrar en las sesiones de jovenes" )
		
	else:
		
		print ( "No se le permite entrar" )
