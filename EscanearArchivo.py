import re

def validar_variable(cadena):
    patronVariable = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(patronVariable, cadena) is not None

def validar_entero(numero):
    patronEntero = r'^[-+]?\d+$'
    return re.match(patronEntero, numero) is not None

def validar_decimales(numero):
    patronDecimales = r'^[-+]?(\d+)?\.(\d+)?([eE]\^?[-+]?\d+)?$'
    return re.match(patronDecimales, numero) is not None

def validar_correo(cadena):
    patronCorreo = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$'
    return re.match(patronCorreo, cadena) is not None

def validar_url(cadena):
    patronUrl = r'^(https?://)?(www\.)?[\w.-]+\.[a-zA-Z]{2,}$'
    return re.match(patronUrl, cadena) is not None

def validar_telefono(numero):
    patronNumero = r'^\d{3}[-\s]\d{3}[-\s]\d{4}$'
    return re.match(patronNumero, numero) is not None

def clasificar_palabra(palabra):
    if validar_variable(palabra):
        return "Variable"
    elif validar_entero(palabra):
        return "Entero"
    elif validar_decimales(palabra):
        return "Decimal"
    elif validar_correo(palabra):
        return "Correo"
    elif validar_url(palabra):
        return "URL"
    elif validar_telefono(palabra):
        return "Teléfono"
    else:
        return "No válido"

def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        print("=" * 70)
        print("           RESULTADO DE VALIDACIÓN DEL ARCHIVO")
        print("=" * 70)
        
        total_palabras = 0
        palabras_por_tipo = {
            "Variable": 0, "Entero": 0, "Decimal": 0,
            "Correo": 0, "URL": 0, "Teléfono": 0, "No válido": 0
        }
        
        for numero_linea, linea in enumerate(lineas, 1):
            print(f"\n--- Línea {numero_linea}: {linea.strip()}")
            palabras = linea.strip().split()
            
            for palabra in palabras:
                total_palabras += 1
                tipo = clasificar_palabra(palabra)
                palabras_por_tipo[tipo] += 1
                
                if tipo == "No válido":
                    print(f"   '{palabra}' -> NO VÁLIDO")
                else:
                    print(f"   '{palabra}' -> {tipo}")
        print("\n" + "=" * 70)
        print("                 ESTADÍSTICAS FINALES")
        print("=" * 70)
        print(f"Total de palabras procesadas: {total_palabras}")
        for tipo, cantidad in palabras_por_tipo.items():
            porcentaje = (cantidad / total_palabras) * 100 if total_palabras > 0 else 0
            print(f"  {tipo}: {cantidad} ({porcentaje:.1f}%)")
        
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def main():
    print("==========================================")
    print("|       .: VALIDADOR DE ENTRADAS :.      |")
    print("|                                        |")
    print("| 1. Validar entrada manual              |")
    print("| 2. Validar archivo .txt                |")
    print("==========================================")
    print()
    
    while True:
        print("Opciones:")
        print("1. Validar entrada manual")
        print("2. Validar archivo .txt")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1-3): ").strip()
        
        if opcion == '1':
            entrada = input("\nIngrese una entrada (o 'volver' para menu): ")
            
            if entrada.lower() == 'volver':
                continue
            
            if validar_variable(entrada):
                print(f"'{entrada}' es un nombre válido para una variable.")
            elif validar_entero(entrada):
                print(f"'{entrada}' es un número entero.")
            elif validar_decimales(entrada):
                print(f"'{entrada}' es un número decimal.")
            elif validar_correo(entrada):
                print(f"'{entrada}' es un correo electrónico válido.")
            elif validar_url(entrada): 
                print(f"'{entrada}' es una URL válida.")
            elif validar_telefono(entrada):
                print(f"'{entrada}' es un número de teléfono válido.")
            else:
                print(f"'{entrada}' NO es una entrada válida.")
                
        elif opcion == '2':
            nombre_archivo = input("\nIngrese el nombre del archivo .txt (ej: 'palabras.txt'): ").strip()
            procesar_archivo(nombre_archivo)
            
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()