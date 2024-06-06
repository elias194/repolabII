class Mascota:
    def __init__(self,estado="",nombre="",raza="",fecha_nacimiento="",propietario="",codigo_propietario="", fichamedica=""):
        self.estado = estado
        self.nombre = nombre
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        self.propietario = propietario

        self.fichamedica=fichamedica

        self.codigo_propietario = codigo_propietario


    def getEstado(self):
        return self.estado
    def setEstado(self):
        return self.estado
    def __str__(self):
        return self.estado, self.nombre, self.raza, self.fecha_nacimiento, self.propietario,self.codigo_propietario
    def __repr__(self):
        return self.estado, self.nombre, self.raza, self.fecha_nacimiento, self.propietario,self.codigo_propietario