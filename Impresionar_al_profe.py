
# encoding: utf-8
# Daniel Rodas
# Fecha de creación: 16/02/2018

# Importaré time . Es decir que coge la hora del sistema
import time 

# Importaré os. que para poder utilizar los comandos del sistema operativo en elque me encuentro (que es LINUX)
import os

"""
 Mi proyecto será una calculadora, la cual nos dará los resultados de las
 operaciones matemáticas y además nos dirá si el resultado es par o inpar.
"""

# Primeramente creo una variable la cúal se llamará numero1 por motivos obvios ( Porque es el primer número que el usuario añadirá ).
numero1 = input ( "Introduzca un numero :  " )
time.sleep (1.5)

print "\n"

print "Ahora procedemos a seleccionar el operador matemático "

# Segundo crearé una varible llamada: operador. Como lo indica el nombre es para escribir los operador 
operador = raw_input ( "( / , *  ,  -  ,  + ) :  " )

print "\n"

time.sleep (1)
# Por último y no por ello menos importante, la variable llamada :  numero2 . 
numero2 = input ( "Introduzca un segundo numero : " )

print "\n"

# Primeramente haré un control de errores en la variable: operador, que es la que tiene más probabilidad de dar fallo.
if not ( ( operador == "/" ) or ( operador == "*" ) or ( operador == "+" ) or ( operador == "-" ) ) :
	
	# Si es así primeramente ará un barrido en la pantalla
	os.system("clear")
	
	# Creo una variable que le llamaré: killing. porque será nuestra variable de conteo 
	killing = 5
	
	print "¡Escrito incorrecto en el operador!"
	print "\n"
	time.sleep (1)
	
	# Creo un bucle para el conteo regresivo
	while ( killing >= 0 ):

		print "KILL THE PROCESS IN : ", (killing)
		print "\n"
		time.sleep(1)
		killing -= 1
	
	"""
	 - Aquí irá el else del WHILE
	 - Es decir que una vez cumplida la condición del while, mi programa tiene que hacer algo.
	 - En este caso hago que muestre el mensaje: Saliendo .....   
	   y despues que haga un barrido a la pantalla y que se cierre el programa 
	""" 		
	time.sleep (0.5)
	print "Saliendo ...."
	time.sleep (0.5)
	os.system("clear")
	exit	

# Segundo: si operador es (/) dividirá ambos números
if ( operador == "/" ) :
	
	if ( numero2 == 0 ):
		print "No se puede utilizar el divisor", numero2
	
	else:
	
		if  ( numero1 % numero2 == 0 ) :
			# En la siguiente linea creo una variable cociente que cuyo valor será el resultado de la división de dividendo y divisor
			cociente =  numero1 / numero2
			# En la siguiente linea creo una variable resto que nos dará el modulo de la división entre dividendo y divisor
			resto = (numero1 % numero2)
			print "La división es exacta. Cociente: ", cociente
	
		else:
	
			# En la siguiente linea creo una variable cociente que cuyo valor será el resultado de la división de dividendo y divisor
			cociente =  numero1 / numero2
			# En la siguiente linea creo una variable resto que nos dará el modulo de la división entre dividendo y divisor
			resto = (numero1 % numero2)
			print "La división no es exacta. Cociente: ", cociente , "  Resto: ", resto

# Tercero: si operador es (*) multiplicará ambos números
elif (operador == "*" ):

	multiplicacion= (numero1 * numero2)
        print "El resultado de la multiplicación és: ", multiplicacion
        time.sleep (0.5)
	
	if (multiplicacion % 2  == 0) :
		
		print "Y además el resultado es un número par."
		
	else:
		
		print "Y además el resustado es un número inpar."

# Cuarto: si operador es (+) sumaran ambos números
elif (operador == "+" ):
	suma = (numero1 + numero2)
	
	print "El resultado de la suma és: ", suma
	time.sleep (0.5)
	
	if (suma % 2  == 0) :
		
		print "Y además el resultado es un número par."
		
	else:
		
		print "Y además el resustado es un número inpar."

else :
	# Quinto: si operador es (-) el primer número restará al segundo
	if (operador == "-" ):
		resta = (numero1 - numero2)
	
		print "El resultado de la rests és: ", resta
		time.sleep (0.5)
	
		if (resta % 2  == 0) :
		
			print "Y además el resultado es un número par."
		
		else:
		
			print "Y además el resustado es un número inpar."
        
