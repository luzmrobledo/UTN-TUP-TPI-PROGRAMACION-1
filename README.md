# Gestión de Datos de Países en Python

**Filtros, ordenamientos y estadísticas con consola de colores**

Trabajo integrador de **Programación 1** · Tecnicatura Universitaria en Programación · Instituto Tecnológico Universitario
Mendoza, 16 de octubre de 2026

---

## Descripción del programa

Sistema de consola escrito en Python que gestiona información de países (nombre, población, superficie en km² y continente). Los datos se almacenan de forma persistente en un archivo CSV y se manipulan desde un menú interactivo con salida en colores ANSI.

**Funcionalidades**

1. **Agregar un país**, con validación de duplicados y de datos numéricos.
2. **Actualizar** la población y la superficie de un país existente.
3. **Buscar** países por nombre (coincidencia parcial o exacta, sin distinguir mayúsculas).
4. **Filtrar** por continente, rango de población o rango de superficie.
5. **Ordenar** por nombre, población o superficie, en forma ascendente o descendente (algoritmo burbuja).
6. **Mostrar estadísticas**: país con mayor y menor población, promedios de población y superficie, y cantidad de países por continente.

**Conceptos aplicados:** funciones, listas y diccionarios, lectura/escritura de archivos CSV, manejo de excepciones, validación de entradas, comprensión de listas, ordenamiento manual y códigos de escape ANSI.

## Instrucciones de uso
1. Elegir una opción del menú ingresando su número (1 a 7) y seguir las indicaciones en pantalla. La opción **7** finaliza el programa.

## Ejemplos de entradas y salidas

Los siguientes ejemplos corresponden a ejecuciones reales a partir del dataset base. Las líneas que siguen a los dos puntos de cada pregunta son las entradas del usuario.

### Menú principal

=======================================
   SISTEMA DE GESTIÓN DE PAÍSES (UTN)  
=======================================
1. Agregar un país
2. Actualizar población y superficie
3. Buscar un país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Salir
---------------------------------------
Seleccione una opción (1-7): 7

¡Gracias por utilizar el sistema! Finalizando ejecución...


### 1. Agregar un país

Seleccione una opción (1-7): 1

--- AGREGAR NUEVO PAÍS ---
Nombre del país: Chile
Cantidad de población: 19493184
Superficie en km²: 756102
Continente: América
Éxito: 'Chile' ha sido agregado correctamente.


Si el nombre ya existe, se muestra `Error: Este país ya se encuentra registrado.`. Si se ingresa un valor no numérico, negativo o cero en población o superficie, se vuelve a pedir el dato.

### 3. Buscar un país

Seleccione una opción (1-7): 3

--- BUSCAR PAÍS ---
Ingrese el nombre (coincidencia parcial o exacta): bra

Nombre               | Población       | Superficie (km²)   | Continente     
---------------------------------------------------------------------------
Brasil               | 213,993,437     | 8,515,767          | América        
---------------------------------------------------------------------------

### 4. Filtrar países (por continente)

Seleccione una opción (1-7): 4

--- FILTRAR PAÍSES ---
1. Por Continente
2. Por Rango de Población
3. Por Rango de Superficie
Seleccione una opción de filtrado: 1
Ingrese el continente: américa

Nombre               | Población       | Superficie (km²)   | Continente     
---------------------------------------------------------------------------
Argentina            | 45,376,763      | 2,780,400          | América        
Brasil               | 213,993,437     | 8,515,767          | América        
---------------------------------------------------------------------------

### 5. Ordenar países (por población, descendente)

Seleccione una opción (1-7): 5

--- ORDENAR PAÍSES ---
1. Por Nombre
2. Por Población
3. Por Superficie
Seleccione el criterio de ordenación: 2
1. Ascendente
2. Descendente
Seleccione el sentido: 2

Nombre               | Población       | Superficie (km²)   | Continente     
---------------------------------------------------------------------------
Brasil               | 213,993,437     | 8,515,767          | América        
Japón                | 125,800,000     | 377,975            | Asia           
Alemania             | 83,149,300      | 357,022            | Europa         
Argentina            | 45,376,763      | 2,780,400          | América        
---------------------------------------------------------------------------

### 6. Mostrar estadísticas

Seleccione una opción (1-7): 6

=======================================
       ESTADÍSTICAS GENERALES          
=======================================
País con MAYOR población: Brasil (213,993,437 hab.)
País con MENOR población: Argentina (45,376,763 hab.)
Promedio de población global: 117,079,875.00 habitantes
Promedio de superficie global: 3,007,791.00 km²

Cantidad de países por continente:
 - América        : 2
 - Asia           : 1
 - Europa         : 1

## Integrantes y participación

Silva, Maia: Constantes de colores, inicializar_csv(), cargar_paises(), guardar_paises(), README y pruebas del CSV con archivos vacíos o dañados.

Sosa, Micaela: solicitar_entero_positivo(), solicitar_texto(), mostrar_tabla(), agregar_pais(), actualizar_pai(), marco teórico y bibliografía del informe.

Ortiz, Ariadna: buscar_pais(), filtrar_paises(), mostrar_estadisticas(), diagramas de flujo y capturas de ejecución.

Robledo, Luz: ordenar_paises() (método burbuja), menu(), bloque __main__, repositorio, integración final y edición del video.

## Enlaces

- **Video explicativo:** (https://drive.google.com/drive/folders/1vO4UGnmGJe-LczFUAZdI95Ix7Oa5eExR?usp=sharing)
- **Informe técnico:** `Informe_TPI_Paises.pdf`
# UTN-TUP-TPI-PROGRAMACION-1
