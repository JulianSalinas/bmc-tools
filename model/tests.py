# ----------------------------------------------------------------------------------------------------------------------

from model.alg_shotgun import *
from model.alg_errores import *
from model.dao_shotgun import *

# ----------------------------------------------------------------------------------------------------------------------
# Abrir el archivo, sustituir saltos de linea por espacios

dao_shotgun = DAOShotgun()
texto = dao_shotgun.abrir_archivo_entrada(nombre_archivo="../files/entrada.txt")

# ----------------------------------------------------------------------------------------------------------------------
# Generacion de fragmentos

alg_shotgun = AlgShotgun({
    "cantidad_fragmentos": 5,
    "promedio_tamanho": 8,
    "desviacion_estandar": 4,
    "rango_traslape": (1, 3)
})

fragmentos = alg_shotgun.generar_fragmentos(texto)
print("Fragmentos sin errores: \n" + str(fragmentos))

# ----------------------------------------------------------------------------------------------------------------------
# Agregar errores a los fragmentos

alg_errores = AlgErrores(texto, fragmentos)

fragmentos = alg_errores.aplicar_errores(porcentaje=50, funcion=alg_errores.sustitucion)
print("Fragmentos con sustituciones: \n" + str(fragmentos))

fragmentos = alg_errores.aplicar_errores(porcentaje=50, funcion=alg_errores.delecion)
print("Fragmentos con deleciones: \n" + str(fragmentos))

fragmentos = alg_errores.aplicar_errores(porcentaje=50, funcion=alg_errores.insercion)
print("Fragmentos con inserciones: \n" + str(fragmentos))

fragmentos = alg_errores.aplicar_errores(porcentaje=50, funcion=alg_errores.inversion)
print("Fragmentos con inversiones: \n" + str(fragmentos))

fragmentos = alg_errores.aplicar_quimeras(porcentaje=50)
print("Fragmentos con quimeras: \n" + str(fragmentos))

# ----------------------------------------------------------------------------------------------------------------------
