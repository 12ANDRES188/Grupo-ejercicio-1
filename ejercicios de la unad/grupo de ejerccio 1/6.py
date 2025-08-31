"""Crea una clase Producto que tenga los atributos nombre, precio, 
stock, y descuento (inicialmente en 0). Agrega métodos 
aplicar_descuento(porcentaje) que ajuste el precio en función del 
porcentaje de descuento dado, y actualizar_stock(cantidad) que 
modifique el stock según la cantidad (positiva o negativa). 
También, crea un método descripcion que devuelva una cadena"""


class Producto ():
    def __init__(self, nombre , precio , stock):
        self.nombre = nombre
        self.precio = precio 
        self.stock= stock
        self.descuento = 0
        
    def aplicar_descuento(self, porcentaje):
        self.descuento = porcentaje
        descuento_del_valor =  self.precio * (porcentaje/ 100)
        self.precio -=descuento_del_valor
        print(f"se aplica un {porcentaje}%  de descuento . nuevo precio {self.precio}")
        
    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"stock actualizado cantidad nueva {self.stock}")
    
    def descripcion (self):
        return f" producto: {self.nombre}, precio {self.precio}, stock {self.stock}, descuento {self.descuento}"
    

producto1 = Producto("Arroz", 3000 , 10)

print(producto1.descripcion())

producto1.aplicar_descuento(10)

