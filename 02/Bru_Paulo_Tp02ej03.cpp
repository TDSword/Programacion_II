/*
3.      Crear un programita que calcule el area de un c´ırculo, para un radio fijo dentro del c´odigo. Defina la constante PI.
*/

#include <iostream>
using namespace std;

int main(){
    const double pi{3.1415};

    double radio{2};

    cout << "Ingrese el radio del Circulo" << endl;

    cin >> radio;

    double area{pi*radio*radio};

    cout << "El area es: " << area << endl;

}