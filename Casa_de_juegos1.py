# encoding: UTF-8
# Nombre del programa:  Casa de juegos1.py
# hecho por: Daniel A Rodas Flores 

# Procederé a importar os y time
from time import sleep 
from os import system
from random import choice

# en desde la ĺínea 10 asta la 34 será mi portada del programa
system("clear")
print"""






                            -------------------------
                            |                       |
                            |         Casa de       |
                            |                       |
                            |        juegos 1       |
                            |                       |
                            |       Programador:    |
                            |                       |
                            |      Daniel Rodas     |
                            |                       |
                            -------------------------




"""

# variable de entrada al primer bucle
salir1 = "N"
while ( salir1 == "N" ):# Comienzo del bucle
    # Hago cosas
    # Aquí hago u            #                                      # 
            #  Hola bienvenido a Casa de juegos1   #
            #                                      #
            ########################################
            #                                      #
            #   Pres. 0 para Salir                 #
            #                                      #
            #   Pres. 1 para Jugar a Cara o Cruz   #
            #                                      #
            ########################################
na comprovación si desea continuar con el programa
    sleep(3)
    system("clear")
    print """


            ########################################
            #                                      # 
            #  Hola bienvenido a Casa de juegos1   #
            #                                      #
            ########################################
            #                                      #
            #   Pres. 0 para Salir                 #
            #                                      #
            #   Pres. 1 para Jugar a Cara o Cruz   #
            #                                      #
            ########################################
            
            
            
            
      """
    entras_si_no= raw_input("            Introduzca un número: ")# variable para entrar al juego o no
    
    if (entras_si_no == "0" ): # Si presiona 0 saldrá del juego y saldrá una pantalla diciendo: Saliendo
        system("clear")
        print """
    
    
    
    
    
    
    
    
                                ############
                                #          #   
                                # Saliendo #
                                #          #
                                ############
    
 
 
 
 
            
            """ 
        sleep(3)
        system("clear")
        salir1="S"
        
    elif (entras_si_no == "1"): # Si presiona 1 continuará el juego
        
        salir2 = "N"  # creación para el bucle  de inicio del juego
        while salir2 == "N":
            # Hago cosas
            system("clear")
            saldo = 100 # doy valor a la variable saldo
            print """


                    ##################################
                    #                                #
                    #    Bienvenido a Cara o Cruz    #
                    #                                #
                    ##################################
                    ·                                ·
                    ·     Presione C para Cara       ·
                    ·                                ·
                    ··································
                    ·                                ·
                    ·     Presione X para Cruz       ·
                    ·                                ·
                    ··································
                                                    
                      Dispone de:""", saldo,"""€ Para comenzar
                      
                         Apuesta mínima de 10€      
                    ··································
                    """
            
            Que_escoge_el_Jugador = raw_input("                    Haga su selección: ") # Variable para saber que escoge el jugador
            Que_escoge_el_Jugador = Que_escoge_el_Jugador.upper() # paso a mayúscula lo que haya leído del teclado la variable Que_escoge_el_Jugador
           
            ######### Creo una lista de las opciones para el random choice ##############
            lista = ["CARA","CRUZ"]
            #################################################
            
            Lanzamiento_de_moneda = choice(lista)# agarro el valor que asigne el ramdom choice de la variable lista
            
            apuesta = input("                    Introduzca la cantidad que desea apostar: ") # Variable para saber lo que apuesta el jugador
            saldo_perder = saldo - apuesta # resta de saldo y apuesta
            saldo_ganar = apuesta * 2 # Ganancias
            
            salir3 = "N" # para iniciar el nuevo ciclo o un nuevo bucle
            while ( salir3 == "N" ): # comienza un bucle
                # Hago cosas
                if ((apuesta > 9) and (Que_escoge_el_Jugador == "X") and not (apuesta > saldo)) or ((apuesta > 9) and (Que_escoge_el_Jugador == "C") and not (apuesta > saldo)): #Comprovación si cumple requisitos
                    if (Que_escoge_el_Jugador == "C"): # si el jugador escoge C que le asigne el valor de CARA
                        seleccion = "CARA"
                    if (Que_escoge_el_Jugador == "X"): # si el jugador escoge X que le asigne el valor de CRUZ
                        seleccion = "CRUZ"
                    if (Que_escoge_el_Jugador !=  "C" and Que_escoge_el_Jugador !=  "X"):  # Condición de salida
                        
                        seguir_jugando = "S"
                    """
                    Resumiendo las siguientes lineas que si hay coincidencia que lo que eligió el jugador 
                    El jugador gana
                    
                    Esto será así asta el siguiente comentario
                    """
                    elif (Lanzamiento_de_moneda == "CARA") and (seleccion == "CARA"): 
                        system("clear")
                        saldo = saldo - apuesta
                        saldo_ganar = apuesta * 2
                        saldo = saldo + saldo_ganar
                        print "Jugador escoge: ", seleccion
                        print "Maquina escoge: CRUZ"
                        
                        sleep(1)
                        print "Lanzando moneda..."
                        sleep(2)
                        print "\n"
                        print "A caído la moneda, y cayó: ", Lanzamiento_de_moneda
                        print "\n"
                        print "Por lo tanto gana Jugador"
                        print "Su saldo es de:", saldo , "€"
                    elif (Lanzamiento_de_moneda == "CRUZ") and (seleccion == "CRUZ"):
                        system("clear")
                        saldo = saldo - apuesta
                        saldo_ganar = apuesta * 2
                        saldo = saldo + saldo_ganar
                        print "Jugador escoge: ", seleccion
                        print "Maquina escoge: CARA"
                        
                        sleep(1)
                        print "Lanzando moneda..."
                        sleep(2)
                        print "\n"
                        print "A caído la moneda, y cayó: ", Lanzamiento_de_moneda
                        print "\n"
                        print "Por lo tanto gana Jugador"
                        print "Su saldo es de:", saldo , "€"
                    """
                    Resumiendo las siguientes lineas que si no hay coincidencia de lo que eligió el jugador 
                    El jugador pierde
                    
                    Todo lo dicho asta el comentario que pone: Incremento
                    """
                    else:
                        system("clear")
                        saldo = saldo - apuesta
                        print "Jugador escoge: ", seleccion
                        print "Maquina escoge: ", Lanzamiento_de_moneda
                        
                        sleep(1)
                        print "Lanzando moneda..."
                        sleep(2)
                        print "\n"
                        print "A caído la moneda, y cayó: ", Lanzamiento_de_moneda
                        print "\n"
                        print "Por lo tanto gana Maquina"
                        print "Su saldo es de:", saldo , "€"
                    
                    # Incremento
                    if (saldo > 9) :
                        seguir_jugando = raw_input("Desea seguir apostando?  (S/N): ")
                        seguir_jugando = seguir_jugando.upper()
                        # Activo indicador de salida si toca
                        if (seguir_jugando == "S"):# Continuar 
                            system("clear")
                            print """



                    ##################################
                    #                                #
                    #    Bienvenido a Cara o Cruz    #
                    #                                #
                    ##################################
                    ·                                ·
                    ·     Presione C para Cara       ·
                    ·                                ·
                    ··································
                    ·                                ·
                    ·     Presione X para Cruz       ·
                    ·                                ·
                    ··································
                                                    
                      Dispone de:""", saldo,"""€ Para comenzar
                      
                         Apuesta mínima de 10€      
                    ··································
                    """ 
                            Que_escoge_el_Jugador = raw_input("                    Haga su selección: ")
                            Que_escoge_el_Jugador = Que_escoge_el_Jugador.upper()
                            lista = ["CARA","CRUZ"]
                            Lanzamiento_de_moneda = choice(lista)
                            saldo = 100
                            apuesta = input("                    Introduzca la cantidad que desea apostar: ")
                            saldo_perder = saldo - apuesta
                            saldo_ganar = apuesta * 2
                        elif (seguir_jugando == "N"):# Condición de salida
                            system("clear")
                            print """
            
            
            
            
            
            
            
            
                                        ############
                                        #          #   
                                        # Saliendo #
                                        #          #
                                        ############
            
         
         
         
         
                    
                    """
                            sleep(3)
                            system("clear")
                            salir1="S"
                        else: # se repite
                            system("clear")
                            print """



                    ##################################
                    #                                #
                    #    Bienvenido a Cara o Cruz    #
                    #                                #
                    ##################################
                    ·                                ·
                    ·     Presione C para Cara       ·
                    ·                                ·
                    ··································
                    ·                                ·
                    ·     Presione X para Cruz       ·
                    ·                                ·
                    ··································
                                                    
                      Dispone de:""", saldo,"""€ Para comenzar
                      
                         Apuesta mínima de 10€      
                    ··································
                    """ 
                            Que_escoge_el_Jugador = raw_input("                    Haga su selección: ")
                            Que_escoge_el_Jugador = Que_escoge_el_Jugador.upper()
                            lista = ["CARA","CRUZ"]
                            Lanzamiento_de_moneda = choice(lista)
                            saldo = 100
                            apuesta = input("                    Introduzca la cantidad que desea apostar: ")
                            saldo_perder = saldo - apuesta
                            saldo_ganar = apuesta * 2                  
                # Activo indicador de salida si toca                          
                else: 
                    salir3 = "S"
            # Activo indicador de salida si toca
            else:
                salir2 = "N"

            

    else: # Control de errores
        system("clear")
        print """
            ##############################################
            #                                            #
            # Error, no puede utilizar teclas diferentes #
            #                                            #
            ##############################################
             """
                
        salir1 = "N"
