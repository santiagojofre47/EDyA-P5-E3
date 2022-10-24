import random
from claseTablaHash import TablaHash

if __name__ == '__main__':
    obj = TablaHash(1000)
    for i in range(1000):
        obj.insertar(random.randint(100000,999999))
    obj.mostrar_longuitudes()
    print('Cantidad de listas que superan el promedio de longuitud de listas por tres unidades: {}'.format(obj.getExceso()))
    print('Cantidad de listas que estan debajo el promedio de longuitud de listas por tres unidades: {}'.format(obj.getDefecto()))