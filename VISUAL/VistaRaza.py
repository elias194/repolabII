from CONTROLLERS.ControllersRaza import ControllersRaza
class VistaRaza:
    def ModificarEstado(self):
        pregunta=input("MODIFICAR ESTADO: SI/NO")
        pregunta=pregunta.lower()
        if pregunta=="si":
            return True
        return False
    def MostrarEstado(self):
        if ControllersRaza.getEstado() == 0 :
            print("desabilitado")
        elif ControllersRaza.getEstado()==1:
            print("habilitado")
