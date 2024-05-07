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
    #Metodo constructor de la clase Grupo
    def __init__(self, cantidad):
        #Se indican atributos privados usando doble subguion
        self.__alumnos = [] #Vector de alumnos para objetos de la clase Alumno
        self.__cantidad = cantidad #Cantidad para el grupo de alumnos
    
    #Metodo que devuelve estado del objeto Grupo
    def __str__(self):
        alumnos_str = "" #representaciones en string de cada alumno en el grupo
        for alumno in self.__alumnos:   #iteracion sobre lista de alumnos
            alumnos_str += str(alumno) + "\n" #se agrega en una nueva linea de alunos_str
        return f"Grupo:\n{alumnos_str}" #Devuelve el valor de alumnos_str en string
    
    #Metodo para agregar alumnos al vector alumno
    def agregar_alumno(self, nombre, edad, promedio): #Envio de parametros de alumno
        if len(self.__alumnos) < self.__cantidad:   #vector actual debe ser menor a cantidad
            alumno = Alumno(nombre, edad, promedio) #se crea instancia de Alumno
            self.__alumnos.append(alumno)   #se agrega a vector alumnos
        else:   #si vector ya esta lleno, devuelve respectivo mensaje
            print("No se puede agregar más alumnos, el grupo está completo.")