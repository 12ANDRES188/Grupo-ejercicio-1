"""Crear una clase Banco con un atributo saldo. Añadir métodos para
depositar y retirar cierta cantidad. """

class Banco():
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar (self, deposito):#metodo depositar
        self.saldo += deposito
        print(f"He depositado {deposito} saldo actual {self.saldo}")
        
    
    def retirar (self, retiro):
        if retiro <= self.saldo:
            self.saldo -= retiro
            print(f"He retirado {retiro} saldo actual {self.saldo} ")
        else:
            print("fondo insuficiente")
            
        
Banco1 = Banco(9000)

print(f"tengo almacenado {Banco1.saldo}")
Banco1.retirar(2000)
Banco1.depositar(1000)