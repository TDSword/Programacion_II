
'''
1. Trabajo con Rectangulos.

    a) Crear una clase llamada Rectangulo.   
    b) La clase debe contener los atributos: base y altura.
    c) Crear los metodos como: calculo-area y calculo-perimetro.
    d) Se debe crear el objeto correspondiente, y se le debe pedir al operador que ingreselos datos necesarios para que el programa calcule el area y el perimetro.
    e) Ademas, se debe considerar:

        Crear el codigo fuente y guardarlo en un archivo del tipo apellido-nombretp01ej01.py
        Comentar el codigo fuente a fin de dar una mayor legibilidad
        La salida por pantalla debe contener toda la informacion necesaria para el usuario, a fin de que sea entendible el programa
        En pantalla, debe figurar en la parte superior derecha de la pantalla el apellido y nombre del estudiante
'''

class Rectangulo:

#   Los atributos correspondientes son la base y la altura
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

#   Para el area le pedimos que nos retone la multiplicacion entre la base y altura, ya que esta nos da el area
    def calculo_area(self):
        return self.base*self.altura

#   Lo mismo se aplica con el perimetro
    def calculo_perimetro(self):
        return (self.base*self.altura)/2

#   Una presentacion al usuario
print('-------------------------------------------------------------')
print('                                                    Bru Paulo')
print('Buenas estimado usuario, usted esta ejecutando un programa.\nUsted debera ingresar la base y la altura de un triangulo,\nposteriormente, dicho programa va a encontrar el perimetro y\narea. Para que el programa funcione correctamente tiene que\ninsertar valores numericos validos, es decir, ingresar solo \nnumeros reales positivos, capaces de escribirse con numeros\ndel 0 al 9.')
print('-------------------------------------------------------------')

#   Ahora se define el triangulo
triangulo_generico = Rectangulo(float(input('ingrese la base: ')), float(input('ingrese la altura: ')))

print('-------------------------------------------------------------')

#   Por ultimo printeo lo pedido
print(f'El area es de {triangulo_generico.calculo_area()} cm^2',
    f'\nEl perimetro es de {triangulo_generico.calculo_perimetro()} cm')

print('                            gracias por usar el programa')
print('-------------------------------------------------------------')