from VISUAL.VistaMascota import Vistamascota
from Raza import Raza
from VISUAL.VistaMascota import Vistamascota
class ControllersMascota:
    def __init__(self):
        self.vista= Vistamascota.getEdad()
        self.modeloRaza= Raza(nombre="",especie="",estado=0)
    def conocerraza(self):
        return self.modeloRaza
    def calcularedad(self):
        edad = 2024 - Vistamascota.getEdad()
        return edad
    def modificar_estado(self):
        if Vistamascota.ModificarEstado() == True :
            if Raza.getEstado()== 0:
                Raza.setEstado(1)
                return "habilitado"
            elif Raza.getEstado()==1:
                Raza.setEstado(0)
                return "desabilitado"

