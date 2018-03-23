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


if (limite <1) :
	print ""
while ( salir=="N" ):
    # Hago cosas
    if (contar < limite and contar > 1):
        if (limite % contar == 0):
            aciertos = aciertos +1        
    # Incremento

    contar = contar - 1
    

    # Activo indicador de salida si toca
    if ( contar < 1): # Condición de salida
        salir = "S"
        
if (aciertos > 0):
    print "\n  No es número primo"

else:
    print "\n Si es número primo"
