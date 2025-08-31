"""Crear una clase abstracta Animal que tenga un método 
hacer_sonido. Luego, crear clases Perro y Gato que hereden de 
Animal e implementen hacer_sonido.  """

from abc import ABC, abstractmethod

class Animal (ABC):#clase abstrata
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro (Animal):
    def hacer_sonido(self):
        print("GUAUUUU")
        
class Gato (Animal):
    def hacer_sonido(self):
        print("MIAUUUU")
        

PERRO1 = Perro()
PERRO1.hacer_sonido()


GATO1 = Gato()
GATO1.hacer_sonido()
