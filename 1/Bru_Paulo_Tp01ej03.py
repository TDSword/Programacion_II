'''
3. Trabajo con calculo de Liquidacion de Sueldos.
    a) Crear una clase llamada Empleado.
    b) La clase debe contener los atributos: nombre, horas-trabajadas y tarifa-hora.
    c) Crear el metodo: calculo-salario.
    d) Se debe crear el objeto correspondiente, y se le debe pedir al operador que ingrese los datos necesarios para que el programa calcule el sueldo que le corresponde cobrar en funcion de las horas trabajadas y el valor de la hora trabajada.
    e) Ademas, se debe considerar:

        Crear el codigo fuente y guardarlo en un archivo del tipo apellido-nombretp01ej03.py
        Comentar el codigo fuente a fin de dar una mayor legibilidad
        La salida por pantalla debe contener toda la informacion necesaria para el usuario, a fin de que sea entendible el programa.
        En pantalla, debe figurar en la parte superior derecha de la pantalla el apellido y nombre del estudiante.
'''

class Empleado:
    def __init__(self,horas,sueldo):
        self.horas = horas
        self.sueldo = sueldo

    def calcular_salario(self):
        return self.horas*self.sueldo

print('-------------------------------------------------------------')
print('                                                    Bru Paulo')
print('Buenas estimado usuario, usted esta ejecutando un programa.\nUsted debera ingresar las horas trabajadas y cuanto cobra por \nhora, posteriormente, dicho programa va a calcular cuanto le \ncorresponde cobrar .Para que el programa funcione correctamente \ntiene que insertar valores numericos validos, es decir, ingresar\n solo numeros reales positivos, capaces de escribirse con numeros\n del 0 al 9.')
print('-------------------------------------------------------------')

empleado_generico = Empleado(float(input('ingrese cuantas horas trabaja al mes: ')),float(input('ingrese cuanto cobra por hora: ')))

print('-------------------------------------------------------------')

#   Por ultimo printeo lo pedido
print(f'Usted devera cobrar ${empleado_generico.calcular_salario()} al mes')

print('                            gracias por usar el programa')
print('-------------------------------------------------------------')