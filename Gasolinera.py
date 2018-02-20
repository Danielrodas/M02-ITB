# coding: UTF-8
# Daniel Rodas Flores
# Fecha de creación: 20/02/2018
import time 
import os

print """
	  ####################################################
	  ##	                                            ##
	  ##	   Bienvenido a la Gasolinera Express       ##
	  ##                                                ##
	  ####################################################
	  ##                                                ##   
	  ##     Presionar 1 para seleccionar : Super       ##
	  ##                                                ##
	  ## 	 Presionar 2 para seleccionar : Sin Plomo   ##
	  ##                                                ##
	  ##     Presionar 3 para seleccionar : Diesel      ##
	  ##                                                ##
	  ####################################################
 	  """
print "\n"

tipo = input("Haga su selección : ")

if ((tipo != 1) and (tipo != 2) and (tipo != 3)) :
	
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
		
elif (tipo == 1):
	
	print """
          #####################################################
          ##                                                 ##
          ##   Presiona 1 para seleccionar: Normal (1.5  €)  ##
          ##                                                 ##
          ##   Presiona 2 para seleccionar: Turbo  (1.55 €)  ##
          ##                                                 ##
          #####################################################
	      """  
	print "\n"
	subtipo=input( "Haga su selección:       " )
	
	if ((subtipo != 1) and (subtipo != 2) ):
	
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
	else:
		
		print "\n"
		if (subtipo == 1):
			Normal= 1.5
			Cantidad=input("Introduzca la cantidad de Gasolina(Litros) :   ")
			precio=Normal*Cantidad
			print "\n"
			print "Su importe es de ", precio," €"
			print "\n"
			
		elif (subtipo == 2):
			turbo= 1.55
			Cantidad=input("Introduzca la cantidad de Gasolina(Litros) :   ")
			precio=turbo*Cantidad
			print "\n"
			print "Su importe es de ", precio," €"
			print "\n"
			
elif (tipo == 2):
	
	print """
  ##########################################################################
  ##                                                                      ##
  ##   Presiona 1 para seleccionar: Normal (1.6  €)                       ##
  ##                                                                      ##
  ##   Presiona 2 para seleccionar: Con aditivos sabor naranja  (1.65 €)  ##
  ##                                                                      ##
  ##########################################################################
	      """  
	print "\n"
	subtipo2=input( "Haga su selección:       " )
	
	if ((subtipo2 != 1) and (subtipo2 != 2) ):
	
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
	else:
		
		print "\n"
		if (subtipo2 == 1):
			Normal= 1.6
			Cantidad=input("Introduzca la cantidad de Gasolina(Litros) :   ")
			precio2=Normal*Cantidad
			print "\n"
			print "Su importe es de ", precio2," €"
			print "\n"
			
		elif (subtipo2 == 2):
			aditivos= 1.65
			Cantidad=input("Introduzca la cantidad de Gasolina(Litros) :   ")
			precio2=aditivos*Cantidad
			print "\n"
			print "Su importe es de ", precio2," €"
			print "\n"
			
			
elif (tipo == 3):
	
	print """
  ##########################################################################
  ##                                                                      ##
  ##         Presiona 1 para seleccionar: Normal (1.7  €)                 ##
  ##                                                                      ##
  ##         Presiona 2 para seleccionar: Fast&Furius (1.75 €)            ##
  ##                                                                      ##
  ##########################################################################
	      """  
	print "\n"
	subtipo3=input( "Haga su selección:       " )
	
	if ((subtipo3 != 1) and (subtipo3 != 2) ):
	
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
	else:
		
		print "\n"
		if (subtipo3 == 1):
			Normal= 1.7
			Cantidad=input("Introduzca la cantidad de Gasolina(Litros) :   ")
			precio3=Normal*Cantidad
			print "\n"
			print "Su importe es de ", precio3," €"
			print "\n"
			
		elif (subtipo3 == 2):
			Fast= 1.75
			Cantidad=input("Introduzca la cantidad de Gasolina(Litros) :   ")
			precio3=Fast*Cantidad
			print "\n"
			print "Su importe es de ", precio3," €"
			print "\n"
