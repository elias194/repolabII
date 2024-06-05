class Persona:
    def __init__(self,nombre="",direccion="",mail="",telefono=0):
        self.nombre=nombre
        self.direccion=direccion
        self.mail=mail
        self.telefono=telefono
    def getNombre(self):
        return self.nombre
    def getDireccion(self):
        return self.direccion
    def getMail(self):
        return self.mail
    def getTelefono(self):
        return self.telefono


    def __str__(self):
        return f'nombre: {self.nombre} \n direccion: {self.direccion } \n mail: {self.mail} \n telefono : {self.telefono} '
    def __repr__(self):
        return f'nombre: {self.nombre} \n direccion: {self.direccion } \n mail: {self.mail} \n telefono : {self.telefono} '

def pedir_datos_Persona():
    pass