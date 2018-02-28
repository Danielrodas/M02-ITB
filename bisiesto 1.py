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
# Comentarlo en clases o en privado...para encontrar error
if not( ((resto_cuatro != 0) or (resto_cien == 0)) and ( resto_cuatrocientos !=0) ):
    
    print "\n"
    print "\n"
    print "                El año", year,"es bisiesto"
    print "\n"
    print "\n"
    
else:
    
    print "\n"
    print "\n"
    print "                El año", year,"no es bisiesto"
    print "\n"
    print "\n"
     
""" Pequeña explicación de los resultados
si es multiplo de 4 y no de 100 == bisiesto
si es multiplo de 4 y de 100 ==  no bisiesto
si es multiplo de 400 y de 100 == bisiesto
si es multiplo de 400 y no de 100 == no bisiesto
"""

