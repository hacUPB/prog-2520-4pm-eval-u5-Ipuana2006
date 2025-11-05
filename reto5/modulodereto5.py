# moduloreto5.py
import os
import csv
import matplotlib.pyplot as plt


# ------------------ Archivo.txt -----------------

def listar_archivos():
    ruta = input(" Ingresá la ruta (dejar vacío para usar la carpeta actual): ").strip()
    if not ruta: 
        ruta = os.getcwd()  
    
    if os.path.exists(ruta) and os.path.isdir(ruta):
        print(f"\n Archivos en: {ruta}\n")
        for archivo in os.listdir(ruta):
            print(f" - {archivo}")
        print()
    else:
        print(" La ruta no existe o no es una carpeta válida.\n")


def contar_palabras_y_caracteres(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read() 
    palabras = contenido.split() 
    num_palabras = len(palabras) 
    num_caracteres_con_espacios = len(contenido) 
    num_caracteres_sin_espacios = len(contenido.replace(" ", ""))
    print(f"\n Resultados del análisis:")
    print(f" - Número de palabras: {num_palabras}")
    print(f" - Caracteres (con espacios): {num_caracteres_con_espacios}")
    print(f" - Caracteres (sin espacios): {num_caracteres_sin_espacios}\n")


def reemplazar_palabra(ruta):
    palabra_original = input(" Ingresá la palabra que querés reemplazar: ")
    palabra_nueva = input(" Ingresá la nueva palabra: ")
    
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    
    nuevo_contenido = contenido.replace(palabra_original, palabra_nueva)
    
    with open(ruta, 'w', encoding='utf-8') as archivo:
        archivo.write(nuevo_contenido) 
    
    print("\n Reemplazo realizado con éxito.\n")


def histograma_vocales(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        texto = archivo.read().lower() 
    
    vocales = "aeiou"
    conteo = {v: texto.count(v) for v in vocales} 
    
    plt.bar(conteo.keys(), conteo.values())
    plt.title("Histograma de ocurrencias de vocales")
    plt.xlabel("Vocal")
    plt.ylabel("Cantidad")
    plt.show()


def submenu_txt(ruta):
    while True:
        print("\n SUBMENÚ ARCHIVOS .TXT")
        print("1. Contar número de palabras y caracteres")
        print("2. Reemplazar una palabra por otra")
        print("3. Histograma de ocurrencia de las vocales")
        print("4. Volver al menú principal")
        
        opcion = input("Elegí una opción: ")
        
        if opcion == "1":
            contar_palabras_y_caracteres(ruta)
        elif opcion == "2":
            reemplazar_palabra(ruta)
        elif opcion == "3":
            histograma_vocales(ruta)
        elif opcion == "4":
            break
        else:
            print(" Opción inválida, intentá de nuevo.")

# ------------------ Archivo.csv ------------------------

def mostrar_15_filas(ruta):
    try:
        with open(ruta, newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for i, fila in enumerate(lector):
                if i >= 15:
                    break
                print(fila)
    except UnicodeDecodeError:
        with open(ruta, newline='', encoding='latin-1') as archivo:
            lector = csv.reader(archivo)
            for i, fila in enumerate(lector):
                if i >= 15:
                    break
                print(fila)


# de aqui esta echo con ia porque me salieron muchos problemas que no logre solucionarlos yo mismo

def calcular_estadisticas(ruta):
    import csv

    # Intentamos leer el archivo con varias codificaciones
    for encoding in ('utf-8-sig', 'latin-1'):
        try:
            with open(ruta, newline='', encoding=encoding) as archivo:
                # Leemos una muestra para intentar detectar el delimitador
                muestra = archivo.read(4096)
                archivo.seek(0)
                try:
                    dialecto = csv.Sniffer().sniff(muestra)
                    delimitador = dialecto.delimiter
                except csv.Error:
                    delimitador = ';'  
                    print(f"\n No se pudo detectar el delimitador automáticamente. Se usará: '{delimitador}'")

                lector = csv.DictReader(archivo, delimiter=delimitador)
                columnas = [c.strip() for c in lector.fieldnames]

                print("\nColumnas detectadas en el archivo CSV:")
                print(columnas)

                # Pedir columna al usuario
                columna = input("\nIngresá el nombre exacto de la columna que querés analizar: ").strip()

                # Buscar coincidencia flexible
                columnas_lower = [c.lower().replace("�", "n") for c in columnas]
                if columna.lower().strip() in columnas_lower:
                    columna = columnas[columnas_lower.index(columna.lower().strip())]
                else:
                    print(f"No se encontró la columna '{columna}'. Revisá el nombre y volvé a intentar.")
                    return

                # Leer datos numéricos de esa columna
                datos = []
                for fila in lector:
                    valor = fila.get(columna, "").strip().replace(',', '.')
                    try:
                        datos.append(float(valor))
                    except ValueError:
                        continue

                if not datos:
                    print(f"No se encontraron valores numéricos válidos en la columna '{columna}'.")
                    return

                # Calcular estadísticas
                promedio = sum(datos) / len(datos)
                minimo = min(datos)
                maximo = max(datos)

                print(f"\nEstadísticas de la columna '{columna}':")
                print(f" - Promedio: {promedio:.2f}")
                print(f" - Mínimo:   {minimo}")
                print(f" - Máximo:   {maximo}")
                return  # salir si todo salió bien

        except UnicodeDecodeError:
            continue  # probar con otra codificación

    print(" No se pudo leer el archivo con ninguna codificación conocida.")


def graficar_columna(ruta):
    # Intentamos con ambas codificaciones comunes
    for encoding in ('utf-8', 'latin-1'):
        try:
            with open(ruta, newline='', encoding=encoding) as archivo:
                # Leer una muestra para detectar delimitador
                muestra = archivo.read(2048)
                archivo.seek(0)

                try:
                    dialecto = csv.Sniffer().sniff(muestra)
                    delimitador = dialecto.delimiter
                except csv.Error:
                    delimitador = ';'  # usar punto y coma por defecto

                lector = csv.DictReader(archivo, delimiter=delimitador)
                columnas = lector.fieldnames

                print("Columnas detectadas en el archivo CSV:")
                print(columnas)

                columna = input("Ingresá el nombre exacto de la columna numérica a graficar: ").strip()

                # Normalizamos el nombre de la columna
                columnas_lower = [c.lower().strip() for c in columnas]
                if columna.lower().strip() in columnas_lower:
                    columna = columnas[columnas_lower.index(columna.lower().strip())]
                else:
                    print(f"No se encontró la columna '{columna}'. Revisá el nombre y volvé a intentar.")
                    return

                # Leemos los datos numéricos (dentro del with)
                datos = []
                for fila in lector:
                    valor = fila.get(columna, "").strip().replace(',', '.')
                    try:
                        datos.append(float(valor))
                    except ValueError:
                        continue

                if not datos:
                    print(f"No se encontraron datos numéricos válidos en la columna '{columna}'.")
                    return

                # Graficamos los datos
                plt.plot(datos, marker='o')
                plt.title(f"Gráfico de la columna '{columna}'")
                plt.xlabel("Índice")
                plt.ylabel(columna)
                plt.grid(True)
                plt.show()

                break  # Ya lo procesó correctamente, salimos del for encoding
        except UnicodeDecodeError:
            continue
    else:
        print(" No se pudo leer el archivo con ninguna codificación conocida.")




def submenu_csv(ruta):
    while True:
        print("\n SUBMENÚ ARCHIVOS .CSV")
        print("1. Mostrar las 15 primeras filas")
        print("2. Calcular estadísticas de una columna")
        print("3. Graficar una columna completa con los datos")
        print("4. Volver al menú principal")
        
        opcion = input("Elegí una opción: ")
        
        if opcion == "1":
            mostrar_15_filas(ruta)
        elif opcion == "2":
            calcular_estadisticas(ruta)
        elif opcion == "3":
            graficar_columna(ruta)
        elif opcion == "4":
            break
        else:
            print(" Opción inválida, intentá de nuevo.")

