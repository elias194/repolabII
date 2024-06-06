class Mascota:
<<<<<<< HEAD
    def __init__(self,estado="",nombre="",raza="",fecha_nacimiento="",propietario="",fichamedica=""):
=======
    def __init__(self,estado="",nombre="",raza="",fecha_nacimiento="",propietario="",codigo_propietario=""):
>>>>>>> parent of 57af4cf (borre)
        self.estado = estado
        self.nombre = nombre
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        self.propietario = propietario
<<<<<<< HEAD
        self.fichamedica=fichamedica
=======
        self.codigo_propietario = codigo_propietario
>>>>>>> parent of 57af4cf (borre)

    def getEstado(self):
        return self.estado
    def setEstado(self):
        return self.estado
    def __str__(self):
        return self.estado, self.nombre, self.raza, self.fecha_nacimiento, self.propietario,self.codigo_propietario
    def __repr__(self):
        return self.estado, self.nombre, self.raza, self.fecha_nacimiento, self.propietario,self.codigo_propietario