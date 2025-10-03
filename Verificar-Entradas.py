import re

def validar_variable(cadena):

    patron = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    
    if re.match(patron, cadena):
        return True
    else:
        return False
    
def validar_entero(numero):
    patronEntero = r'^[-+]?\d+$'
    if re.match(patronEntero, numero):
        return True
    else: 
        return False
    
def validar_decimales(numero):
    patronDecimales = r'^[-+]?(\d+)?\.(\d+)?([eE]\^?[-+]?\d+)?$'
    if re.match(patronDecimales, numero):
        return True
    else:
        return False

def validar_correo(cadena):
    patronCorreo = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$'
    if re.match(patronCorreo, cadena):
        return True
    else:
        return False

def validar_url(cadena):
    patronUrl = r'^(https?://)?(www\.)?[\w.-]+\.[a-zA-Z]{2,}$'
    if re.match(patronUrl, cadena):
        return True
    else:
        return False
    
def validar_telefono(numero):
    patron = r'^\d{3}[-\s]\d{3}[-\s]\d{4}$'
    
    if re.match(patron, numero):
        return True
    else:
        return False

def main():
    print("------------------------------------------")
    print("|       .: VALIDADOR DE ENTRADAS :.       |")
    print("| Nombres de Variables:                   |")
    print("| - Empezar con letra o guion bajo [ _ ]  |")
    print("| Números enteros o decimales:            |")
    print("| - Positivos y negativos                 |")
    print("| Correos Electrónicos:                   |")
    print("| - ejemplo@dominio.com                   |")
    print("| URLs:                                   |")
    print("| - http://www.ejemplo.com ó ejemplo.com  |")
    print("------------------------------------------")
    print()
    
    while True:
        entrada = input("Ingrese una entrada (o 'salir' para terminar): ")
        
        if entrada.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        if validar_variable(entrada):
            print(f"'{entrada}'es un nombre valido para una variable.")
        elif validar_entero(entrada):
            print(f"'{entrada}' es un número entero.")
        elif validar_decimales(entrada):
            print(f"'{entrada}' es un número decimal.")
        elif validar_correo(entrada):
            print(f"{entrada}' es un correo electrónico válido.")
        elif validar_url(entrada): 
            print(f"'{entrada}' es una URL válida.")
        elif validar_telefono(entrada):
            print(f"'{entrada}' es un número de teléfono válido.")
        else:
            print(f"'{entrada}' NO es una entrada válida para ninguno de los casos.")

if __name__ == "__main__":
    main()