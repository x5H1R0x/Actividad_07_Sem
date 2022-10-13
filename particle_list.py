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