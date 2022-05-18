#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la librería csv respectivamente
from test import tester
import csv

def solucion():

    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.

    header = ["Indice", "Fecha", "Open", "Close", "Variacion_diaria", "Descripcion"]
    file_name = "analisis_bitcoin.csv"
    file_nam2 = "BTC-USD.csv"
    f = open(file_name, 'w', newline='')
    f = csv.writer(f, delimiter =';')
    f.writerow(header)
    i = 0
    sumatoria = 0
    menor_precio = "null"
    mayor_precio = "null"
    fecha_menor_precio = ""
    fecha_mayor_precio = ""

    with open(file_nam2, 'r') as file:

        reader = csv.reader(file)
        for row in reader:
            if i > 0:
                if menor_precio == "null":
                    menor_precio = row[1]
                    fecha_menor_precio = row[0]
                elif menor_precio > row[1]:
                    menor_precio = row[1]
                    fecha_menor_precio = row[0]

                if mayor_precio == "null":
                    mayor_precio = row[1]
                    fecha_mayor_precio = row[0]
                elif mayor_precio < row[1]:
                    mayor_precio = row[1]
                    fecha_mayor_precio = row[0]

                diff = float(row[4]) - float(row[1])
                sumatoria = sumatoria + diff
                if diff > 0:
                    estado = "Sube"
                elif diff < 0:
                    estado = "Baja"
                else:
                    estado = "Estable"
                dato = [i -1] + [row[0]] + [row[1]] + [row[4]] + [diff] + [estado]
                f.writerow(dato)
            i = i +1

        variacion_diaria_media = sumatoria / i

        return str(fecha_menor_precio), float(menor_precio), str(fecha_mayor_precio), float(mayor_precio), float(variacion_diaria_media)

tester(solucion)