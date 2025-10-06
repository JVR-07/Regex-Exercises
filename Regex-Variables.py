import re

from EscanearArchivo import validar_decimales

def validar_variable(cadena):

    patron = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    
    if re.match(patron, cadena):
        return True
    else:
        return False

entrada = input("Ingrese el nombre de una variable: ")

if validar_variable(entrada):
    print(f"'{entrada}' es un nombre de variable válido.")
else:
    print(f"'{entrada}' NO es un nombre de variable válido.")
