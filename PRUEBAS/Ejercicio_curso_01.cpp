#include <iostream>

using namespace std;


int main(){


    cout << "Bienvenido al Servicio de intalacion de piso flotante!"<<endl;


    int metros_calidad_media{0};

    cout << "\nCuantos metros de calidad media: ";

    cin >> metros_calidad_media;


    int metros_calidad_alta{0};

    cout << "\nCuantos metros de calidad alta: ";

    cin >> metros_calidad_alta;


    const double calidad_media{35.5};

    const double calidad_alta{55.3};

    const double iva{0.21};

    const int expira_presupuesto{30};

    cout << "Presupuesto para piso flotante: "<< endl;

    double presupuesto_media{metros_calidad_media*calidad_media};

    double presupuesto_alta{metros_calidad_alta*calidad_alta};

    double presupuesto_total{(presupuesto_media+presupuesto_alta)*(iva+1)};

    double presupuesto{(presupuesto_media+presupuesto_alta)};

    double iva_total{(presupuesto_media+presupuesto_alta)*(iva)};



    cout << "Presupuesto: " << presupuesto << endl;

    cout << "Iva: " << iva_total << endl;

    cout << "Presupuesto total: " << presupuesto_total << endl;



    return 0;

}