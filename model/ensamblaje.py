import numpy as np

def obtenerSubcadena(indF1, frag1, indF2, frag2):
    subCadena = ""
    while(indF1 < len(frag1) and indF2 < len(frag2)):
        if(frag1[indF1] == frag2[indF2]):
            subCadena+=frag1[indF1]
            indF1 += 1
            indF2 += 1
        else:
            subCadena = ""
            break
    return subCadena

def obtenerPesos(frag1,frag2):  #Obtiene el peso que hay entre dos palabras
    indiceF1 = len(frag1)-1
    indiceF2 = 0
    peso = 0
    while indiceF1 >= 0 and indiceF2 < len(frag2):
        subcadena = obtenerSubcadena(indiceF1, frag1, 0, frag2)
        if(subcadena!=""):
            peso=len(subcadena)
        indiceF1-=1
        indiceF2+=1
    return peso

def grafoOriginal(frags):
    grafo=[]
    indiceFrag1 = 0
    while indiceFrag1 < len(frags): #Escoge fragmento por fragmento
        indiceFrag2 = 0
        while indiceFrag2 < len(frags): #Escoge a cada uno de los fragmentoss con los que va a comparar
            peso=obtenerPesos(frags[indiceFrag1],frags[indiceFrag2])
            if(indiceFrag2!=indiceFrag1 and peso!=0):
                grafo.append([frags[indiceFrag1], frags[indiceFrag2],peso])
            indiceFrag2+=1
        indiceFrag1+=1
    return grafo

def grafoSimplificado(pesoMin, grafo):
    indice=0
    tamanno = len(grafo)
    while indice < tamanno:
        if (grafo[indice][2] < pesoMin):
            grafo.pop(indice)
            indice-=1
        tamanno = len(grafo)
        indice+=1
    return grafo
