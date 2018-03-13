# encoding: UTF-8
# Inicializaciones
import time
from subprocess import call

call("clear")

salir = "N"
contar= 1 
limite= input ("Hasta que número desea el amo que cuente? ")

if limite <= 0:
    print "Operación incorrecta."
    time.sleep(1.2)
    call("clear")
    salir = "S"
    
while ( salir=="N" ):
    # Hago cosas
    print  contar

    # Incremento
    contar = contar + 1
    time.sleep(0.2)
    # Activo indicador de salida si toca
    if ( contar > limite ): # Condición de salida
        salir = "S"
