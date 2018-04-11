# encoding: UTF-8
# Nombre del programa ejercicio-bucle-promedio.py
# hecho por: Daniel A Rodas Flores 

# Procederé a importar os y time
import time 
import os

# en desde la ĺínea 10 asta la 34 será mi portada del programa
os.system("clear")
print"""






                            -------------------------
                            |                       |
                            |        Promedio       |
                            |                       |
                            |       Programador:    |
                            |                       |   
                            |      Daniel Rodas     |
                            |                       |
                            -------------------------





"""
time.sleep(3)
os.system("clear")



# Inicializaciones   # aqui van las variables 
salir = "N"
suma_numeros=0
vueltas= 0
promedio= 0 

numeros= input("")


# creo bucle para comenzar
while ( salir=="N" ):
    # Hago cosas

    vueltas = vueltas + 1
    suma_numeros = suma_numeros + numeros        
    
    print "vueltas", vueltas
    print "suma", suma_numeros 
    numeros= input("")
    # Incremento


    # Activo indicador de salida si toca
    if ( numeros == -1 ): # Condición de salida

        salir = "S"
            
# Calculo el promedio
promedio =  suma_numeros / vueltas
round(promedio,2)
print "El promedio es = ", promedio

