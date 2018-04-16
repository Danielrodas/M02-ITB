# encoding: UTF-8
# Nombre del programa ejercicio-bucle-promedio.py
# hecho por: Daniel A Rodas Flores 

# Procederé a importar os , time y de random importaré randint
import time 
import os
from random import randint

# en desde la ĺínea 10 asta la 34 será mi portada del programa
os.system("clear")
print"""





                            -------------------------
                            |                       |
                            |     Piedra, papel     |
                            |                       |
                            |        tijeras        |
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
            # Hola bienvenido a Piedra papel o tijeras #
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
turno_machine = 0
entras_si_no= raw_input("            Introduzca un número: ")
Gana_machine = 0
Gana_humano = 0
salir2= "N"

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

elif(entras_si_no == "1" ): # si presiona el 1 continuará con el juego y procedemos a mostrar el menú de piedra, papel o tijeras
    os.system("clear")
    print """
    
                    ########################################
                    #                                      #
                    #    Presione 1 para piedra  --- PI    #
                    #                                      #
                    #    Presione 2 para papel   --- PA    #
                    #                                      #
                    #    Presione 3 para tijeras --- TI    #
                    #                                      #
                    ########################################
          """
          
    # en la siguiente linea pido que el jugador haga su selección
    humano= raw_input("        Haga su selección (Tambien puede escribir el nombre de la cosa) \n        o escribir su abreviatura (PI/PA/TI):  ")
    humano = humano.upper() # Paso a mayúsculas el resultado si es letra
    
    while ( salir=="N" ): # procedemos a entrar en bucle para continuar jugando
        # Hago cosas
        machine = randint(1,3)
            
            # asta el primer comentario que haya se miran que sean iguales para establecer un empate
        if (machine == 1 and humano == "1") or (machine == 1 and humano == "PI"):
            turno_humano = "Piedra"
            turno_machine = "Piedra" 
            print "\n"
            print "        Jugador escoge:",turno_humano
            time.sleep(0.2)
            print "        Maquina escoge",turno_machine
            print "\n"
            print "        Hay un empate"
            
        elif (machine == 2 and humano == "2") or (machine == 2 and humano == "PA"):
            turno_humano = "Papel"
            turno_machine = "Papel" 
            print "\n"
            print "        Jugador escoge:",turno_humano
            time.sleep(0.2)
            print "        Maquina escoge",turno_machine
            print "\n"
            print "        Hay un empate"

        elif (machine == 3 and humano == "3") or (machine == 3 and humano == "TI"):
            turno_humano = "Tijeras"
            turno_machine = "Tijeras" 
            print "\n"
            print "        Jugador escoge:",turno_humano
            time.sleep(0.2)
            print "        Maquina escoge",turno_machine
            print "\n"
            print "        Hay un empate"

            # a partir de aqui se comprueba si gana machine
        elif (machine == 1 and humano == "3") or (machine == 1 and humano == "TI"):
            turno_machine = "Piedra"
            turno_humano = "Tijeras"
            print "\n"
            print "        Jugador escoge: ",turno_humano
            time.sleep(0.2)
            print "        Maquina escoge: ",turno_machine
            print "\n"
            print "        Gana MACHINE"
            Gana_machine = Gana_machine +1  #Gana puntos

        elif (machine == 2 and humano == "1") or (machine == 2 and humano == "PI"):
            turno_machine = "Papel"
            turno_humano = "Piedra"
            print "\n"
            print "        Jugador escoge: ",turno_humano
            time.sleep(0.2)
            print "        Maquina escoge: ",turno_machine
            print "\n"
            print "        Gana MACHINE"
            Gana_machine = Gana_machine +1 #Gana puntos
            
        elif (machine == 3 and humano == "2") or (machine == 1 and humano == "PA"):
            turno_machine = "Tijeras"
            turno_humano = "Papel"
            print "\n"
            print "        Jugador escoge: ",turno_humano
            time.sleep(0.2)
            print "        Maquina escoge: ",turno_machine
            print "\n"
            print "        Gana MACHINE"
            Gana_machine = Gana_machine +1   #Gana puntos          

            # a partir de aqui compruebo que gane Humano
        elif (machine == 3 and humano == "1") or (machine == 3 and humano == "PI"):
            turno_machine = "Tijeras"
            turno_humano = "Piedra"
            print "\n"
            print "        Jugador escoge: ",turno_humano
            time.sleep(0.2)
            print "        Maquina escoge: ",turno_machine
            print "\n"
            print "        Gana jugador"
            Gana_humano = Gana_humano + 1 #Gana puntos
            
        elif (machine == 1 and humano == "2") or (machine == 1 and humano == "PA"):
            turno_machine = "Tijeras"
            turno_humano = "Piedra"
            print "\n"
            print "        Jugador escoge: ",turno_humano
            time.sleep(0.2)
            print "        Maquina escoge: ",turno_machine
            print "\n"
            print "        Gana jugador"
            Gana_humano = Gana_humano + 1 #Gana puntos
                        

        elif (machine == 2 and humano == "3") or (machine == 2 and humano == "TI"):
            turno_machine = "Papel"
            turno_humano = "Tijeras"
            print "\n"
            print "        Jugador escoge: ",turno_humano
            time.sleep(0.2)
            print "        Maquina escoge: ",turno_machine
            print "\n"
            print "        Gana jugador"
            Gana_humano = Gana_humano + 1 #Gana puntos
            
        else: # Prueba de errores si se equivoca el usuario sale del programa y quien ganó
            os.system("clear")
            print """
        ##############################################
        #                                            #
        # Error, no puede utilizar teclas diferentes #
        #                                            #
        ##############################################
         """
            
            salir = "S"
        
        # Incremento
            # pregunto si quiere continuar jugando
        print "\n"
        continuar = raw_input("        Desea continuar jugando (S/N): ")
        
        continuar = continuar.upper() # Paso a mayuscula la variable continuar
        # Activo indicador de salida si toca
        if ( continuar == "N" or continuar == "NO" ): # Condición de salida
                salir = "S"
                
        elif ( continuar == "S" or continuar == "SI" ): # si presiona S o escribe SI continuará jugando
            os.system("clear")
            print """
            
                    ########################################
                    #                                      #
                    #    Presione 1 para piedra  --- PI    #
                    #                                      #
                    #    Presione 2 para papel   --- PA    #
                    #                                      #
                    #    Presione 3 para tijeras --- TI    #
                    #                                      #
                    ########################################
                  """
            humano= raw_input("        Haga su selección (Tambien puede escribir el nombre de la cosa) \n        o escribir su abreviatura (PI/PA/TI):  ")
            humano = humano.upper()
        else:
            os.system("clear")
            print """
        ##############################################
        #                                            #
        # Error, no puede utilizar teclas diferentes #
        #                                            #
        ##############################################
         """
            
            salir = "S"
            
     # Una vez salido del bucle compruebo quien hizo más puntos
     
    if (Gana_humano > Gana_machine): # Compruebo si el jugador obtuvo más puntos
        os.system("clear")
        print "\n"
        print "        Puntos totales de jugador: ", Gana_humano
        print "        Puntos totales de maquina: ", Gana_machine
        time.sleep(0.1)
        total= Gana_humano - Gana_machine
        print "\n"
        print "        Gana Jugador por:" ,total, "Puntos"
        
    elif (Gana_humano < Gana_machine): # Compruebo si el machine obtuvo más puntos
        os.system("clear")
        print "\n"
        print "        Puntos totales de jugador: ", Gana_humano
        print "        Puntos totales de maquina: ", Gana_machine
        time.sleep(0.1)
        total= Gana_machine - Gana_humano
        print "\n"
        print "        Gana machine por:" ,total, "Puntos"
        
    else: # Compruebo si en cantidad de puntos an obtenido puntuación igualitarias
        os.system("clear")
        print "\n"
        print "        En puntos totales, jugador y maquina, han quedado empatados"
else:
    os.system("clear")
    print """
        ##############################################
        #                                            #
        # Error, no puede utilizar teclas diferentes #
        #                                            #
        ##############################################
         """
            
    salir = "S"

