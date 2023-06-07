class cliente:
    
    def __init__(self,altura, naciolalidad, edad, nombre, direccion):
        self.altura = altura
        self.nacionalidad= naciolalidad
        self.edad = edad 
        self.nombre= nombre
        self.direccion= direccion
    def __str__(self) :
        return f"el cliente se llama {self.nombre}, tiene nacionalidad { self.nacionalidad }"
    def cambiar_direccion(self):
        calle = input("¿ cual es la calle?: ")
        altura = input(" ¿ cual es la altura?: ")
        ciudad = input(" ¿cual es la ciudad ?:  ")
        direccion= f"{calle}  {altura}, {ciudad}"
        self.direccion= direccion
        

cliente1 = cliente("1,85", "venezolana", "23", "jose","C.A.B.A, palermo")       
print(cliente1.altura)
print(cliente1.edad)
print(cliente1.nacionalidad)
print(cliente1.nombre)
print(cliente1.direccion)




