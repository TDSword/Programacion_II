'''
8. Crear una clase llamada MazoCartas, que representara un mazo de 52 cartas de poker.
Debera usar internamente otra clase, que tambien debera crear llamada Carta.
    a) La clase MazoCartas tendra un metodo repartir que robara una carta del mazo, eliminandola de este.
    b) Un metodo llamado barajar que mezcle nuevamente las cartas y se asegure que esten las 52.
    c) La clase Carta, ademas, debera tener los siguientes atributos: palo (Corazones, Diamantes, Treboles, Picas) y valor. (A,2,3,4,5,6,7,8,9,10,J,Q,K)
    d) Ademas, se debe considerar: 
        Crear el codigo fuente y guardarlo en un archivo del tipo apellido-nombretp01ej08.py
        Comentar el codigo fuente a fin de dar una mayor legibilidad
        La salida por pantalla debe contener toda la informacion necesaria para el usuario, a fin de que sea entendible el programa.
        En pantalla, debe figurar en la parte superior derecha de la pantalla el apellido y nombre del estudiante.
'''
import random

class Cartas:
#   Se recorre por palo y numero, en caso especiales, en vez del nro va la letra correspondiente
    def __init__(self):
        lista_de_cartas = []
        for j in ['Trebol','Pika','Corazon','Diamante']:
            for i in range(13):
                if i == 0:
                    lista_de_cartas.append(str(f'A de {j}'))
                elif i <= 9 and i!=0:
                    lista_de_cartas.append(str(f'{i+1} de {j}'))
                elif i == 10:
                    lista_de_cartas.append(str(f'J de {j}'))
                elif i == 11:
                    lista_de_cartas.append(str(f'Q de {j}'))
                elif i == 12:
                    lista_de_cartas.append(str(f'K de {j}'))
        self.cartas = lista_de_cartas

#   Seleciona un carta aleatoria, se queda guardada en una variable x, posteriormente se usa como referencia para saber q carta sacar y returnar
    def robar_carta(self):
        x = random.choice(self.cartas)
        self.cartas.remove(str(x))
        return x

#   Como robar carta ya es aleatorio, no hace falta mezclar el mazo, para mezclar, simplemente de redefine el mazo a como estaba
    def mezclar_cartas(self):
        listado_de_cartas = []
        for j in ['Trebol','Pika','Corazon','Diamante']:
            for i in range(13):
                if i == 0:
                    listado_de_cartas.append(str(f'A de {j}'))
                elif i <= 9 and i!=0:
                    listado_de_cartas.append(str(f'{i+1} de {j}'))
                elif i == 10:
                    listado_de_cartas.append(str(f'J de {j}'))
                elif i == 11:
                    listado_de_cartas.append(str(f'Q de {j}'))
                elif i == 12:
                    listado_de_cartas.append(str(f'K de {j}'))
        self.cartas = listado_de_cartas


mazo_generico = Cartas()

print('-------------------MAZO(52)--------------------------------')

print(mazo_generico.cartas)

print('-------------------------------------------------------------')
#   El usuario roba 10 cartas
mano_de_cartas = [ mazo_generico.robar_carta() for i in range(10) ]

print('-------------------MANO(10)--------------------------------')
#   Se printea la mano para ver las cartas robadas
print(mano_de_cartas)

print('-------------------MAZO(42)--------------------------------')
#   Se confirma q el mazo ya no cuenta con las cartas robadas
print(mazo_generico.cartas)

print('-------------------MAZO_MEZCLADO(52)-----------------------')
#   Ahora de repone el mazo y se printean las respectivas cartas
mazo_generico.mezclar_cartas()

print(mazo_generico.cartas)
