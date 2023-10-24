/*
Crear un programita que calcule el volumen de un cono. Recordar que la f´ormula de vol´umen de un cono es V = 1 3 πr2h donde el radio y la altura deben ser ingresados por el usuario, y se debe definir la constante pi en el c´odigo.
*/

#include <iostream>
using namespace std;

int main(){

//int mimatrix[5]{2,24,4,1,-7};
int mimatrix[5] = {2,231,-12,4,1};

for (int i=0; i<5; i++){
    mimatrix[i] = {i+1};
    i=i+1;
}

cout << "mimatrix es: " << endl;

for( int i=0; i<5;i++){

    if (i== 0){
        cout << "[";
    }

    cout << mimatrix[i];

    if (i!= 4){
        cout << ", ";
    }

    if (i== 4){
        cout << "]";
    }
}

}
