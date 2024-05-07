#Creación de atributos de la clase Alumno
class Alumno:
    #Se indican atributos privados usando doble subguion
    __nombre = 'Desconocido'       #Nombre del alumno
    __edad = 16                 #Edad del alumno
    __promedio = 0.0            #Promedio del alumno
    
    #Creacion de getters y setters
    def getNombre(self):        #Self es un parámetro implicito
        return self.__nombre   #Se usa self para referirse a si mismo.
    def getEdad(self):
        return self.__edad
    def getPromedio(self):
        return self.__promedio
    def setNombre(self, n):  #Se envian 02 parametros (implicto/explicito)
        self.__nombre = n
    def setEdad(self, n):
        self.__edad = n
    def setPromedio(self, n):
        self.__promedio = n

#Creación de la clase Grupo
class Grupo:
    #Se indican atributos privados usando doble subguion
    __alumnos = []   #Vector de alumnos para objetos de la clase Alumno
    __cantidad = 0   #Cantidad para el grupo de alumnos