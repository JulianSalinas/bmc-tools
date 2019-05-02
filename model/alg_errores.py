# ----------------------------------------------------------------------------------------------------------------------

import inspect
import numpy as np

# ----------------------------------------------------------------------------------------------------------------------


class AlgErrores(object):

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self, texto, fragmentos):
        self.texto = texto
        self.fragmentos = np.array(fragmentos)
        self.errores = []

    # ------------------------------------------------------------------------------------------------------------------

    def agregar_errores(self, dic_errores):

        self.fragmentos = self.aplicar_errores(dic_errores["sustituciones"], self.sustitucion)
        self.fragmentos = self.aplicar_errores(dic_errores["inserciones"], self.insercion)
        self.fragmentos = self.aplicar_errores(dic_errores["deleciones"], self.delecion)
        self.fragmentos = self.aplicar_errores(dic_errores["inversiones"], self.insercion)
        self.fragmentos = self.aplicar_quimeras(dic_errores["quimeras"])

        return self.fragmentos

    # ----------------------------------- ------------------------------------------------------------------------------

    def aplicar_errores(self, porcentaje, funcion):

        cantidad = int(porcentaje / 100 * len(self.fragmentos))
        indices = np.sort(np.random.choice(len(self.fragmentos), cantidad, False))
        self.fragmentos[indices] = [funcion(frag) for frag in self.fragmentos[indices]]

        return self.fragmentos

    # ------------------------------------------------------------------------------------------------------------------

    def aplicar_quimeras(self, porcentaje):

        cantidad = int(porcentaje / 100 * len(self.fragmentos))
        quimeras = [self.quimera() for i in range(cantidad)]
        self.fragmentos = np.append(self.fragmentos, quimeras)

        return self.fragmentos

    # ------------------------------------------------------------------------------------------------------------------

    def sustitucion(self, cadena):

        cadena_antes = cadena
        cadena = list(cadena)
        texto = list(self.texto.replace(" ", ""))

        indice_sustituto = np.random.randint(0, len(texto))
        indice_sustitucion = np.random.randint(0, len(cadena))

        cadena[indice_sustitucion] = texto[indice_sustituto]
        cadena_despues = "".join(cadena)

        self.errores.append(("sustitucion", cadena_antes, cadena_despues))
        return cadena_despues

    # ------------------------------------------------------------------------------------------------------------------

    def insercion(self, cadena):

        cadena_antes = cadena
        cadena = list(cadena)
        dominio = list(self.texto.replace(" ", ""))

        indice_insertar = np.random.randint(0, len(dominio))
        indice_insercion = np.random.randint(0, len(cadena))

        cadena.insert(indice_insercion, dominio[indice_insertar])
        cadena_despues = "".join(cadena)

        self.errores.append(("insercion", cadena_antes, cadena_despues))
        return cadena_despues

    # ------------------------------------------------------------------------------------------------------------------

    def delecion(self, cadena):

        cadena_antes = cadena
        cadena = np.array(list(cadena))

        indice_delecion = np.random.randint(0, len(cadena))
        indices_conservar = np.delete(range(0, len(cadena)), indice_delecion)

        cadena = cadena[indices_conservar]
        cadena_despues = "".join(cadena)

        self.errores.append(("delecion", cadena_antes, cadena_despues))
        return cadena_despues

    # ------------------------------------------------------------------------------------------------------------------

    def inversion(self, cadena):

        cadena_despues = cadena[::-1]

        self.errores.append(("inversion", cadena, cadena_despues))
        return cadena_despues

    # ------------------------------------------------------------------------------------------------------------------

    def quimera(self):

        indice = lambda: np.random.randint(0, len(self.fragmentos))
        elegidos = self.fragmentos[indice()], self.fragmentos[indice()]
        quimera = elegidos[0] + elegidos[1]

        self.errores.append(("quimera", elegidos, quimera))
        return quimera

# ----------------------------------------------------------------------------------------------------------------------
