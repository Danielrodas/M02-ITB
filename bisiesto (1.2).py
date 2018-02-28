# encoding: UTF-8
# Daniel Rodas
# Fecha de creación : 28/02/2018


import os


os.system("clear")
year= input("""




                ######################################
                ## Bienvenido al comparador de años ##
                ######################################



                Introducir un año: """)  



resto_cien = year % 100
resto_cuatro = year % 4
resto_cuatrocientos = year % 400

# Estableceré un control de errores en el cual no se puede utilizar el 0
if ( year == 0 ):
    
    print "\n"
    print "\n"
    print "                No se puede utilizar el 0 para establecer un año"
    print "\n"
    print "\n"
# Comprovaré que no sean número 
elif( resto_cien != 0 ):
    print "\n"
    print "\n"    
    print "                El año", year,"no es bisiesto"
    print "\n"
    print "\n"    

else:
    # Ahora definiré los que son años bisiestos
    if ( resto_cuatro == 0 ) or ( resto_cuatrocientos == 0 ):
    
        print "\n"
        print "\n"    
        print "                El año", year,"es bisiesto"
        print "\n"
        print "\n"

