class Mascota:
    def __init__(self,estado="",nombre="",raza="",fecha_nacimiento="",propietario="",codigo_propietario=""):
        self.estado = estado
        self.nombre = nombre
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        self.propietario = propietario
        self.codigo_propietario = codigo_propietario

    def conocerraza(self):
        return self.raza()

    def calcularedad(self):
        pass

    def modificar_estado(self):
        pass

    def __str__(self):
        return self.estado, self.nombre, self.raza, self.fecha_nacimiento, self.propietario,self.codigo_propietario