"""Crear una clase llamada Persona con atributos nombre y edad, e
inicialízalos con valores predeterminados."""

class Persona ():
    def __init__(self, nombre = "andres" , edad= 33):
        self.nombre = nombre
        self.edad= edad
        

persona0= Persona()
print(f"Nombre {persona0.nombre}, Edad  {persona0.edad}")

persona1= Persona("carlos" , 20)
print(f"Nombre {persona1.nombre}, Edad  {persona1.edad}")
