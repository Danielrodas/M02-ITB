#encoding
#Daniel Rodas
#Fecha de creación : 22/02/2018  modificación: 01/03/2018
cajon1 = "Movil"
cajon2 = "Bocadillo"
cajon3 = "Boli"
cajon4 = "bebida"

print cajon1 , "    C1"
print cajon2 , "    C2" 
print cajon3 , "    C3" 
print cajon4 , "    C4" 

print "\n"
print "\n"


cajon_extra= cajon1
cajon1 = cajon3
cajon3 = cajon_extra

cajon2 = "Bocadillo"
cajon_extra = cajon2
cajon4 = "bebida"

cajon_extra = cajon2
cajon2=cajon4
cajon4=cajon_extra

print cajon1 , "    C1"
print cajon2 , "    C2" 
print cajon3 , "    C3" 
print cajon4 , "    C4"

print "\n"
print "\n"
