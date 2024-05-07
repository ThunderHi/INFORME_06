#include <iostream>
#include <string>

using namespace std;

//Declaración anticipada de la clase Circulo
class Circulo;

//Función para calcular el área de un círculo
double calcularArea(const Circulo& c);  // Declara una función llamada `calcularArea` que devuelve un valor de tipo `double`
//Recibe un parámetro de tipo `const Circulo&` llamado `c`
//NOTA: La palabra clave `const` indica que el objeto `Circulo` pasado a la función no se puede modificar dentro de la función

//Definición de la clase Circulo
class Circulo {
private:
    double radio;   //Atributo privado llamado `radio` de tipo `double` para almacenar el radio del círculo
    double diametro;    //Atributo privado llamado `diametro` de tipo `double` para almacenar el diámetro del círculo

public:
    //Constructor de la clase que inicializa los atributos `radio` y `diametro` con el valor proporcionado en el parámetro `r`
    Circulo(double r) : radio(r), diametro(2 * r) {}

    //Declaración de la función amiga
    //Declara la función `calcularArea` como una función amiga de la clase `Circulo`
    //Esto permite que la función `calcularArea` acceda a los atributos privados de la clase `Circulo`
    friend double calcularArea(const Circulo& c);
};

//Implementación de la función para calcular el área del círculo
double calcularArea(const Circulo& c) { //Implementación de la función `calcularArea` definida anteriormente
    return 3.14159 * c.radio * c.radio; // Calcula y devuelve el área del círculo utilizando la fórmula `π * radio^2`
}

int main() {
    //Creación de instancias de la clase Circulo
    Circulo circulo1(5.0); //Crea un objeto `Circulo` llamado `circulo1` con un radio de 5.0
    Circulo circulo2(3.0); //Crea un objeto `Circulo` llamado `circulo2` con un radio de 3.0

    //Utilización de la función amiga para calcular el área de los círculos
    cout<<"Area del circulo 1 es la siguiente: "<<calcularArea(circulo1)<<endl;
    cout<<"Area del circulo 2 es la siguiente: "<<calcularArea(circulo2)<<endl;

    return 0;
}
