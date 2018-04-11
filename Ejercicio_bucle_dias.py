# encoding: UTF-8
# Nombre del programa ejercicio_bucle_dias.py
# hecho por: Daniel A Rodas Flores 

# Procederé a importar os y time
import time 
import os

# en desde la ĺínea 10 asta la 34 será mi portada del programa
os.system("clear")
print"""






                            -------------------------
                            |                       |
                            |          Días         |
                            |                       |
                            |      Programador:     |
                            |                       |   
                            |      Daniel Rodas     |
                            |                       |
                            -------------------------





"""
time.sleep(3)
os.system("clear")

# Inicializaciones
# Las lineas desde la 38 asta 44 son variables
salir = "N"
numeros_dias= input("Introduzca un número de días: ")
resta_anyos = 0 
anyo = 0
dias = 0
meses = 0
semanas = 0 

#Control de errores
if ( numeros_dias < 0 ):
    print "Lo sentimos no puede utilizar números negativos"
    salir= "S"
if ( numeros_dias > 0 ):    
    while ( salir=="N" ):
        # Hago cosas
        if (numeros_dias > 364): # Compruebo que sea un año
            resta_anyos = numeros_dias - 365
            numeros_dias= resta_anyos
            anyo = anyo + 1
        elif (numeros_dias > 30): # Compruebo que sea un mes
            resta_anyos = numeros_dias - 30
            numeros_dias= resta_anyos
            meses = meses + 1
        elif (numeros_dias > 6): # Compruebo que no sea una semana
            resta_anyos = numeros_dias - 7
            numeros_dias= resta_anyos
            semanas = semanas + 1 

        # Activo indicador de salida si toca
        if ( numeros_dias < 7 ) or numeros_dias == 0: # Condición de salida
                salir = "S"
    # Muestro por pantalla el resultado en años
    print anyo,
    if ( anyo == 1 ): # Compruebo en caso de que tenga años ponerlo en plural o no
        print "año"
    else: 
        print "años"

    # Muestro por pantalla el resultado en meses
    print meses,
    if (meses == 1):   # Compruebo en caso de que tenga meses ponerlo en plural o no
        print "mes"
    else:
        print "meses"

    # Muestro por pantalla el resultado en semanas
    print semanas,
    if (semanas == 1): # Compruebo en caso de que tenga semanas ponerlas en plural o no
        print "semana"
    else:
        print "semanas"            

    # Muestro por pantalla el resultado en días
    dias = numeros_dias 
    print dias,
    if (dias == 1):   # Compruebo en caso de que tenga días ponerlo en plural o no
        print "Dia"
        
    else:
        print "Dias"
