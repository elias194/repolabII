class Diagnostico:
    def __init__(self,estado=0 , descripcion=""):
        self.estado=estado
        self.descripcion=descripcion

    def getEstado(self):
        return self.estado
    def getDescripcion(self):
        return self.descripcion
    def setEstado(self):
        return self.estado
    def Modificar_Estado(self):
        pass
    def Modificar_Diagnostico(self):
        pass
    def Eliminar_Diagnostico(self):
        pass

    def __str__(self):
        return f'estado: {self.estado} \n descripcion: {self.descripcion}  '

    def __repr__(self):
        return f'estado: {self.estado} \n descripcion: {self.descripcion}  '

