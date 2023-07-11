'''
6. Crear una clase llamada Computo, con su constructor por defecto sin parametros, que
permitira realizar una serie de calculos sobre numeros enteros. Debera crear los siguientes
metodos:
    a) Un metodo llamado factorial que permita calcular el factorial de un numero entero. Debera testear el metodo instanciando la clase como en todos los ejercicios.
    b) Un metodo llamado suma que calcule la suma de los primeros n numeros enteros.
    c) Un metodo llamado es-primo que permita testear si el numero es primo o no.
    d) Un metodo tabla-multiplicacion que creara y mostrara la tabla de multiplicar de un numero entero dado.
    e) Un metodo lista-divisores que obtenga todos los divisores de un dado numero entero y los retorne en un arreglo.
    f ) Ademas, se debe considerar:
        Crear el codigo fuente y guardarlo en un archivo del tipo apellido-nombretp01ej06.py
        Comentar el codigo fuente a fin de dar una mayor legibilidad
        La salida por pantalla debe contener toda la informacion necesaria para el usuario, a fin de que sea entendible el programa.
        En pantalla, debe figurar en la parte superior derecha de la pantalla el apellido y nombre del estudiante.
'''

class Computo:
    def __init__(self,nro):
        self.nro = nro

#   Para calcular el factorial y la suma defino y llamo a una funcion recursiva
    def calcular_factorial(self):
        def factorial(n):
            if n==0 or n==1:
                        resultado=1
            elif n>1:
                        resultado=n*factorial(n-1)
            return resultado
        return factorial(self.nro)

    def calcular_suma(self):
        def suma(n):
            if n==0 or n==1:
                        resultado=1
            elif n>1:
                        resultado=n+suma(n-1)
            return resultado
        return suma(self.nro)

#   Para calcular la primicidad se usan la propiedades de los nros primos
    def calcular_primicidad(self):
        for i in range(2,self.nro):
            if self.nro % i == 0:
                return "Compuesto"
        return "Primo"

#   Para hacer la tabla acumulo los resultados en una palabra vacia para poder retornarla como una unica cadena
    def calcular_tabla(self):
        tabla = ''
        for i in range(10):
            tabla += str(f'{self.nro} x {i+1} = {(i+1)*self.nro}\n')
        return tabla

#   Recorre los nros anteriores y comprueba si es divisor, en caso de q así sea lo uno a la cadena
    def calcular_divisores(self):
        div = ''
        for i in range(self.nro):
            if self.nro % (i+1) == 0:
                div += str(f'{i+1} ')
        if div != '':
            return div
        else:
            return 'No tiene divisores'

#   Una presentación
print('-------------------------------------------------------------')
print('                                                    Bru Paulo')
print('Buenas! Usted deberá ingresar un nro entero positivo, posteriormente \nel programa lo analizara')
print('-------------------------------------------------------------')
#   Se define el nro
nro_generico = Computo(int(input('Ingrese el nro entero positivo: ')))



print(f'Su factorial es: {nro_generico.calcular_factorial()}')
print(f'Su suma es: {nro_generico.calcular_suma()}')
print(f'Es un nro: {nro_generico.calcular_primicidad()}')
print(f'Su tabla es: \n{nro_generico.calcular_tabla()}')
print(f'Sus divisores: {nro_generico.calcular_divisores()}')

print('                            gracias por usar el programa')
print('-------------------------------------------------------------')  