import os
import modulodereto5 as mr5



def main():
    while True:
        print("----------------------------")
        print("         MENÚ PRINCIPAL          ")
        print("----------------------------\n")
        print("1. Listar archivos en la ruta actual o una ruta específica")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")

        opcion = input("Elegí una opción (1-4): ").strip()  # elimina espacios antes y después

        if opcion == "1":
            # Listar archivos
            ruta = input("Ingresá una ruta (o dejá vacío para la carpeta actual): ").strip()
            if ruta == "":
                ruta = os.getcwd()  # carpeta actual
            elif not os.path.exists(ruta):
                print(f" La ruta '{ruta}' no existe.")
                continue

            print(f"\n Archivos en: {ruta}")
            archivos = os.listdir(ruta)
            if not archivos:
                print(" No se encontraron archivos en esta carpeta.")
            else:
                for archivo in archivos:
                    print("  -", archivo)

        elif opcion == "2":
            # Archivos de texto
            ruta = input("Ingresá la ruta del archivo .txt: ").strip()
            if os.path.exists(ruta) and ruta.lower().endswith(".txt"):
                mr5.submenu_txt(ruta)
            else:
                print(" Archivo no encontrado o formato incorrecto (.txt requerido).")

        elif opcion == "3":
            # Archivos CSV
            ruta = input("Ingresá la ruta del archivo .csv: ").strip()
            if os.path.exists(ruta) and ruta.lower().endswith(".csv"):
                mr5.submenu_csv(ruta)
            else:
                print(" Archivo no encontrado o formato incorrecto (.csv requerido).")

        elif opcion == "4":
            print(" ¡Hasta luego!")
            break

        else:
            print(" Opción inválida. Intentá nuevamente.")


if __name__ == "__main__":
    main()

