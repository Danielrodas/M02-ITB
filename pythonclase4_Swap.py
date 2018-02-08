# encoding: utf-8
# Daniel Rodas
# Fecha de creación: 08/02/2018

mano_der = "Movil"

mano_iz = "temporal"

mano_extra = ""

print mano_der , ", der" 
print mano_iz , ", iz"
print mano_extra, ", ex"

mano_extra = mano_der
print mano_extra, ", ex" 
print mano_der, ", der"

mano_der = mano_iz
print mano_der, ", der"
print mano_iz,  ", iz"

mano_iz = mano_extra
print mano_iz, ", iz"
print mano_extra , ", ex"
