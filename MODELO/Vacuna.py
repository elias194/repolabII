class Vacuna:
    def __init__(self,nombre="",registro="",tipovacuna="",estado=0,precio=0.0):
        self.nombre=nombre
        self.registro=registro
        self.tipovacuna=tipovacuna
        self.estado=estado
        self.precio=precio

    def getEstado(self):
        return self.estado
    def getRegistro(self):
        return self.registro
    def setEstado(self):
        return self.estado
    def setRegistro(self):
        return self.registro

    def Modificar_Estado(self):
        pass
    def Modificar_Registro(self):
        pass
    def Eliminar_Vacuna(self):
        pass

    def __str__(self):
        return f'nombre : {self.nombre} \n registro: {self.registro} \n vacuna : {self.tipovacuna} \n estado: {self.estado} \n precio: {self.precio}  '

    def __repr__(self):
        return f'nombre : {self.nombre} \n registro: {self.registro} \n vacuna : {self.tipovacuna} \n estado: {self.estado} \n precio: {self.precio}  '

