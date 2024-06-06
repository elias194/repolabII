from MODELO.Raza import Raza
from VISUAL.VistaMascota import Vistamascota
<<<<<<< HEAD
from MODELO.Mascota import Mascota

class ControllersMascota:
    def __init__(self):
        self.vista= Vistamascota()
        self.modeloRaza= Raza()
        self.modeloMascota= Mascota()
    def conocerraza(self):
        return self.modeloRaza

=======
class ControllersMascota:
    def __init__(self):
        self.vista= Vistamascota.getEdad()
        self.modeloRaza= Raza(nombre="",especie="",estado=0)
    def conocerraza(self):
        return self.modeloRaza
    def calcularedad(self):
        edad = 2024 - Vistamascota.getEdad()
        return edad
>>>>>>> parent of 57af4cf (borre)
    def modificar_estado(self):
        if Vistamascota.ModificarEstado() == True :
            if Raza.getEstado()== 0:
                Raza.setEstado(1)
                return "habilitado"
            elif Raza.getEstado()==1:
                Raza.setEstado(0)
                return "desabilitado"

<<<<<<< HEAD
    def asignar_raza(self):
        pass
    def modificar_mascota(self):
        pass
    def asignarespecie(self):
        pass
    def pedir_nombre(self):
        nombre= Vistamascota.NombreMascota()
    def asigarpropietario(self):
        pass
=======
>>>>>>> parent of 57af4cf (borre)
