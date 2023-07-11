'''
2. Trabajo con Circulos.
    a) Crear una clase llamada Circulo.
    b) La clase debe contener el atributo: radio.
    c) Crear los metodos como: calculo-area y calculo-circunferencia.
    d) Se debe crear el objeto correspondiente, y se le debe pedir al operador que ingreselos datos necesarios para que el programa calcule el area y la circunferencia.
    e) Ademas, se debe considerar:
        Crear el codigo fuente y guardarlo en un archivo del tipo apellido-nombretp01ej02.py
        Comentar el codigo fuente a fin de dar una mayor legibilidad
        La salida por pantalla debe contener toda la informacion necesaria para el usuario, a fin de que sea entendible el programa.
        En pantalla, debe figurar en la parte superior derecha de la pantalla el apellido y nombre del estudiante.

'''

class Circulo:

#   El atributo correspondiente es radio
    def __init__(self, radio):
        self.radio = radio

#   Para el area le pedimos que nos retone la multiplicacion entre pi y el radio al cuadrado, ya que esta nos da el area
    def calculo_area(self):
        return (3.14159*(self.radio**2))

#   Lo mismo se aplica con el perimetro
    def calculo_circunferencia(self):
        return (2*3.14159*self.radio)

#   Una presentacion al usuario
print('-------------------------------------------------------------')
print('                                                    Bru Paulo')
print('Buenas estimado usuario, usted esta ejecutando un programa.\nUsted debera ingresar el radio de un circulo, posteriormente,\ndicho programa va a encontrar la circunferencia y area.\nPara que el programa funcione correctamente tiene que insertar\nvalores numericos validos, es decir, ingresar solo numeros \nreales positivos, capaces de escribirse con numeros del 0 al 9.')
print('-------------------------------------------------------------')

#   Ahora se define el circulo
circulo_generico = Circulo(float(input('ingrese el radio: ')))

print('-------------------------------------------------------------')

#   Por ultimo printeo lo pedido
print(f'El area es de {circulo_generico.calculo_area()} cm^2',
    f'\nEl perimetro es de {circulo_generico.calculo_circunferencia()} cm')

print('                            gracias por usar el programa')
print('-------------------------------------------------------------')