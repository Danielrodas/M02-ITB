# encoding: UTF-8
# Daniel A. Rodas Flores
import os    #en esta linea estoy importando "os" para poder utilizar "clear"


# Inicializaciones
os.system("clear") # Hago un clear
print "\n"  # Hago un cambio de linea o un intro

###################################
##       datos importantes       ##
###################################         
                                 ##
actual = 1                       ##
siguiente = 1                    ##
extra = 0                        ##
                                 ##
#########################################################
##                 Números de vueltas                  ## 
#########################################################
                                                       ##
vuelta = 2                                             ##
limite = input("Introduzca el número de vueltas:  ")   ##
                                                       ##
#########################################################

################
##  variable  ##
##    para    ##
##   salir    ##
################
salir = "N"   ##
################


if (limite < 0):    # Control de errores
    os.system ("clear")
    print "\n"
    print """    Lo sentimos pero en fibonacci no es 
    permitido un número de vuelta en negativo"""
    print "\n"
    salir = "S"

elif (limite == 0):
    actual = 0
    print "\n"  
    print 0
    print 1
    print "\n"
    salir = "S"

elif (limite == 1):

    print "\n"
    print 1
    print 1
    print "\n"
    salir = "S"

elif ( limite > 1 ): 

    extra = actual + siguiente
    print "\n"
    print 1 
    print 1  

       
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
