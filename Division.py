#encoding: UTF-8 

# Daniel A Rodas
# Fecha de creación:  12/02/2018
import time

# En las dos siguientes lineas creo dos variables A y B las cuales su valor será asignado por el usuario
A = input( "Introduzca un número dividendo :  " )
B = input( "Introduzca un número divisor :    " )

# En la siguiente linea creo una variable C que cuyo valor será el resultado de la división de A y B
C =  A // B  

# En la siguiente linea creo una variable que nos dará el modulo de la división entre A y B
D = A%B


if  ( A % B == 0 ) :
	
	print "La división es exacta. Conciente: ", C
	
else:
	
	print "La división no es exacta. Conciente: ", C , "  Resto: ", D 
