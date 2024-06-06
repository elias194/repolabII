from MODELO.Raza import Raza
from VISUAL.VistaMascota import Vistamascota
from MODELO.Mascota import Mascota

class ControllersMascota:
    def __init__(self):
        self.vista= Vistamascota()
        self.modeloRaza= Raza()
        self.modeloMascota= Mascota()
    def conocerraza(self):
        return self.modeloRaza

    def modificar_estado(self):
        if Vistamascota.ModificarEstado() == True :
            if Raza.getEstado()== 0:
                Raza.setEstado(1)
                return "habilitado"
            elif Raza.getEstado()==1:
                Raza.setEstado(0)
                return "desabilitado"

    def asignar_raza(self):
        pass
    def modificar_mascota(self):
        pass
    def asignarespecie(self):
        pass
    def pedirnombre(self):
        pass
    def asigarpropietario(self):
        pass
