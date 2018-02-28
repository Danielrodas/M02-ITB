# encoding: utf-8
# Daniel Rodas 

import time 
import os

os.system("clear")
primer_numero = input ("Introduzca un número: ")
segundo_numero = input ("Introduzca otro número: ")

if ( ( primer_numero == 0 ) or ( segundo_numero == 0 ) ):
    
    print "No se puede utilizar el cero."

elif ( ( primer_numero < 0 ) or ( segundo_numero < 0 ) ):
    
    print "No se pueden utilizar los números negativos."

elif ( primer_numero == segundo_numero ):
    
    print "Ambos números son iguales"
    
else:
    
    if ( primer_numero > segundo_numero ):
        
        mayor = primer_numero
        menor = segundo_numero
        
    if ( segundo_numero > primer_numero ):
        
        mayor = segundo_numero
        menor = primer_numero
        
    if ( mayor % menor == 0 ):
        
        print mayor,"es múltiplo de", menor
    
    else:
        
        print mayor,"no es múltiplo de", menor
