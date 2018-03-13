# encoding: UTF-8
# Inicializaciones
import time
from subprocess import call

call("clear")

salir = "N"
contar= 1 


 
while ( salir=="N" ):
    # Hago cosas
    print "Número", contar

    # Incremento
    contar = contar + 1
    time.sleep(0.2)
    # Activo indicador de salida si toca
    if ( contar > 50 ): # Condición de salida
        salir = "S"
