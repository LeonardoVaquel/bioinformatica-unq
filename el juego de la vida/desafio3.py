#!/usr/bin/env python3

# Creá un script en Python que, tomando como input un archivo con una secuencia de ADN, 
# permita identificar las regiones promotoras de un gen, considerando que tal región comienza y termina con la caja TATA.

import argparse

BOX_REGEX = 'TATA'

def identificador_de_regiones(filepath):
    with open(filepath) as file:
        cadena = file.read()
    result = cadena.strip('\n').split(BOX_REGEX)[1:]
    print('Regiones de la secuencia de ADN:')
    for r in result: print('- ',r)


parser = argparse.ArgumentParser(description='Descripcion')
parser.add_argument('-f', '--file',
                    type=str,
                    help='File path', required=True)

args = parser.parse_args()

identificador_de_regiones(args.file)