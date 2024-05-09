#Creación de atributos de la clase Alumno
class Alumno:
    #Método constructor
    def __init__(self, nombre, edad, promedio):
        #Se indican atributos privados usando doble subguion
        self.__nombre = nombre  #Nombre del alumno
        self.__edad = edad      #Edad del alumno
        self.__promedio = promedio  #Promedio del alumno
    
    #Creación de getters
    def getNombre(self):        #self es un parámetro implícito
        return self.__nombre   #se usa self para referirse a si mismo.
    def getEdad(self):
        return self.__edad
    def getPromedio(self):
        return self.__promedio
    
    #Creación de método que devolverá estado del objeto en string
    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Promedio: {self.__promedio}"
    
    #Creacion de método que compara promedio entre objetos y devuelve valor booleano
    def __lt__(self, otro):
        return self.__promedio < otro.getPromedio()

#Creación de la clase Grupo
class Grupo:
    #Método constructor de la clase Grupo
    def __init__(self, cantidad):
        #Se indican atributos privados usando doble subguion
        self.__alumnos = [] #Vector de alumnos para objetos de la clase Alumno
        self.__cantidad = cantidad #Cantidad para el grupo de alumnos
    
    #Método que devuelve estado del objeto Grupo
    def __str__(self):
        alumnos_str = "" #representaciones en string de cada objeto alumno en el grupo
        for alumno in self.__alumnos:   #iteración sobre lista de alumnos
            alumnos_str += str(alumno) + "\n" #se agrega en una nueva linea de alumnos_str
        return f"Grupo:\n{alumnos_str}" #devuelve el valor de alumnos_str
    
    #Método para agregar alumnos al vector alumno
    def agregar_alumno(self, alumno): #se envía objeto de clase Alumno como parámetro
        if len(self.__alumnos) < self.__cantidad:   #se compara tamaño de vector y cantidad
            self.__alumnos.append(alumno)   #se añade a vector alumno
        else:
            print("No se puede agregar más alumnos, el grupo está completo.")
    #Método para ordenar por promedios
    def ordenar_por_promedio(self):     #se aplica ordenamiento por método de la burbuja
        for i in range(1,self.__cantidad):     #for que recorre todo vector alumno
            for j in range(0,self.__cantidad-1):    #for para comparar entre alumnos
                if self.__alumnos[i].getPromedio() < self.__alumnos[j].getPromedio(): 
                    temp = self.__alumnos[i]    #se asigna alumno[i] a temporal
                    self.__alumnos[i] = self.__alumnos[j] #se asigna [j] en [i]
                    self.__alumnos[j] = temp #se devuelve alumno[i] en alumno [j]
    
    #Método para hallar el promedio de promedios del vector alumnos
    def promedio_grupo(self):
        if not self.__alumnos:  #verifica si vector esta vacío
            return 0    #en ese caso devuelve 0 para evitar dividir entre 0
        else:
            suma=0  #se crea variable acumuladora
            for i in range(0,self.__cantidad):
                suma += self.__alumnos[i].getPromedio() #se acumulan promedios
            return round(suma/self.__cantidad,2) #se retorna valor redondeado maximo 2 decimales
    
    #Método para retornar mejor promedio
    def mejor_promedio(self):
        if not self.__alumnos:  #Verifica si vector esta vacío
            return None #Retorna None (ninguno)
        #Escoge el primer objeto de vector como partida para operar
        mejor_promedio = self.__alumnos[0]  
        for alumno in self.__alumnos[1:]:   #recorre vector de alumnos
            #si el promedio de objeto es mayor al mejor_promedio hasta ahora
            if alumno.getPromedio() > mejor_promedio.getPromedio():
                mejor_promedio = alumno #asigna nuevo objeto como mejor promedio
        return mejor_promedio #Retorna al objeto Alumno con mejor promedio
    
# Función principal del programa
if __name__ == "__main__":  # verifica si el nombre del módulo es "__main__"
    #Se crea objetos de la clase Alumno
    alumno1 = Alumno("Juan", 17, 16.5)
    alumno2 = Alumno("María", 18, 15.8)
    alumno3 = Alumno("Pedro", 20, 19.2)
    alumno4 = Alumno("Luisa", 17, 11.9)
    alumno5 = Alumno("Carlos", 19, 16.1)
    alumno6 = Alumno("Thunder", 19, 10)

    #Se crea objeto de la clase Grupo con capacidad para 5 alumnos
    grupo = Grupo(5)

    #Se crean objetos de Alumno y se asignan al al vector alumno de Grupo
    grupo.agregar_alumno(alumno1)
    grupo.agregar_alumno(alumno2)
    grupo.agregar_alumno(alumno3)
    grupo.agregar_alumno(alumno4)
    grupo.agregar_alumno(alumno5)
    
    #Muestra estado del objeto de Grupo mediante string
    print(grupo)

    #Muestra el promedio del vector de Alumno
    print(f"Promedio del grupo: {grupo.promedio_grupo()}")
    
    #Muestra el mejor promedio
    mejor_alumno = grupo.mejor_promedio()
    #Si el vector no esta vacio
    if mejor_alumno:
        print(f"Mejor promedio:\n{mejor_alumno}")
    #sino muestra que no hay alumnos
    else:
        print("No hay alumnos en el grupo.")
    
    #Muestra el vector alumno ordenado
    grupo.ordenar_por_promedio()
    print(grupo)    #Muestra el vector ordenado de mayor a menor
