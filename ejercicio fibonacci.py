# encoding: UTF-8
# Daniel A. Rodas Flores
import os    #en esta linea estoy importando "os" para poder utilizar "clear"


# Inicializaciones
os.system("clear")
print "\n"

####################################
actual = 1
siguiente = 1
extra = 0 
###############################
vuelta = 2
limite = input("Introduzca el número de vueltas:  ")
#################################
salir = "N"
if (limite < 0):
    salir = "S"

elif (limite == 0):
    print "\n"	
    print actual
    print siguiente
    print "\n"
    salir = "S"

elif (limite == 1):
    actual = 1
    siguiente = 1
    print "\n"
    print actual
    print siguiente
    print "\n"
    salir = "S"

elif ( limite > 1 ): 

    extra = actual + siguiente
    print "\n"
    print actual 
    print siguiente  
   
    while ( salir=="N" ):
        # Hago cosas
        print extra
        
        # Incremento
        actual = siguiente
        siguiente = extra 
        extra = actual + siguiente
        
        
        vuelta = vuelta + 1
        # Activo indicador de salida si toca
        if (vuelta > limite): # Condición de salida
                print "\n"
                salir = "S"
