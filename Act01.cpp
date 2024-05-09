#include <iostream>
#include <string>

using namespace std;

//Definición de la clase Estudiante
class Estudiante {
public:
    string nombre;
    int edad;
    int notas[3]; //Se indica que "notas" es un arreglo de enteros de longitud 3  
    double promedio;

    //Constructor para inicializar los datos
    Estudiante(string nombre, int edad, int nota1, int nota2, int nota3) {
        this->nombre = nombre; //Asigna el valor del parámetro `nombre` al atributo `nombre` del objeto
        this->edad = edad; //Asigna el valor del parámetro `edad` al atributo `edad` del objeto
        this->notas[0] = nota1; //Asigna el valor del parámetro `nota1` a la primera posición del arreglo `notas`
        this->notas[1] = nota2; //Asigna el valor del parámetro `nota2` a la segunda posición del arreglo `notas`
        this->notas[2] = nota3; //Asigna el valor del parámetro `nota3` a la tercera posición del arreglo `notas`
        this->promedio = calcularPromedio(); //Calcula y asigna el promedio de las notas al atributo `promedio` del objeto
    }

    //Función para calcular el promedio de las notas
    double calcularPromedio() { //Función que calcula el promedio de las notas del estudiante
        double suma = 0; //Variable local para almacenar la suma de las notas
        for (int i = 0; i < 3; i++) { //Recorre el arreglo de notas utilizando un bucle `for`
            suma += notas[i]; //Suma cada nota al valor de la variable `suma`
        }
        return suma / 3; //Calcula y devuelve el promedio dividiendo la suma de las notas por 3 (cantidad de notas)
    }
};

//Función para imprimir estudiantes con promedio mayor a cierta nota
void imprimirMayoresPromedio(Estudiante estudiantes[], int numEstudiantes, double notaMinima) { //Imprime los estudiantes con un promedio mayor a la nota mínima especificada
    for (int i = 0; i < numEstudiantes; i++) { //Recorre el arreglo de estudiantes utilizando un bucle `for`
        if (estudiantes[i].promedio > notaMinima) { //Compara el promedio del estudiante actual con la nota mínima
            cout<<estudiantes[i].nombre<<" - Promedio: "<<estudiantes[i].promedio<<endl; //Si el promedio es mayor, imprime el nombre y promedio del estudiante
        }
    }
}

int main() {
    //Creación de un arreglo de objetos Estudiante y llenado con información
    Estudiante estudiantes[] = {  //Arreglo de objetos `Estudiante` inicializado con datos de estudiantes
        Estudiante("Juan", 20, 85, 90, 88),
        Estudiante("Maria", 22, 78, 85, 90),
        Estudiante("Pedro", 21, 92, 88, 95),
        Estudiante("Luisa", 23, 80, 75, 82)
    };
    int numEstudiantes = sizeof(estudiantes) / sizeof(Estudiante); //Calcula el número de estudiantes en el arreglo
    // Ordenamiento del array de estudiantes por promedio de mayor a menor usando el método de la burbuja
    for (int i = 0; i < numEstudiantes - 1; i++) {
        for (int j = 0; j < numEstudiantes - i - 1; j++) {
            if (estudiantes[j].promedio < estudiantes[j + 1].promedio) {
                // Intercambiar estudiantes[j] y estudiantes[j+1]
                Estudiante temp = estudiantes[j];
                estudiantes[j] = estudiantes[j + 1];
                estudiantes[j + 1] = temp;
            }
        }
    }

    // Imprimir el array ordenado
    cout << "Array ordenado por promedio de mayor a menor: \n";
    for (int i = 0; i < numEstudiantes; i++) {
        cout << estudiantes[i].nombre << " - Promedio: " << estudiantes[i].promedio << endl;
    }

    //Llamada a la función para imprimir estudiantes con promedio mayor a 85    
    cout<<"alumnos con promedio mayor a 85:"<<endl;
    imprimirMayoresPromedio(estudiantes, numEstudiantes, 85);

    return 0;
}
