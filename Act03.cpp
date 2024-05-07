#include<iostream>
using namespace std;

class Banco {   //Definir clase banco
public:
  // Atributo estatico para la tasa de interés
  static float Tasainteres;

  // Metodo estatico para cambiar la tasa de interés
  static void Cambiartasainteres(float nuevatasa) {
    Tasainteres = nuevatasa;
  }
};

// Inicializar la tasa de interés estática
float Banco::Tasainteres = 0.01; // Tasa inicial del 1%

class Cuentabancaria {
private:
  float saldo;

public:
  // Constructor
  Cuentabancaria(float saldoinicial) : saldo(saldoinicial) {}   //Monto inicial de dinero en la cuenta bancaria

  // Metodo para depositar dinero
  void depositar(float monto) {
    saldo += monto;
  }

  // Metodo para retirar dinero
  void retirar(float monto) {
    if (saldo >= monto) {
      saldo -= monto;
    } else {
      cout << "Saldo insuficiente" << endl;
    }
  }

  // Calcular interés ganado usando la tasa de interés estática 
  float calcularInteres() {
    return saldo * Banco::Tasainteres;
  }
};

int main() {
  // Cambiar la tasa de interés del banco
  Banco::Cambiartasainteres(0.02); // Tasa del 2%

  // Crear una cuenta bancaria y definir el saldo inicial
  Cuentabancaria cuenta(1000);

  // Depositar dinero
  cuenta.depositar(500);

  // Retirar dinero
  cuenta.retirar(200);

  // Calcular interés ganado
  float interesGanado = cuenta.calcularInteres();
  cout << "Interes ganado: " << interesGanado << endl;

  return 0;
}
