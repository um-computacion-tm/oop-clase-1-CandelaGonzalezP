#un parametro se convierte de obligatorio a optativo cuando le pongo un valor por defecto --> ej: def (self, nombre = 'pepe')

class Persona:

    def __init__ (self, nombre: str = 'john', apellido: str ='doe', dni: int = 123456):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__dni__ = dni
    
    def __str__(self):                  #para mostrar datos de la persona
        return f'Mis datos son nombre = {self.__nombre__} apellido = {self.__apellido__} documento = {self.__dni__}'

    
