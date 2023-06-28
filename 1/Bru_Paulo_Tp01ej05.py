'''
5. Trabajo con Maquina Calculadora - Conversor de mts a km y cm.
    a) Crear una clase llamada MaquinaCalculadora.
    b) La clase debe contener los atributos: peso, color y altura.
    c) Crear el metodo: metros-a-kilometros.
    d) Crear el metodo: metros-a-centrimetros.
    e) Se debe crear el objeto correspondiente, y se le debe pedir al operador que ingrese los datos necesarios para que el programa calcule la conversion de metros a kilometros y de metros a centimetros.
    f ) Ademas, se debe considerar:
        Crear el codigo fuente y guardarlo en un archivo del tipo apellido-nombretp01ej05.py
        Comentar el codigo fuente a fin de dar una mayor legibilidad
        La salida por pantalla debe contener toda la informacion necesaria para el usuario, a fin de que sea entendible el programa.
        En pantalla, debe figurar en la parte superior derecha de la pantalla el apellido y nombre del estudiante.
'''


class MaquinaCalculadora:
#   Los parametros son tres, pero lo que intersa es solo la altura, asi q por defecto se deja el peso y color ya definidos, asi el usuario tiene la posisbilidad de manipularlos si desea
    def __init__(self,altura,peso=0,color='negro'):
        self.altura = altura
        self.peso = peso
        self.color = color

    def metros_a_kilometros(self):
        return (self.altura/1000)

    def metros_a_centimetros(self):
        return (self.altura*100)


#   Una presentación
print('-------------------------------------------------------------')
print('                                                    Bru Paulo')
print('Buenas! Usted deberá ingresar un nro en metros, posteriormente \nel programa lo analizara y le dara su equivalente en centimetros \ny metros')
print('-------------------------------------------------------------')
#   Se define el nro
nro_generico = MaquinaCalculadora(int(input('Ingrese el nro de metros: ')))

print(f'Su equivalente en centimetros es: {nro_generico.metros_a_centimetros()} cm.')
print(f'Su equivalente en kilometros es: {nro_generico.metros_a_kilometros()} km.')

print('                            gracias por usar el programa')
print('-------------------------------------------------------------')  