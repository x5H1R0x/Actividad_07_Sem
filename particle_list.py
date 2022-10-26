import json
from particle import Particle

class Particle_List:
    def __init__(self):
        self.__Particles = []

    def addToEnd(self, part:Particle):
        self.__Particles.append(part)

    def addFirst(self, part:Particle):
        self.__Particles.insert(0, part)

    def showAll(self):
        for part in self.__Particles:
            print(part)
    
    def __str__(self):
        return "".join(
            str(particle) for particle in self.__Particles
        )

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particle.to_dict() for particle in self.__Particles]
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0


    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__Particles =[Particle(**part) for part in lista]
                
            return 1
        except:
            return 0
