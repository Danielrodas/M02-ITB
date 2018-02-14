#encoding: UTF-8 

# Daniel A Rodas
# Fecha de creación:  12/02/2018  Fecha de modificación: 14/02/2018 
import time

# En las dos siguientes lineas creo dos variables dividendo y divisor las cuales su valor será asignado por el usuario
dividendo=input( "Introduzca un número dividendo :  " )

divisor=input( "Introduzca un número divisor :    " )

# En la siguiente linea creo una variable cociente que cuyo valor será el resultado de la división de dividendo y divisor
cociente =  dividendo / divisor

# En la siguiente linea creo una variable resto que nos dará el modulo de la división entre dividendo y divisor
resto = (dividendo % divisor)
 

if  ( resto == 0 ) :
	
	print "La división es exacta. Conciente: ", cociente
	
else:
	
	print "La división no es exacta. Conciente: ", cociente , "  Resto: ", resto
