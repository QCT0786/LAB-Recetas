from typing import NamedTuple, List
from datetime import *
import csv

# Definición de los NamedTuple
Ingrediente = NamedTuple("Ingrediente",
                         [("nombre", str),
                          ("cantidad", float),
                          ("unidad", str)])

Receta = NamedTuple("Receta",
                    [("denominacion", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", List[Ingrediente]),
                     ("tiempo", int),
                     ("calorias", int),
                     ("fecha", date),
                     ("precio", float)])

def lee_recetas(ruta_archivo: str)->list[Receta]:
    with open(ruta_archivo, encoding = "utf-8") as f:
        lector = csv.reader(f, delimiter = ";")
        next(lector)
        lista = []
        for denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio in lector:
            denominacion = str(denominacion)
            tipo = str(tipo)
            dificultad = str(dificultad)
            ingredientes = parsear_ingredientes(ingredientes)
            tiempo = int(tiempo)
            calorias = int(calorias)
            fecha = datetime.strptime(fecha, "%d/%m/%Y")
            precio = float(precio.replace(",","."))
            lista.append(Receta(denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio))
        return lista





def parsear_ingredientes(cadena: str)-> list[Ingrediente]:
    lista = []
    if len(cadena)>0:
        for i in cadena.split(","):
            lista.append(parsear_ingrediente(i))
    return lista

def parsear_ingrediente(cadena2: str)-> Ingrediente:

    tupla = cadena2.split("-") 
    nombre = tupla[0]
    cantidad = float(tupla[1].replace(",", "."))
    unidad = tupla[2]

    return Ingrediente(nombre, cantidad, unidad)
