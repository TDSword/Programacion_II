/*
4.      Crear un programa que pida al usuario dos n´umeros y devuelva la suma de ambos, y su multiplicaci´on.
*/

#include <iostream>
using namespace std;

int main(){
    int n1, n2;
    cout << "Ingrese el primer nro: ";
    cin >> n1;

    cout << "Ingrese el primer nro: ";
    cin >> n2;

    int nsuma = n1+n2;
    int nmulti = n1*n2;

    cout << "La suma es:" << nsuma << endl;
    cout << "La multiplicacion es:" << nmulti << endl;

}