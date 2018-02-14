#encoding: UTF-8 

# Daniel A Rodas
# Fecha de creación:  12/02/2018  Fecha de modificación: 14/02/2018 
import time

# En las dos siguientes lineas creo dos variables Dividendo y Divisor las cuales su valor será asignado por el usuario
Dividendo = input( "Introduzca un número dividendo :  " 
Dividor   = input( "Introduzca un número divisor :    " )

# En la siguiente linea creo una variable C que cuyo valor será el resultado de la división de A y B
Cociente =  Dividendo / Divisor

# En la siguiente linea creo una variable que nos dará el modulo de la división entre A y B
Resto = Dividendo % Dividor
 

if  ( Resto == 0 ) :
	
	print "La división es exacta. Conciente: ", Conciente
	
else:
	
	print "La división no es exacta. Conciente: ", Cociente , "  Resto: ", Resto
