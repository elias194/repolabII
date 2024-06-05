from VISUAL.VistaRaza import VistaRaza
from MODELO.Raza import Raza
class ControllersRaza:
    def __init__(self):

    def Modificar_estado(self):
        if VistaRaza.ModificarEstado() == True :
            if Raza.getEstado()== 0:
                Raza.setEstado(1)
                return "habilitado"
            elif Raza.getEstado()==1:
                Raza.setEstado(0)
                return "desabilitado"


    def getEstado(self):
        return Raza.getEstado()
