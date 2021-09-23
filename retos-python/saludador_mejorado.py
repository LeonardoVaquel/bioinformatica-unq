#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Este es un saludador personalizado: ¡Toma tu nombre y apellido y te responde!')
parser.add_argument('-n', '--name',
                    type=str,
                    help='user name', required=True)
parser.add_argument(
    '-s', '--surname',
    type=str,
    help='user surname'
)

args = parser.parse_args()

print(f"¡Hola {args.name} {args.surname}! ¡Bienvendix!")