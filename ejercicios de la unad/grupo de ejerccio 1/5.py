"""Crea una clase Rectangulo que tenga dos atributos, ancho y alto. 
Incluye un método area que calcule y devuelva el área del 
rectángulo, y un método perimetro que devuelva el perímetro. 
Crea una instancia de Rectangulo y muestra su área y perímetro."""

class Rectangulo():
    def __init__(self, ancho, alto):
        self.ancho = ancho 
        self.alto = alto
        
    def area (self):
        #Area = ancho * alto
        return self.ancho * self.alto
    
    def perimetro (self):
        return 2 * (self.ancho + self.alto)
    

MiRectangulo = Rectangulo (7,3)

print("Area del rectangulo", MiRectangulo.area())

print("perimetro del rectangulo", MiRectangulo.perimetro())
