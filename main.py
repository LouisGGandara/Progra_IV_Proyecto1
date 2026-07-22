# Entonces veremos qué hace cada quién
# Ahí vamos viendo, pero pues, tiene que estar listo para el lunes, o a más tardar martes
class Persona:
    def __init__(self, Nombre, DPI, Correo):
        self.Nombre = Nombre
        self.DPI = DPI
        self.Correo = Correo
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre):
        if len(Nombre) >= 3:
            self.__Nombre = Nombre
        else:
            print("Nombre incorrecto")
    @property
    def DPI(self):
        return self.__DPI
    @DPI.setter
    def DPI(self, DPI):
        if len(DPI)==13:
            self.__DPI = DPI
        else:
            print("DPI incorrecto")
    @property
    def Correo(self):
        return self.__Correo
    @Correo.setter
    def Correo(self, Correo):
        if '@' in Correo:
            self.__Correo = Correo
        else:
            print("Correo incorrecto")
    def MostrarInformacion(self):
        print("Nombre:", self.Nombre)
        print("DPI:", self.DPI)
        print("Correo:", self.Correo)
class Usuario(Persona):
    def __init__(self, Nombre, DPI, Correo, Direccion):
        super().__init__(Nombre,DPI,Correo)
        self.Direccion = Direccion
    @property
    def Direccion(self):
        return self.__Direccion
    @Direccion.setter
    def Direccion(self, Direccion):
        self.__Direccion = Direccion
    def MostrarInformacion(self):
        print("Nombre:", self.Nombre)
        print("DPI:", self.DPI)
        print("Correo:", self.Correo)
        print("Direccion:", self.Direccion)
class Trabajador(Persona):
    def __init__(self, Nombre, DPI, Correo, Tipo, Resenas):
        super().__init__(Nombre,DPI,Correo)
        self.Tipo = Tipo
        self.Resenas = Resenas
    @property
    def Tipo(self):
        return self.__Tipo
    @Tipo.setter
    def Tipo(self, Tipo):
        if len(Tipo)>=3:
            self.__Tipo = Tipo
        else:
            print("Tipo de trabajo incorrecto")
    @property
    def Resenas(self):
        return self.__Resenas
    @Resenas.setter
    def Resenas(self, Resenas):
        self.__Resenas = Resenas
    def MostrarInformacion(self):
        print("Nombre:", self.Nombre)
        print("DPI:", self.DPI)
        print("Correo:", self.Correo)
        print("Tipo de trabajo:", self.Tipo)
        print("Reseñas:", self.Resenas)
