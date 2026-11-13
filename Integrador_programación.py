import csv
import os

NOMBRE_ARCHIVO = "paises.csv"

# --- PALETA DE COLORES ANSI PARA LA CONSOLA ---
RESET = "\033[0m"
NEGRITA = "\033[1m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
CIAN = "\033[36m"
BLANCO_FONDO = "\033[37;1m"

def inicializar_csv():
    """Crea el archivo CSV con datos iniciales si no existe."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        datos_iniciales = [
            ["nombre", "poblacion", "superficie", "continente"],
            ["Argentina", "45376763", "2780400", "América"],
            ["Japón", "125800000", "377975", "Asia"],
            ["Brasil", "213993437", "8515767", "América"],
            ["Alemania", "83149300", "357022", "Europa"]
        ]
        try:
            with open(NOMBRE_ARCHIVO, mode='w', newline='', encoding='utf-8') as f:
                escritor = csv.writer(f)
                escritor.writerows(datos_iniciales)
        except IOError:
            print(f"{ROJO}Error: No se pudo crear el archivo base.{RESET}")

def cargar_paises():
    """Lee el archivo CSV y devuelve una lista de diccionarios."""
    lista_paises = []
    if not os.path.exists(NOMBRE_ARCHIVO):
        inicializar_csv()
        
    try:
        with open(NOMBRE_ARCHIVO, mode='r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    lista_paises.append(pais)
                except (ValueError, KeyError):
                    print(f"{AMARILLO}Advertencia: Fila omitida por errores de formato.{RESET}")
    except IOError:
        print(f"{ROJO}Error: No se pudo leer el archivo CSV.{RESET}")
    return lista_paises

def guardar_paises(lista_paises):
    """Guarda la lista de diccionarios en el archivo CSV."""
    try:
        with open(NOMBRE_ARCHIVO, mode='w', newline='', encoding='utf-8') as f:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            for pais in lista_paises:
                escritor.writerow(pais)
        return True
    except IOError:
        print(f"{ROJO}Error: No se pudieron guardar los cambios en el archivo.{RESET}")
        return False

def mostrar_tabla(lista):
    """Muestra una lista de países formateada en consola con colores."""
    if not lista:
        print(f"\n{AMARILLO}--- No hay países para mostrar con ese criterio ---{RESET}")
        return
    print(f"\n{NEGRITA}{CIAN}{'Nombre':<20} | {'Población':<15} | {'Superficie (km²)':<18} | {'Continente':<15}{RESET}")
    print(f"{CIAN}" + "-" * 75 + f"{RESET}")
    for p in lista:
        print(f"{p['nombre']:<20} | {p['poblacion']:<15,} | {p['superficie']:<18,} | {p['continente']:<15}")
    print(f"{CIAN}" + "-" * 75 + f"{RESET}")

def solicitar_entero_positivo(mensaje):
    """Valida que la entrada sea un número entero mayor que cero."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print(f"{ROJO}Por favor, ingrese un número mayor a 0.{RESET}")
        except ValueError:
            print(f"{ROJO}Entrada inválida. Debe ser un número entero.{RESET}")

def solicitar_texto(mensaje):
    """Valida que la entrada de texto no esté vacía."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print(f"{ROJO}Este campo no puede quedar vacío.{RESET}")

# --- FUNCIONALIDADES DEL SISTEMA ---

def agregar_pais(lista_paises):
    print(f"\n{NEGRITA}{AZUL}--- AGREGAR NUEVO PAÍS ---{RESET}")
    nombre = solicitar_texto("Nombre del país: ")
    
    for p in lista_paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"{ROJO}Error: Este país ya se encuentra registrado.{RESET}")
            return

    poblacion = solicitar_entero_positivo("Cantidad de población: ")
    superficie = solicitar_entero_positivo("Superficie en km²: ")
    continente = solicitar_texto("Continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(nuevo_pais)
    if guardar_paises(lista_paises):
        print(f"{VERDE}Éxito: '{nombre}' ha sido agregado correctamente.{RESET}")

def actualizar_pais(lista_paises):
    print(f"\n{NEGRITA}{AZUL}--- ACTUALIZAR DATOS DE UN PAÍS ---{RESET}")
    nombre = solicitar_texto("Ingrese el nombre del país a modificar: ")
    
    for p in lista_paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"{AMARILLO}Modificando datos para {p['nombre']}:{RESET}")
            p["poblacion"] = solicitar_entero_positivo("Nueva población: ")
            p["superficie"] = solicitar_entero_positivo("Nueva superficie en km²: ")
            if guardar_paises(lista_paises):
                print(f"{VERDE}Éxito: Datos actualizados correctamente en el disco.{RESET}")
            return
    print(f"{ROJO}Error: El país buscado no existe.{RESET}")

def buscar_pais(lista_paises):
    print(f"\n{NEGRITA}{AZUL}--- BUSCAR PAÍS ---{RESET}")
    criterio = solicitar_texto("Ingrese el nombre (coincidencia parcial o exacta): ").lower()
    resultados = [p for p in lista_paises if criterio in p["nombre"].lower()]
    mostrar_tabla(resultados)

def filtrar_paises(lista_paises):
    print(f"\n{NEGRITA}{AZUL}--- FILTRAR PAÍSES ---{RESET}")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    opcion = input("Seleccione una opción de filtrado: ")

    resultados = []
    if opcion == "1":
        continente = solicitar_texto("Ingrese el continente: ").lower()
        resultados = [p for p in lista_paises if p["continente"].lower() == continente]
    elif opcion == "2":
        min_pob = solicitar_entero_positivo("Población mínima: ")
        max_pob = solicitar_entero_positivo("Población máxima: ")
        resultados = [p for p in lista_paises if min_pob <= p["poblacion"] <= max_pob]
    elif opcion == "3":
        min_sup = solicitar_entero_positivo("Superficie mínima: ")
        max_sup = solicitar_entero_positivo("Superficie máxima: ")
        resultados = [p for p in lista_paises if min_sup <= p["superficie"] <= max_sup]
    else:
        print(f"{ROJO}Opción inválida.{RESET}")
        return

    mostrar_tabla(resultados)

def ordenar_paises(lista_paises):
    print(f"\n{NEGRITA}{AZUL}--- ORDENAR PAÍSES ---{RESET}")
    print("1. Por Nombre")
    print("2. Por Población")
    print("3. Por Superficie")
    criterio_opc = input("Seleccione el criterio de ordenación: ")
    
    criterio_map = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    if criterio_opc not in criterio_map:
        print(f"{ROJO}Opción inválida.{RESET}")
        return
    
    campo = criterio_map[criterio_opc]
    
    print("1. Ascendente")
    print("2. Descendente")
    sentido_opc = input("Seleccione el sentido: ")
    
    descendente = False
    if sentido_opc == "2":
        descendente = True
    elif sentido_opc != "1":
        print(f"{ROJO}Opción inválida.{RESET}")
        return

    # Ordenamiento burbuja académico
    lista_ordenada = list(lista_paises)
    n = len(lista_ordenada)
    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = lista_ordenada[j][campo]
            val2 = lista_ordenada[j+1][campo]
            
            if isinstance(val1, str):
                val1 = val1.lower()
                val2 = val2.lower()

            if (not descendente and val1 > val2) or (descendente and val1 < val2):
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]

    mostrar_tabla(lista_ordenada)

def mostrar_estadisticas(lista_paises):
    if not lista_paises:
        print(f"{ROJO}\nNo hay datos cargados para calcular estadísticas.{RESET}")
        return

    print(f"\n{NEGRITA}{AMARILLO}======================================={RESET}")
    print(f"{NEGRITA}{AMARILLO}       ESTADÍSTICAS GENERALES          {RESET}")
    print(f"{NEGRITA}{AMARILLO}======================================={RESET}")
    
    pais_mayor_pob = max(lista_paises, key=lambda x: x["poblacion"])
    pais_menor_pob = min(lista_paises, key=lambda x: x["poblacion"])
    
    total_poblacion = sum(p["poblacion"] for p in lista_paises)
    total_superficie = sum(p["superficie"] for p in lista_paises)
    prom_pob = total_poblacion / len(lista_paises)
    prom_sup = total_superficie / len(lista_paises)
    
    conteos_continente = {}
    for p in lista_paises:
        cont = p["continente"]
        conteos_continente[cont] = conteos_continente.get(cont, 0) + 1

    print(f"{NEGRITA}País con MAYOR población:{RESET} {VERDE}{pais_mayor_pob['nombre']}{RESET} ({pais_mayor_pob['poblacion']:,} hab.)")
    print(f"{NEGRITA}País con MENOR población:{RESET} {AMARILLO}{pais_menor_pob['nombre']}{RESET} ({pais_menor_pob['poblacion']:,} hab.)")
    print(f"{NEGRITA}Promedio de población global:{RESET} {prom_pob:,.2f} habitantes")
    print(f"{NEGRITA}Promedio de superficie global:{RESET} {prom_sup:,.2f} km²")
    print(f"\n{NEGRITA}Cantidad de países por continente:{RESET}")
    for continente, cant in conteos_continente.items():
        print(f" - {CIAN}{continente:<15}{RESET}: {cant}")

# --- MENÚ PRINCIPAL ---

def menu():
    paises = cargar_paises()
    while True:
        print(f"\n{NEGRITA}{AZUL}======================================={RESET}")
        print(f"{NEGRITA}{AZUL}   SISTEMA DE GESTIÓN DE PAÍSES (UTN)  {RESET}")
        print(f"{NEGRITA}{AZUL}======================================={RESET}")
        print(f"{CIAN}1.{RESET} Agregar un país")
        print(f"{CIAN}2.{RESET} Actualizar población y superficie")
        print(f"{CIAN}3.{RESET} Buscar un país por nombre")
        print(f"{CIAN}4.{RESET} Filtrar países")
        print(f"{CIAN}5.{RESET} Ordenar países")
        print(f"{CIAN}6.{RESET} Mostrar estadísticas")
        print(f"{ROJO}7.{RESET} Salir")
        print(f"{AZUL}---------------------------------------{RESET}")
        
        opcion = input("Seleccione una opción (1-7): ").strip()
        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            print(f"\n{VERDE}¡Gracias por utilizar el sistema! Finalizando ejecución...{RESET}\n")
            break
        else:
            print(f"{ROJO}Opción inválida. Intente nuevamente.{RESET}")

if __name__ == "__main__":
    menu()