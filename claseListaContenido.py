import numpy as np
from claseNodo import Nodo

class ListaSecuecial:
    __maximo = None
    __ult = None
    __lista = None
    __numeroLista = None
    
    def __init__(self, numero, maximo = 20):
        self.__lista = np.empty(maximo,dtype=int)
        self.__maximo = maximo
        self.__ult = 0
        self.__numeroLista = numero
    
    def getNumLista(self):
        return self.__numeroLista
    def getLonguitudLista(self):
        return self.__ult
    
    def lleno(self):
        return (self.__ult == self.__maximo-1)
    
    def vacio(self):
        return (self.__ult == 0)
            
    def shift(self,i):
        j = self.__ult
        while j > i:
            self.__lista[j] = self.__lista[j-1]
            j-=1
            
    def suprimir(self,elemento):
        assert isinstance(elemento, int)
        if not self.vacio():
            i = 0
            encontro = False
            while not encontro and i <= self.__ult-1:
                if self.recuperar(i) == elemento:
                    self.rshift(i)
                    self.__ult-=1
                    encontro = True
                else:
                    i += 1
            if not encontro:
                print('ERROR: Elemento no encontrado')
               
                    
    def rshift(self,i):
        while i <= self.__ult:
            self.__lista[i] = self.__lista[i+1]
            i+=1

    def insertar(self,elemento):
        assert isinstance(elemento, int)
        if not self.lleno():
            i = 0
            if self.vacio():
                self.__lista[i] = elemento
                self.__ult+=1
            else:
                encontro = False
                while not encontro and i<=self.__ult-1:
                    if self.recuperar(i) < elemento:
                        self.shift(i)
                        self.__lista[i] = elemento
                        self.__ult+=1
                        encontro = True
                    else:
                        i+=1
                
                if not encontro:#Si el elemento debe ir al final..
                    self.__lista[i] = elemento
                    self.__ult+=1           
        else:
            print('ERROR: no hay espacio')
    
    def recorrer(self):
        if not self.vacio():
            for i in range(self.__ult):
                print(self.__lista[i])
        else:
            print('ERROR: Lista vacia!')
    
    def recuperar(self, p):
        val = None
        if not self.vacio():
            if p >= 0 and p <= self.__ult-1:
                    val = self.__lista[p]
        return val

    def buscar(self, elemento):
        encontro = False
        i = 0
        val = None
        while not encontro and i<=self.__ult-1:
            if self.__lista[i] == elemento:
                encontro = True
                val = i
            else:
                i+=1
        return val
        
    def primer_elemento(self):
        val = None
        if not self.vacio():
            val = self.__lista[0]
        else:
            print('ERROR: Lista vacia!')
        return val
    
    def ultimo_elemento(self):
        val = None
        if not self.vacio():
            val = self.__lista[ult-1]
        else:
            print('ERROR: Lista vacia!')
        return val
    
    def siguiente(self, p):
        if not self.vacio():
            val = None
            if p-1 >= 0 and p-1 < self.__ult-1:

                val = p+1
            else:
                print('ERROR: No hay mas elementos despues de la posicion ingresada!')
        else:
            print('ERROR: Lista vacia!')