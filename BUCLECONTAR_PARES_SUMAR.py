# encoding: UTF-8
# Inicializaciones
# Daniel
import time
from subprocess import call

call("clear")

salir = "N"
contar= 1 
limite= input ("Hasta que número desea el amo que cuente? ")
sumar=0

if limite <= 0:
    print "Operación incorrecta."
    time.sleep(1.2)
    call("clear")
    salir = "S"

while ( salir=="N" ):
    if (contar % 2 == 0):
        # Hago cosas
        print  contar
        sumar= (sumar + contar)

    # Incremento
    
    contar = contar + 1
    time.sleep(0.2)

    # Activo indicador de salida si toca
    if ( contar > limite ): # Condición de salida
        print "La suma total es:",sumar
        salir = "S"
