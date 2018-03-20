# encoding: UTF-8
# Daniel Rodas Flores

import os
import time
os.system("clear")
# Inicializaciones
salir = "N"
vueltas= 1
direccion = ""
while ( salir=="N" ):
    # Hago cosas
    if ( vueltas % 8 == 1 ) or ( vueltas % 8 == 2 ):
        direccion = "Arriba"
        print vueltas,"->", direccion 

    if ( vueltas % 8 == 3 ) or ( vueltas % 8 == 4 ):
        direccion = "DERECHA"
        print vueltas,"->", direccion 
        
    if ( vueltas % 8 == 5 ) or ( vueltas % 8 == 6 ):
        direccion = "Abajo"
        print vueltas,"->", direccion 

    if ( vueltas % 8 == 7 ) or ( vueltas % 8 == 0 ):
        direccion = "Izquierda"
        print vueltas,"->", direccion         
    # Incremento
    vueltas= vueltas+1
    time.sleep(0.2)
    # Activo indicador de salida si toca
    if ( vueltas > 8 ): # Condición de salida
            salir = "S"
