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
        return self.__promedio < otro.getPromedio()

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
    
    #Metodo para ordenar por promedios
    def ordenar_por_promedio(self):
        self.__alumnos.sort()   #sort() ordena de menor a mayor por defecto
    
    #Metodo para hallar el promedio de promedios del vector alumnos
    def promedio_grupo(self):
        if not self.__alumnos:  #verifica si vector esta vacio
            return 0    #en ese caso devuelve 0 para evitar dividir entre 0
        #se obtiene el promedio de cada alumno mediante un "for", se suma, y se divide entre
        #la longitud del vector. Devuelve el promedio de promedios
        return sum(alumno.getPromedio() for alumno in self.__alumnos) / len(self.__alumnos)
    
    #Metodo para retornar mejor promedio
    def mejor_promedio(self):
        if not self.__alumnos:  #Verifica si vector esta vacio
            return None #Retorna None (ninguno)
        #Escoge el primer objeto de vector como partida para operar
        mejor_promedio = self.__alumnos[0]  
        for alumno in self.__alumnos[1:]:   #recorre vector de alumnos
            #si el promedio de objeto es mayor al mejor_promedio hasta ahora
            if alumno.getPromedio() > mejor_promedio.getPromedio():
                mejor_promedio = alumno #asigna nuevo objeto como mejor promedio
        return mejor_promedio #Rettorna al objeto Alumno con mejor promedio