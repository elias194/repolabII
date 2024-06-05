class Raza:
    def __init__(self,nombre="",especie="",estado=0):
        self.nombre=nombre
        self.especie=especie
        self.estado=estado

    def getNombre(self):
        return self.nombre
    def getEspecie(self):
        return self.especie
    def getEstado(self):
        return self.estado
    def setNombre(self):
        return self.nombre
    def setEspecie(self):
        return self.especie
    def setEstado(self):
        return self.estado

    def estado_raza(self):
        pass

    def Modificar_estado(self):
        pass

    def eliminar_raza(self):
        pass

    def mostrar_raza(self):
        pass

    def __str__(self):
        return f'nombre: {self.nombre} \n Especie: {self.especie} \n Estado: {self.estado} '

    def __repr__(self):
        return f'nombre: {self.nombre} \n Especie: {self.especie} \n Estado: {self.estado}'

