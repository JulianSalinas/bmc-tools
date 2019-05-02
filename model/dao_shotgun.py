# ----------------------------------------------------------------------------------------------------------------------
import json
from util.file import *

# ----------------------------------------------------------------------------------------------------------------------


class DAOShotgun(object):

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.archivo_entrada = "../files/entrada.txt"
        self.archivo_salida_fragmentos = "../files/salida.txt"
        self.archivo_salida_descripcion = "../files/salida.json"

    # ------------------------------------------------------------------------------------------------------------------

    def abrir_archivo_entrada(self, nombre_archivo):
        cadena = open_file(nombre_archivo)
        return cadena.replace("\n", " ")

    # ------------------------------------------------------------------------------------------------------------------

    def abrir_archivo_fragmentos(self, nombre_archivo):
        cadena = open_file(nombre_archivo)
        return cadena.split("\n")

    # ------------------------------------------------------------------------------------------------------------------

    def guardar_archivo_fragmentos(self, fragmentos, nombre_archivo):
        cadena = "".join([fragmento + "\n" for fragmento in fragmentos])
        save_file(nombre_archivo, cadena)

    # ------------------------------------------------------------------------------------------------------------------

    def abrir_archivo_descriptivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as fp:
            return json.load(fp)

    # ------------------------------------------------------------------------------------------------------------------

    def guardar_archivo_descriptivo(self, diccionario, nombre_archivo):
        with open(nombre_archivo, 'w') as fp:
            json.dump(diccionario, fp, indent=4)

# ----------------------------------------------------------------------------------------------------------------------
