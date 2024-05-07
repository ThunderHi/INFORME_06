#include <iostream>   //inclusion de librería iostream
using namespace std;  //uso de espacio standar

class Vector {  //creacion de clase Vector
public:
  float x;    //creacion de atributos
  float y;

  // Constructor
  Vector(float x, float y) : x(x), y(y) {}

  // Operador suma (+) sobrecargado
  Vector operator+(const Vector& otroVector) {  //se envia objeto como parametro
    return Vector(x + otroVector.x, y + otroVector.y);
  }

  // Operador resta (-) sobrecargado
  Vector operator-(const Vector& otroVector) {  //se envia objeto como parametro
    return Vector(x - otroVector.x, y - otroVector.y);
  }

  // Imprimir el vector
  void imprimir() {
    cout << "Vector: (" << x << ", " << y << ")" << endl;
  }
};

int main() {
  // Crear vectores
  Vector vectorA(5.4, 7.3);
  Vector vectorB(4.5, 5.2);

  // Suma de vectores
  //se crea otro objeto y se asigna la suma
  Vector vectorC = vectorA + vectorB;
  vectorC.imprimir(); // Resultado: Vector: (9.9, 12.5)

  // Resta de vectores
  //se crea otro objeto y se asigna la resta
  Vector vectorD = vectorA - vectorB;
  vectorD.imprimir(); // Resultado: Vector: (0.9, 2.1)

  return 0;
}
