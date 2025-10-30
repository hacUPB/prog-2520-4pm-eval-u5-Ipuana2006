import csv

# crear la lista d temperatura, humedad presion y leer los datos del archivo
humedad = []
temperatura = []
presion = []
with open('C:\\Users\\B09S202est\\Desktop\\VARIABLES.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile,delimiter=";") #se utiliza el método reader
    encabezado = next(lector)
    for fila in lector:          #con el for se itera sobre el objeto para leer
        dato = fila[2] #0.84
        try:
            dato = float(dato.replace(',','.'))
        except:
            print("Dato no encontrado")
            dato = 0.0
        humedad.append(dato)
        print(encabezado[2])
        print(humedad)
    csvfile.seek(0)
    for fila in lector:
        T = fila[0]
        T = int(T)
        temperatura.append(T)
        print(encabezado[0])



