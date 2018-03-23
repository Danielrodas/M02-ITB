# encoding: UTF-8
# Inicializaciones
# Daniel Alexander Rodas Flores
import time
from subprocess import call

call("clear")

salir = "N"
limite = input ("Desde que número desea el amo que cuente? ")
contar = limite
aciertos = 0

if (limite <= 0):
    print "\n"
    print "Error, no se puede utilizar el", limite, "para dicha operación"
    print "\n"
    salir="S"
else:
    while ( salir=="N" ):
        # Hago cosas
         
        # Incremento
        if (limite % contar == 0):
            aciertos = aciertos +1   
        
        contar = contar - 1
        

        # Activo indicador de salida si toca
        if ( contar < 1): # Condición de salida
            salir = "S"
            
    if (aciertos <= 2):

        print "\nSi es número primo \n"

    else:

        print "\nNo es número primo\n"
