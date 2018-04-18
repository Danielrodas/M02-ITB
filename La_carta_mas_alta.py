# encoding: UTF-8
# Nombre del programa: La_Carta_Mas_Alta.py
# hecho por: Daniel A Rodas Flores 

# Procederé a importar os , time y de random importaré randint
import time 
import os
from random import randint

# en desde la ĺínea 10 asta la 35 será mi portada del programa
os.system("clear")
print"""





                            -------------------------
                            |                       |
                            |      La Carta Más     |
                            |                       |
                            |          Alta         |
                            |                       |
                            |       Programador:    |
                            |                       |
                            |      Daniel Rodas     |
                            |                       |
                            -------------------------
                            
                            
                            
                            
                            
                           
"""
time.sleep(3)
os.system("clear")

# Aquí hago una comprovación si desea continuar con el programa
print """


            ############################################
            #                                          # 
            #   Hola bienvenido a La Carta Más Alta    #
            #                                          #
            ############################################
            #                                          #
            #          Pres. 0 para Salir              #
            #                                          #
            #          Pres. 1 para Jugar              #
            #                                          #
            ############################################
            
            
            
            
      """
# Inicializaciones # Aqui van las variables
salir = "N"
entras_si_no= raw_input("            Introduzca un número: ")

if (entras_si_no == "0" ): # Si presiona 0 saldrá del juego y saldrá una pantalla diciendo: Saliendo
    os.system("clear")
    print """
    
    
    
    
    
    
    
    
                                ############
                                #          #   
                                # Saliendo #
                                #          #
                                ############
    
 
 
 
 
            
            """
    time.sleep(3)
    os.system("clear")
    salir="S"
elif (entras_si_no == "1"): # Si presiona 1 continuará el juego
    os.system("clear")
    print """
           #####################################
           #                                   #
           #  VALORES DE CARTAS SEGÚN NUMEROS  #
           #                                   #
           #####################################
              Pres  2 para carta de valor  2
              Pres  3 para carta de valor  3
              Pres  4 para carta de valor  4
              Pres  5 para carta de valor  5
              Pres  6 para carta de valor  6
              Pres  7 para carta de valor  7
              Pres  8 para carta de valor  8
              Pres  9 para carta de valor  9
              Pres 10 para carta de valor 10
              Pres 11 para carta de valor  J
              Pres 12 para carta de valor  Q
              Pres 13 para carta de valor  K
              Pres 14 para carta de valor  A
    """

    Cartas_Jugador = input("           Introduzca un Número de carta: ")
    if ( Cartas_Jugador > 1 and Cartas_Jugador < 15 ):
        while ( salir=="N" ):
            # Hago cosas
            Cartas_Maquina = randint(2,14)
            Palo_cartas_Jugador  =  randint(1,4)
            Palo_cartas_Maquina  =  randint(1,4)
            Cartas_Maquina = randint(2,14)
            Valor_Cartas_Jugador = 0
            Valor_Cartas_Maquina = 0
            Valor_Palo_cartas_Jugador  = 0
            Valor_Palo_cartas_Maquina  = 0
             

            ##### Valores por el tipo de palo, (Ordenados de valor: de menos a más) [el comentario va para el palo de jugador y maquina] #####

            # Valor del Palo del jugador
            if ( Palo_cartas_Jugador == 1 ):#pruebo con 1
                Valor_Palo_cartas_Jugador = "Trebol"
            if ( Palo_cartas_Jugador == 2 ):#pruebo con 2
                Valor_Palo_cartas_Jugador = "Corazon Negro"
            if ( Palo_cartas_Jugador == 3 ):#pruebo con 3
                Valor_Palo_cartas_Jugador = "Corazon Rojo"
            if ( Palo_cartas_Jugador == 4 ):#pruebo con 4
                Valor_Palo_cartas_Jugador = "Diamante"

            # Valor del Palo de la maquina
            if ( Palo_cartas_Maquina == 1 ):#pruebo con 1
                Valor_Palo_cartas_Maquina = "Trebol"
            if ( Palo_cartas_Maquina == 2 ):#pruebo con 2
                Valor_Palo_cartas_Maquina = "Corazon Negro"
            if ( Palo_cartas_Maquina == 3 ):#pruebo con 3
                Valor_Palo_cartas_Maquina = "Corazon Rojo"
            if ( Palo_cartas_Maquina == 4 ):#pruebo con 4
                Valor_Palo_cartas_Maquina = "Diamante"

            # Voy a comprobar que Cartas_Jugador sea mayor que Cartas_Maquina    
            if ( Cartas_Jugador > Cartas_Maquina ):
                # Ahora Voy a dar los valores correspondientes a Cartas_Jugador desde la 11 asta la 14
                if ( Cartas_Jugador > 1 and Cartas_Jugador < 11 ):
                    Valor_Cartas_Jugador = Cartas_Jugador
                elif (Cartas_Jugador == 11):
                    Valor_Cartas_Jugador = "J"
                elif (Cartas_Jugador == 12):
                    Valor_Cartas_Jugador = "Q"
                elif (Cartas_Jugador == 13):
                    Valor_Cartas_Jugador = "K"
                elif (Cartas_Jugador == 14):
                    Valor_Cartas_Jugador = "A"
                # Ahora Voy a dar los valores correspondientes a Cartas_Maquina desde la 11 asta la 14
                if ( Cartas_Maquina > 2 and Cartas_Maquina < 11 ):
                    Valor_Cartas_Maquina = Cartas_Maquina    
                elif (Cartas_Maquina == 11):
                    Valor_Cartas_Maquina = "J"
                elif (Cartas_Maquina == 12):
                    Valor_Cartas_Maquina = "Q"
                elif (Cartas_Maquina == 13):
                    Valor_Cartas_Maquina = "K"
                elif (Cartas_Maquina == 14):
                    Valor_Cartas_Maquina = "A"
                
                print "           Jugador escoge:",Valor_Cartas_Jugador, "de", Valor_Palo_cartas_Jugador
                
                print "           Maquina escoge:",Valor_Cartas_Maquina, "de", Valor_Palo_cartas_Maquina
                
                time.sleep(1)
                
                print "           Gana Jugador"
                
            # Voy a comprobar que Cartas_Maquina sea mayor que Cartas_Jugador  
            if ( Cartas_Jugador < Cartas_Maquina ):
                # Ahora Voy a dar los valores correspondientes a Cartas_Jugador desde la 11 asta la 14
                if ( Cartas_Jugador > 1 and Cartas_Jugador < 11 ):
                    Valor_Cartas_Jugador = Cartas_Jugador
                elif (Cartas_Jugador == 11):
                    Valor_Cartas_Jugador = "J"
                elif (Cartas_Jugador == 12):
                    Valor_Cartas_Jugador = "Q"
                elif (Cartas_Jugador == 13):
                    Valor_Cartas_Jugador = "K"
                elif (Cartas_Jugador == 14):
                    Valor_Cartas_Jugador = "A"
                # Ahora Voy a dar los valores correspondientes a Cartas_Maquina desde la 11 asta la 14
                if ( Cartas_Maquina > 1 and Cartas_Maquina < 11 ):
                    Valor_Cartas_Maquina = Cartas_Maquina    
                elif (Cartas_Maquina == 11):
                    Valor_Cartas_Maquina = "J"
                elif (Cartas_Maquina == 12):
                    Valor_Cartas_Maquina = "Q"
                elif (Cartas_Maquina == 13):
                    Valor_Cartas_Maquina = "K"
                elif (Cartas_Maquina == 14):
                    Valor_Cartas_Maquina = "A"
                
                print "           Jugador escoge:",Valor_Cartas_Jugador, "de", Valor_Palo_cartas_Jugador
                
                print "           Maquina escoge:",Valor_Cartas_Maquina, "de", Valor_Palo_cartas_Maquina
                
                time.sleep(1)
                
                print "           Gana Maquina"    

            # Incremento
            time.sleep(3)
            os.system("clear")
            print "\n"
            continuar = raw_input("        Desea continuar jugando (S/N): ")
                
            continuar = continuar.upper() # Paso a mayuscula la variable continuar
            # Activo indicador de salida si toca
            if ( continuar == "N" or continuar == "NO" ): # Condición de salida
                        salir = "S"
                        
            elif ( continuar == "S" or continuar == "SI" ): # si presiona S o escribe SI continuará jugando
                os.system("clear")
                print """
           #####################################
           #                                   #
           #  VALORES DE CARTAS SEGÚN NUMEROS  #
           #                                   #
           #####################################
              Pres  2 para carta de valor  2
              Pres  3 para carta de valor  3
              Pres  4 para carta de valor  4
              Pres  5 para carta de valor  5
              Pres  6 para carta de valor  6
              Pres  7 para carta de valor  7
              Pres  8 para carta de valor  8
              Pres  9 para carta de valor  9
              Pres 10 para carta de valor 10
              Pres 11 para carta de valor  J
              Pres 12 para carta de valor  Q
              Pres 13 para carta de valor  K
              Pres 14 para carta de valor  A
    """

                Cartas_Jugador = input("           Introduzca un Número de carta: ")
            
            else:# Control de errores
                os.system("clear")
                print """
                    ##############################################
                    #                                            #
                    # Error, no puede utilizar teclas diferentes #
                    #                                            #
                    ##############################################
                     """
                        
                salir = "S"
    else: # Control de errores
        os.system("clear")
        print """
            ##############################################
            #                                            #
            # Error, no puede utilizar teclas diferentes #
            #                                            #
            ##############################################
             """
                
        salir = "S"
else: # Control de errores
    os.system("clear")
    print """
        ##############################################
        #                                            #
        # Error, no puede utilizar teclas diferentes #
        #                                            #
        ##############################################
         """
            
    salir = "S"
