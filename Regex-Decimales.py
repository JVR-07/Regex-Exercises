import re

def validar_decimales(numero):
    patronDecimales = r'^[-+]?(\d+)?\.(\d+)?([eE]\^?[-+]?\d+)?$'
    if re.match(patronDecimales, numero):
        return True
    else:
        return False

def validar_entero(numero):
    patronEntero = r'^[-+]?\d+$'
    if re.match(patronEntero, numero):
        return True
    else: 
        return False

numero = input("Ingrese un numero entero o decimal: ")

if validar_decimales(numero):
    print(f"'{numero}' es un decimal.")
elif validar_entero(numero):
    print(f"'{numero}' es un entero.")
else:
    print(f"'{numero}' NO es un número.")
