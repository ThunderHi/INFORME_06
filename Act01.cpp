#include <iostream>
#include <vector>

using namespace std;
//Definición de la clase Estudiante
class Estudiante {
public:
    string nombre;
    int edad;
    vector<int> notas;  //Atributo público llamado `notas` de tipo `vector<int>` para almacenar las notas del estudiante
    double promedio;    //Atributo público llamado `promedio` de tipo `double` para almacenar el promedio de las notas del estudiante

    //Constructor para inicializar los datos
    Estudiante(string nombre, int edad, vector<int> notas) {
        this->nombre = nombre; //Asigna el valor del parámetro `nombre` al atributo `nombre` del objeto
        this->edad = edad; //Asigna el valor del parámetro `edad` al atributo `edad` del objeto
        this->notas = notas; //Asigna el valor del parámetro `notas` al atributo `notas` del objeto
        this->promedio = calcularPromedio(); //Calcula y asigna el promedio de las notas al atributo `promedio` del objeto
    }

    //Función para calcular el promedio de las notas
    double calcularPromedio() { //Función que calcula el promedio de las notas del estudiante
        double suma = 0; //Variable local para almacenar la suma de las notas
        for (int nota : notas) { //Recorre el vector de notas utilizando un bucle `for range`
            suma += nota; //Suma cada nota al valor de la variable `suma`
        }
        return suma / notas.size(); //Calcula y devuelve el promedio dividiendo la suma de las notas por la cantidad de notas
    }
};

//Función para imprimir estudiantes con promedio mayor a cierta nota
void imprimirMayoresPromedio(vector<Estudiante> estudiantes, double notaMinima) { //Función que imprime los estudiantes con un promedio mayor a la nota mínima especificada
    for (Estudiante estudiante : estudiantes) { //Recorre el vector de estudiantes utilizando un bucle `for range`
        if (estudiante.promedio > notaMinima) { //Compara el promedio del estudiante actual con la nota mínima
            cout<<estudiante.nombre<<" - Promedio: "<<estudiante.promedio<<endl; //Si el promedio es mayor, imprime el nombre y promedio del estudiante
        }
    }
}

int main() {
    //Creación de un vector de objetos Estudiante y llenado con información
    vector<Estudiante> estudiantes = {  //Vector de objetos `Estudiante` inicializado con datos de estudiantes
        Estudiante("Juan", 20, {85, 90, 88}),
        Estudiante("Maria", 22, {78, 85, 90}),
        Estudiante("Pedro", 21, {92, 88, 95}),
        Estudiante("Luisa", 23, {80, 75, 82})
    };

    //Llamada a la función para imprimir estudiantes con promedio mayor a 85    
    imprimirMayoresPromedio(estudiantes, 85);

    return 0;
}
