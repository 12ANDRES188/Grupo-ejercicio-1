"""Encapsulamiento y métodos estáticos: Crear una clase Usuario con 
un atributo privado _password. Añadir un método para cambiar la 
contraseña solo si se ingresa correctamente la actual. """

class Usuario:
    def __init__(self,  password):# el constructor
        self._password =  password # el guion bajo indica que es privado 
        
    def cambiar_contraseña (self,original): # metodo 
        #primero verificamos si la contrasñea actual coincide on la ingresada
        if self._password != original:
            print("no se puede cambiar la contra")
        
        else:
            #si coincide pedimos nueva contra
            nueva = input("ingrese nueva contra")
            self._password = nueva
            print("contrasñea cambiada eficazmente")
        
        
usuario1 = Usuario("Andres")

usuario1.cambiar_contraseña("Andres")
