import random
import math
import numpy as np
from claseListaContenido import ListaSecuecial

class TablaHash:
    __arreglo = None
    __tamanio = None
    __cant_listas = None

    def __init__(self, tamanio):
        tamanio = math.floor(tamanio/20)
        while not self.es_primo(tamanio):
            tamanio+=1
        self.__tamanio = tamanio
        self.__arreglo = np.empty(tamanio, dtype=ListaSecuecial)
        self.__cant_listas = 0
    
    def es_primo(self, numero):
        band = True
        n = 2
        while band and n < numero:
            if numero%n == 0:
                band = False
            else:
                n+=1
        return band
    
        
    def getDireccion(self, clave):
        clave = str(clave)
        lista = [str(a) for a in clave]
        n1 = lista[0]+lista[1]+lista[2]+lista[3]
        n2 = lista[4]+lista[5]
        direccion = int(n1)+int(n2)
        direccion = (direccion%self.__tamanio)#se aplica doble hashing
        return direccion

    def insertar(self, clave):
        dir = self.getDireccion(clave)
        if self.__arreglo[dir] == None:
            self.__cant_listas+=1
            nueva_lista = ListaSecuecial(self.__cant_listas)
            nueva_lista.insertar(clave)
            self.__arreglo[dir] = nueva_lista
        elif self.__arreglo[dir].buscar(clave) != None:
            print('ERROR: Elemento ya existente!')
        else:
            self.__arreglo[dir].insertar(clave)
    
    def buscar(self, clave):
        dir = self.getDireccion(clave)
        if self.__arreglo[dir] == None:
            print('ERROR: Elemento no existente!')
        else:
            if self.__arreglo[dir].buscar() != None:
                print('Elemento encontrado!')
    
    def mostrar_longuitudes(self):
        for i in range(self.__tamanio):
            if self.__arreglo[i] is not None:
                print('Longuitud de la lista {}: {}'.format(self.__arreglo[i].getNumLista(),self.__arreglo[i].getLonguitudLista()))
    def getPromedio(self):
        total=0
        for i in range(self.__tamanio):
            if self.__arreglo[i] is not None:
                total+=self.__arreglo[i].getLonguitudLista()
        total=math.floor(total/self.__cant_listas)
        return total

    def getExceso(self):
        prom = self.getPromedio()
        count = 0
        for i in range(self.__tamanio):
            if self.__arreglo[i] is not None:
                if self.__arreglo[i].getLonguitudLista() > prom and self.__arreglo[i].getLonguitudLista() <= prom+3:
                    count+=1
        return count
    
    def getDefecto(self):
        prom = self.getPromedio()
        count = 0
        for i in range(self.__tamanio):
            if self.__arreglo[i] is not None:
                if self.__arreglo[i].getLonguitudLista() >= prom-3 and self.__arreglo[i].getLonguitudLista() < prom:
                    count+=1
        return count
    
    def getCantListas(self):
        return self.__cant_listas