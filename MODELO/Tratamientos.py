class Tratamientos:
    def __init__(self,estado=0):
        self.estado=estado
        self.registro_tratamientos=[]

    def Modificar_tratamientos(self):
        pass
    def Eliminar_tratamientos(self):
        pass

    def __str__(self):
        return f'estado: {self.estado} \n registros: {self.registro_tratamientos}  '

    def __repr__(self):
        return f'estado: {self.estado} \n registros: {self.registro_tratamientos}  '
