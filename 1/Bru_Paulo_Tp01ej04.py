'''
4. Trabajo con calculo Indice de Masa Corporal (IMC).
    a) Crear una clase llamada Persona.
    b) La clase debe contener los atributos: nombre, peso y altura.
    c) Crear el metodo: calculo-imc.
#    d) Se debe crear el objeto correspondiente, y se le debe pedir al operador que ingrese los datos necesarios para que el programa calcule el sueldo que le corresponde cobrar en funcion de las horas trabajadas y el valor de la hora trabajada.
    e) Nota: El IMC (Indice de Masa Corporal)es una medida que se utiliza para determinar si una persona tiene un peso saludable en relacion con su altura. Se calcula dividiendo el peso de una persona en kilogramos por el cuadrado de su altura en metros.
    f) Ademas, se debe considerar:
            Crear el codigo fuente y guardarlo en un archivo del tipo apellido-nombretp01ej04.py
            Comentar el codigo fuente a fin de dar una mayor legibilidad
            La salida por pantalla debe contener toda la informacion necesaria para el usuario, a fin de que sea entendible el programa.
            En pantalla, debe figurar en la parte superior derecha de la pantalla el apellido y nombre del estudiante.
'''

class Persona:
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

# dividiendo el peso de una persona en kilogramos por el cuadrado de su altura en metros.
    def calculo_imc(self):
        return ((self.peso)/(self.altura**2))

#   Una presentacion al usuario
print('-------------------------------------------------------------')
print('                                                    Bru Paulo')
print('Buenas estimado usuario, usted esta ejecutando un programa.\nUsted debera ingresar su nombre, peso y altura, posteriormente,\ndicho programa va a encontrar su IMC.Para que el programa funcione \ncorrectamente tiene que insertar valores numericos validos, \nes decir, que para ingresar su peso y altura debe ingresar solo \nnumeros reales positivos, capaces de escribirse con numeros del \n0 al 9.')
print('-------------------------------------------------------------')

#   Ahora se define el circulo
persona_generica = Persona(str(input('Ingrese si nombre: ').title()),float(input('ingrese su altura en metros: ')),float(input('ingrese su peso en kg:  ')))

print('-------------------------------------------------------------')

#   Por ultimo printeo lo pedido
print(f'{persona_generica.nombre} tu IMC es de: {persona_generica.calculo_imc()}')

print('                            gracias por usar el programa')
print('-------------------------------------------------------------')  