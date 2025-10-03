import re

def validar_telefono(numero):
    patron = r'^\d{3}[-\s]\d{3}[-\s]\d{4}$'
    
    if re.match(patron, numero):
        return True
    else:
        return False

def main():
    print("Validador de números de teléfono")
    print("Formatos aceptados:")
    print("- XXX-XXX-XXXX (con guiones)")
    print("- XXX XXX XXXX (con espacios)")
    print()
    
    while True:
        telefono = input("Ingrese un número de teléfono (o 'salir' para terminar): ")
        
        if telefono.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        if validar_telefono(telefono):
            print(f"El número '{telefono}' tiene un formato válido.")
        else:
            print(f"El número '{telefono}' NO tiene un formato válido.")
            
if __name__ == "__main__":
    main()