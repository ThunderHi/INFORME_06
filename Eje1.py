#Creación de atributos de la clase Alumno
class Alumno:
    #Método constructor
    def __init__(self, nombre, edad, promedio):
        #Se indican atributos privados usando doble subguion
        self.__nombre = nombre  #Nombre del alumno
        self.__edad = edad      #Edad del alumno
        self.__promedio = promedio  #Promedio del alumno
    
    #Creacion de getters y setters
    def getNombre(self):        #Self es un parámetro implicito
        return self.__nombre   #Se usa self para referirse a si mismo.
    def getEdad(self):
        return self.__edad
    def getPromedio(self):
        return self.__promedio
    
    #Creacion de metodo que devolverá estado del objeto
    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Promedio: {self.__promedio}"
    
    #Creacion de metodo que compara promedio entre objetos
    def __lt__(self, otro):
        return self.__promedio < otro.get_promedio()

#Creación de la clase Grupo
class Grupo:
    def __init__(self, cantidad):
        #Se indican atributos privados usando doble subguion
        self.__alumnos = [] #Vector de alumnos para objetos de la clase Alumno
        self.__cantidad = cantidad #Cantidad para el grupo de alumnos