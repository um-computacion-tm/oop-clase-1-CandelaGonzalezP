# Objetos != programacion funcional
# permite modelar la realidad, definir clases
# los objetos tienen estados porque tienen atributos
# self__atributo__ = 0 SIEMPRE con --a--
# PARADIGMA DE PROGRAMACION: conjunto de reglas de programacion
# TIOBE index: mide el uso de los lenguajes de programacion
# referencia = objeto


class Profesor:              # --> clases (1)

    def __init__(self, el_nombre, el_email):      #constructor (_init_) = funcion que se ejecuta cuando se crea el objeto de la clase, recibe parametros (1- yo mismo, 2- atributo)
        self.__nombre__ = el_nombre
        self.__email__ = el_email

    def dame_tu_nombre(self):               #devuelve valores que estan arriba
        return self.__nombre__

profe_elio = Profesor("Elio", "elio@gmail.com")            # --> objetos (n)
profe_gabi = Profesor("Gabriel", "gabriel@um.edu.ar")      # profe_gabi --> es la referencia,no el objeto

"""print(profe_elio.dame_tu_nombre())
print(profe_gabi.dame_tu_nombre())"""                 #metodo dentro de la clase profesor que devuelve el nombre (en este caso)



class Alumno:

    def __init__(self, el_nombre_del_alumno):        #constructor
        self.__nombre__ = el_nombre_del_alumno
        self.__inasistencias__ = 0          #cuando arranca todos van a tener 0 inasistencias
        self.__dieta__ = ""
        self.__mentor__ = None

    def mentoria(self, profesor):           
        self.__mentor__ = profesor          # --> objeto que esta referenciado a otro objeto

    def falta(self):
        self.__inasistencias__ += 1        #cada vez que la persona falta se le suma una inasistencia al alumno

    def elegir_dieta_especial(self, la_dieta):
        self.__dieta__ = la_dieta

    def es_vegano(self):
        self.__dieta__ = "vegano"

    def esta_libre(self):
        if self.__inasistencias__ >= 5:       #OJO con el SELF, porque sino es una variable comun
            return "ESTA LIBRE"
        else:
            return "OK"



alumno_juan = Alumno("Juancito")
alumno_Maria = Alumno("Maria")


alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
print(alumno_juan.esta_libre())
alumno_juan.falta()
print(alumno_juan.esta_libre())


alumno_Maria.elegir_dieta_especial("vegetariana")
print(alumno_Maria.__dieta__)
alumno_juan.es_vegano()
print(alumno_juan.__dieta__)


alumno_juan.mentoria(profe_elio)      # --> relaciono clases
print(alumno_juan.__mentor__.__nombre__)         # --> el .nombre es importante porque es el atributo que necesito del profesor en este caso

# TODOS LOS ATRIBUTOS VAN CON __ atributo__
#variables_nombres (snake)       ClasesNombres (primera mayuscula)