class Estudiante:
    __id = ''
    __nombre = ''
    __correo = ''
    __contra = None

    def __init__(self, nombre, correo, contra):
        self.__nombre = nombre
        self.__correo = correo
        self.__contra = contra

    def getNombre(self):
        return self.__nombre

    def getCorreo(self):
        return self.__correo

    def getContra(self):
        return self.__contra