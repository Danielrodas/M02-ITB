# coding: UTF-8
# Daniel Rodas Flores
# Fecha de creación: 20/02/2018
import time 
import os


os.system("clear")

print """


              ####################################################
              ##                                                ##
              ##       Bienvenido a la Gasolinera Express       ##
              ##                                                ##
              ####################################################
              ##                                                ##
              ##     Presionar 1 para seleccionar : Super       ##
              ##                                                ##
              ##     Presionar 2 para seleccionar : Sin Plomo   ##
              ##                                                ##
              ##     Presionar 3 para seleccionar : Diesel      ##
              ##                                                ##
              ####################################################
 	
    
    
      """

tipo = raw_input("              Haga su selección : ")


if (tipo == "1"):
    
    os.system("clear")
    
    
    print """
    
          
            #####################################################
            ##                                                 ##
            ##   Presiona 1 para seleccionar: Normal (1.5  €)  ##
            ##                                                 ##
            ##   Presiona 2 para seleccionar: Turbo  (1.55 €)  ##
            ##                                                 ##
            #####################################################
	  
      
        """ 
    subtipo = raw_input("            Haga su selección : ")
    
    print "\n"
    
    if (subtipo == "1"):
        
        Normal= 1.5
        
        Cantidad=input("            Introduzca la cantidad de Gasolina(Litros) :   ")
        
        precio= Normal * Cantidad
        
        print "\n"
        
        print "            Su importe es de ", precio," €"
        
        print "\n"
        
        time.sleep (2)
        
        os.system("clear")
    
    elif (subtipo == "2"):
        
        turbo= 1.55
        
        Cantidad=input("            Introduzca la cantidad de Gasolina(Litros) :   ")
        
        precio= turbo * Cantidad
        
        print "\n"
        
        print "            Su importe es de ", precio," €"
        
        print "\n"

        time.sleep (2)
        
        os.system("clear")
        
    else:
        
        os.system("clear")
        
        print "\n"
        
        print "Lo sentimos  no es posible hacer la operación"
        
        print "\n"
        
        time.sleep (2)
        
        os.system("clear")        
        
elif (tipo == "2"):
    
    os.system("clear")
    print """
    
    
    
  ##########################################################################
  ##                                                                      ##
  ##   Presiona 1 para seleccionar: Normal (1.6  €)                       ##
  ##                                                                      ##
  ##   Presiona 2 para seleccionar: Con aditivos sabor naranja  (1.65 €)  ##
  ##                                                                      ##
  ##########################################################################
	
    
          """ 
    subtipo2 = raw_input("  Haga su selección : ")
    
    print "\n"
    
    if (subtipo2 == "1"):
        
        Normal= 1.6
        
        Cantidad=input("  Introduzca la cantidad de Gasolina(Litros) :   ")
        
        precio= Normal * Cantidad
        
        print "\n"
        
        print "  Su importe es de ", precio," €"
        
        print "\n"
        
        time.sleep (2)
        
        os.system("clear")
    
    elif (subtipo2 == "2"):
        
        aditivos= 1.65
        
        Cantidad=input("  Introduzca la cantidad de Gasolina(Litros) :   ")
        
        precio= aditivos * Cantidad
        
        print "\n"
        
        print "  Su importe es de ", precio," €"
        
        print "\n"

        time.sleep (2)
        
        os.system("clear")
        
    else:
        
        os.system("clear")
        
        print "\n"
        
        print "Lo sentimos  no es posible hacer la operación"
        
        print "\n"
        
        time.sleep (2)
        
        os.system("clear")

elif (tipo == "3"):
    
    os.system("clear")
    
    print """
  
  
  ###########################################################
  ##                                                       ##
  ##   Presiona 1 para seleccionar: Normal (1.7  €)        ##
  ##                                                       ##
  ##   Presiona 2 para seleccionar: Fast&Furius (1.75 €)   ##
  ##                                                       ##
  ###########################################################
	
    
          """
    
    subtipo3 = raw_input("  Haga su selección : ")
    
    print "\n"
    
    if (subtipo3 == "1"):
        
        Normal= 1.7
        
        Cantidad=input("  Introduzca la cantidad de Gasolina(Litros) :   ")
        
        precio= Normal * Cantidad
        
        print "\n"
        
        print "  Su importe es de ", precio," €"
        
        print "\n"
        
        time.sleep (2)
        
        os.system("clear")
    
    elif (subtipo3 == "2"):
        
        Fast= 1.75
        
        Cantidad=input("  Introduzca la cantidad de Gasolina(Litros) :   ")
        
        precio= Fast * Cantidad
        
        print "\n"
        
        print "  Su importe es de ", precio," €"
        
        print "\n"

        time.sleep (2)
        
        os.system("clear")
        
    else:
        
        os.system("clear")
        
        print "\n"
        
        print "Lo sentimos  no es posible hacer la operación"
        
        print "\n"
        
        time.sleep (2)
        
        os.system("clear")
else:
    os.system("clear")
    
    print "\n"
    
    print "Lo sentimos  no es posible hacer la operación"
        
    print "\n"
        
    time.sleep (2)
        
    os.system("clear")
