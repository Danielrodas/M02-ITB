# encoding: UTF-8
# DanieL Rodas Flores
# Fecha de creación:  01/02/2018
import os
from math import pi

#########################################################

os.system ("clear")

menu = raw_input ("""

        Calculadora de áreas
        --------------------
        
        T) Triángulo
        C) Círculo
        
        --------------------
        
        ¿Que figura quiere Calcular ( Escriba T o C)?  """)

menu = menu.upper()

if ( menu == "T" ):
    
    print "\n"
    base = input ("        Escriba la base: ")
    altura = input ("        Escriba la altura: ")
    
    if ( ( base < 0 ) or ( altura <0 ) ):
        
        print "\n"
        print "        Operación no válida."
        print "\n"
        
    else:
        operacion = (base * altura)/2
        print "\n"
        print "        Un triángulo de base", base , "y una altura de", altura, "tiene un área de", operacion
        print "\n"
        
elif ( menu == "C" ):
    
    Radio = input ( "        Introduzca un radio: " )
    
    if ( Radio < 0 ):
        
        print "\n"
        print "        Operación no válida"
        print "\n"
    
    else:
        
        operacion = pi * ( Radio**2 )
        round(operacion,2)
        print "\n"
        print "        Un círculo de radio",Radio, "tiene un área de", operacion
        print "\n"
        
else:
    
    print "\n"
    print "        Operación no válida"
    print "\n"
    
