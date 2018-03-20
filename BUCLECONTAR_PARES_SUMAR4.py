# encoding: UTF-8
# Daniel Rodas
# Inicializaciones
import time
import os

os.system("clear")

salir = "N"
contar= 1 
limite= 5 #input ("Hasta que número desea el amo que cuente? ")
sumar=0

if limite <= 0:
    print ("Operación incorrecta.")
    time.sleep(1.2)
    call("clear")
    salir = "S"
    
while ( salir=="N" ):
    # Hago cosas
    if (contar % 2 == 0):
        if (contar <= limite-2):
            print contar , "+",
            sumar= (sumar + contar)
        else: 
            print contar, 
            sumar= (sumar + contar)
    # Incremento
    contar = contar + 1
    
    
    time.sleep(0.2)

    # Activo indicador de salida si toca
    if ( contar > limite ): # Condición de salida
        
        salir = "S"
if contar >= limite :
    print   "=", sumar 
