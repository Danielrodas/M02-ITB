#encoding: UTF-8 

# Daniel A Rodas
# Fecha de creación:  09/02/2018
import time

A = input ( "Introduzca un número: " )

time.sleep (1)

B = input ( "Introduzca un número diferente: " )

time.sleep (1)

C = input ( "Introduzca un número diferente: " )

#Primeramente compruebo que no haya números iguales
if (( A == B  ) and ( A == C )) or (( B == A ) and ( B ==  C )) or (( C == A ) and ( C == B )) :
	print  "Todos los números son iguales" 

else:
    
    # Ahora compruebo que haya dos números iguales
	if ( ( (A == B) and not ( A == C ) ) or ( ( B == C ) and not ( B == A ) ) or ( ( A == C ) and not ( A == B) ) ):
					
		print "hay dos números iguales"  
		
	else:
		
		# Una vez comprovado lo anterior procedemos a comprobar que número es mayor y cúal es menor 
		# El mismo comentario de arriba se procederá a todas las siguientes comparaciones que vienen a continuación
		if ( ( A > B ) and ( A > C ) ) :
	
			print  "El número " , A , " es el mayor" 
	
			time.sleep (1)
	
			if ( B > C ) :
		
				print  "El número " , C , " es el menor" 
	
			else :
		
				print   "El número " , B , " es el menor" 
	
		else: 
	
			if ( ( B > A ) and ( B > C ) ) :
	
				print  "El número " , B , " es el mayor" 
	
				time.sleep (1)
	
				if ( A > C ) :
		
					print  "El número " , C , " es el menor" 
	
				else:
		
					print   "El número " , A , " es el menor" 

			else:
	
				if ( ( C > A ) and ( C > B ) ) :
	
					print  "El número " , C , " es el mayor" 
	
					time.sleep (1)
	
					if ( A > B ) :
		
						print  "El número " , B , " es el menor" 
	
					else:
		
						print   "El número " , A , " es el menor" 
