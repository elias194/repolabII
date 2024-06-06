class Veterinario(Persona):
    def __init__(self,nombre,direccion,mail,telefono,nummatricula,especializacion):
        super().__init__(nombre,direccion,mail,telefono)
        self.nummatricula = nummatricula
        self.especializacion = especializacion

    def mostrarveterinario(self):
        return "veterinario:",self.nombre,"direccion:",self.direccion,"mail:",self.mail,"telefono:",self.telefono