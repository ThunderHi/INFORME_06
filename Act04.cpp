#include <iostream>
using namespace std;

class Vector {
public:
  float x;
  float y;

  // Constructor
  Vector(float x, float y) : x(x), y(y) {}

  // Operador suma (+) sobrecargado
  Vector operator+(const Vector& otroVector) {
    return Vector(x + otroVector.x, y + otroVector.y);
  }

  // Operador resta (-) sobrecargado
  Vector operator-(const Vector& otroVector) {
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
  Vector vectorC = vectorA + vectorB;
  vectorC.imprimir(); // Resultado: Vector: (6, 8)

  // Resta de vectores
  Vector vectorD = vectorA - vectorB;
  vectorD.imprimir(); // Resultado: Vector: (-2, -2)

  return 0;
}
