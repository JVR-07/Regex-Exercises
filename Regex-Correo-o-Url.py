import re

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

cadena = input("Ingrese un correo o url: ")

if validar_correo(cadena):
    print(f"'{cadena}' es un correo.")
elif validar_url(cadena):
    print(f"'{cadena}' es una URL.")
else:
    print(f"'{cadena}' NO tiene un formato válido.")
