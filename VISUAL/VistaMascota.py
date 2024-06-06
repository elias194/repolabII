class Vistamascota:
    def ModificarEstado(self):
        pregunta=input("MODIFICAR ESTADO: SI/NO")
        pregunta=pregunta.lower()
        if pregunta=="si":
            return True
        return False

