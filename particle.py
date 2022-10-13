from algorithms import euclidean_distance

class Particle:
    def __init__(self,id, ori_X=0, ori_Y=0, dest_X=0, dest_Y=0, speed=0, R=0, G=0, B=0):
        self.__id = id
        self.__origen_x = ori_X
        self.__origen_y = ori_Y
        self.__destino_x = dest_X
        self.__destino_y = dest_Y
        self.__velocidad = speed
        self.__red = R
        self.__green = G
        self.__blue = B
        self.__distancia = euclidean_distance(ori_X, ori_Y, dest_X, dest_Y)
    
    def __str__(self) -> str:
        return(
            '\nID: ' + str(self.__id) +
            '\nOrigen X: ' + str(self.__origen_x) +
            '\nOrigen Y: ' + str(self.__origen_y) + 
            '\nDestino X: ' + str(self.__destino_x) +
            '\nDestino Y: ' + str(self.__destino_y) +
            '\nVelocidad: ' + str(self.__velocidad) +
            '\nRojo: ' + str(self.__red) +
            '\nVerde: ' + str(self.__green) +
            '\nAzul: ' + str(self.__blue) +
            '\nDistancia: ' + str(self.__distancia) +
            '\n'
        )