# from nombrearchivo (sin .py) import cosaAimportar 

from persona import Persona

if __name__ == '__main__':
    persona = Persona () # --> para importar clases
    print (persona)
    print (persona.__str__())

    persona = Persona ()
    print (persona)          # 2 direcciones de memoria distintas

    persona = Persona ()
    print (persona)    