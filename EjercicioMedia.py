'''--------------------- LIBRERIAS -----------------------'''

import pandas as pd
import math
from tkinter import Label, Tk, Button, filedialog, Frame

'''--------------------- FUNCIONES -----------------------'''


def buscarMedia(lista, elementos):
    suma = 0
    for i in lista:
        if (math.isnan(i) == False):
            suma += i
    media = suma / elementos
    return round(media, 2)


def buscarDesviacion(lista, media, elementos):
    suma = 0
    for i in lista:
        if (math.isnan(i) == False):
            operacion = (i-media)**2
            suma += operacion
    divicion = suma / elementos
    ventana = math.sqrt(divicion)
    return round(ventana, 2)


def buscarArchivo():
    file1 = filedialog.askopenfilenames(filetypes=[('Archivos CSV', '*.csv')])
    leerCSV(file1[0])


def limpiar(varFrame):
    separador(varFrame)
    Button(varFrame, text="Limpiar contenido", width="50", fg="black",
           font=("Verdana", 10), command=varFrame.destroy).pack()


def leerCSV(nombre):
    frame2 = Frame(ventana)
    frame2.pack()
    try:
        datosCVS = pd.read_csv(nombre, header=0)
        nombreColumnas = datosCVS.columns
        for columna in nombreColumnas:
            operar(datosCVS, columna, frame2)
    except:
        Label(text="No se ha encontrado un archivo.csv").pack()
    limpiar(frame2)


def operar(datosCVS, columna, varFrame):
    try:
        separador(varFrame)
        Label(varFrame, text="Columna: " + columna, font="bold").pack()
        columnaLista = datosCVS[columna]

        elementos = len(columnaLista)
        media = buscarMedia(columnaLista, elementos)
        desviacionEstandar = buscarDesviacion(columnaLista, media, elementos)

        Label(varFrame, text="La media Es: " + str(media)).pack()
        Label(varFrame, text="La Desviacion estandar Es: " +
              str(desviacionEstandar)).pack()
    except:
        Label(varFrame, text="Dato no valido").pack()


def separador(varFrame):
    Label(varFrame, text="------------------------------------------", fg="red").pack()


'''--------------------- INTERFAZ -----------------------'''

ventana = Tk()

ventana.title("Media y Desviacion CSV")
ventana.resizable(0, 0)
ventana.geometry("650x1000")

Label(text="Software para hallar la media y la desviacion estandar de las "
      "columnas de un archivo .csv", width=650, height=2,
      fg="white", bg="#00A11D", font=("Verdana bold", 10)).pack()

frame = Frame(ventana, bg="#D6D6D6", width=650, height=300)
frame.pack()

Label(frame, text="Ingrese un archivo .csv", width=650, height=2, bg="#D6D6D6",
      fg="black", font=("Verdana", 10)).pack(pady=5)

Button(frame, text="Buscar Archivo", width="50", fg="black", font=("Verdana", 10),
       command=buscarArchivo).pack(pady=5)
ventana.mainloop()