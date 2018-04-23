# encoding: UTF-8
# Nombre del programa: Cara_o_Cruz.py
# hecho por: Daniel A Rodas Flores 

# Procederé a importar os y time
from random import choice
from time import sleep
from os import system 

# en desde la ĺínea 11 asta la 35 será mi portada del programa
system("clear")
print"""






                            -------------------------
                            |                       |
                            |      Cara O Cruz      |
                            |                       |
                            |      Programador:     |
                            |                       |   
                            |      Daniel Rodas     |
                            |                       |
                            -------------------------





"""
sleep(3)
system("clear")
# Aquí hago una comprovación si desea continuar con el programa
print """


            ######################################
            #                                    # 
            #   Hola bienvenido a Cara o Cruz    #
            #                                    #
            ######################################
            #                                    #
            #          Pres. 0 para Salir        #
            #                                    #
            #          Pres. 1 para Jugar        #
            #                                    #
            ######################################
            
            
            
            
      """
# Inicializaciones # Aqui van las variables
salir = "N"
entras_si_no= raw_input("            Introduzca un número: ")

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
    salir="S"
elif (entras_si_no == "1"): # Si presiona 1 continuará el juego
    ###### Crearé una lista de las opciones  que hay

    system("clear")
    print """



                    ##################################
                    #                                #
                    #    BienvenidO a Cara o Cruz    #
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
                
                
                """
    # Inicializaciones
    salir = "N"
    Que_escoge_el_Jugador = raw_input("                    Haga su selección: ")
    Que_escoge_el_Jugador = Que_escoge_el_Jugador.upper()
    lista = ["CARA","CRUZ"]
    Lanzamiento_de_moneda = choice(lista)

    while ( salir=="N" ):
        # Hago cosas
        if (Que_escoge_el_Jugador == "C"):
            seleccion = "CARA"
        if (Que_escoge_el_Jugador == "X"):
            seleccion = "CRUZ"
        if (Que_escoge_el_Jugador !=  "C" and Que_escoge_el_Jugador !=  "X"):  # Condición de salida
            print "\n"
            print "                    ERROR SOLUCIONAR"
            salir = "S"
        elif (Lanzamiento_de_moneda == "CARA") and (seleccion == "CARA"):
            system("clear")
            print "Jugador escoge: ", seleccion
            print "Maquina escoge: CRUZ"
            
            sleep(1)
            print "Lanzando moneda..."
            sleep(2)
            print "\n"
            print "A caído la moneda, y cayó: ", Lanzamiento_de_moneda
            print "\n"
            print "Por lo tanto gana Jugador"
        elif (Lanzamiento_de_moneda == "CRUZ") and (seleccion == "CRUZ"):
            system("clear")
            print "Jugador escoge: ", seleccion
            print "Maquina escoge: CARA"
            
            sleep(1)
            print "Lanzando moneda..."
            sleep(2)
            print "\n"
            print "A caído la moneda, y cayó: ", Lanzamiento_de_moneda
            print "\n"
            print "Por lo tanto gana Jugador"

        else:
            system("clear")
            print "Jugador escoge: ", seleccion
            print "Maquina escoge: ", Lanzamiento_de_moneda
            
            sleep(1)
            print "Lanzando moneda..."
            sleep(2)
            print "\n"
            print "A caído la moneda, y cayó: ", Lanzamiento_de_moneda
            print "\n"
            print "Por lo tanto gana Maquina"  
        

        # Incremento
        continuar = raw_input("Usted desea Jugar otra vez (S/N): ")
        continuar = continuar.upper()
        # Activo indicador de salida si toca
        if ( continuar == "N" ): # Condición de salida
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
                salir = "S"
        elif (continuar == "S"):
            ###### Crearé una lista de las opciones  que hay

            system("clear")
            print """



                    ##################################
                    #                                #
                    #    BienvenidO a Cara o Cruz    #
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
                
                
                """
            # Inicializaciones
            Que_escoge_el_Jugador = raw_input("                    Haga su selección: ")
            Que_escoge_el_Jugador = Que_escoge_el_Jugador.upper()
            lista = ["CARA","CRUZ"]
            Lanzamiento_de_moneda = choice(lista)
        else: 
            system("clear")
            print """
        ##############################################
        #                                            #
        # Error, no puede utilizar teclas diferentes #
        #                                            #
        ##############################################
        """
            
            salir = "S"
else: # Control de errores
    system("clear")
    print """
        ##############################################
        #                                            #
        # Error, no puede utilizar teclas diferentes #
        #                                            #
        ##############################################
        """
            
    salir = "S"

