'''
7. Crear una clase llamada Facturador, con los siguientes atributos: fechafacturacion, nombrecliente,
detalle, preciounitario, cantidad, preciototal. Crear los eventos para facturar
mercaderias varias y crear evento para mostrar la factura por pantalla, pedir que el
usuario ingrese los datos. comentar el codigo y la salida por pantalla.. Debera crear los
siguientes metodos:

    a) Un metodo llamado facturarmercaderia. El cual debera realizar el proceso de facturacion, es decir, se debera ingresar: fecha facura, nombre de cliente, detalle producto, cantidad, precio unitorio y calcular precio total.
    b) Un metodo llamado Mostrar factura por pantalla.

'''
class Facturador:
#   A pesar de no tener valor a la hora de definir la clase, los atributos siguen estando
    def __init__(self):
        self.fechafacturacion = ''
        self.nombrecliente = ''
        self.detalle = ''
        self.preciounitario = ''
        self.cantidad = ''
        self.preciototal = ''

#   Ahora se refinen los valores vacios por los ingresados por el usurario
    def facturarmercaderia(self):
        self.fechafacturacion = str(input('Ingrese fecha facturacion: '))
        self.nombrecliente = str(input('Ingrese nombre cliente: '))
        self.detalle = str(input('Ingrese   detalle: '))
        self.preciounitario = float(input('Ingrese precio unitario: '))
        self.cantidad = int(input('Ingrese cantidad: '))
        self.preciototal = float(float(self.preciounitario)*float(self.cantidad))

    def mostrar_factura(self):
        # Simplemente comprobando q el precio unitario sea distinto de '' se puede saber si se lleno la factura, en caso contrario tendria que ser un numero
        if self.preciounitario != '':
            print(f'-------------------------FACTURA---------------------------\nFecha de facturacion: {self.fechafacturacion} \nNombre del cliente: {self.nombrecliente}')
        else:
            print('NO SE REGISTRO NINGUNA FACTURA')

# se definee la compra
compra_generica = Facturador()

n= ''
print('-------------------------------------------------------------')
print('                                                    Bru Paulo')
print('Buenas! Este programa creara facturas:\n 1) Para crear/redefinir la factura\n 2) Para mostrar la factura\n 3) Para salir')
while n != 3:
    if n != '':
        print('-------------------------------------------------------------')
        print(' 1) Para crear/redefinir la factura\n 2) Para mostrar la factura\n 3) Para salir')

    n = int(input('\nIngrese el nro: '))

    # Un print solo x motivos esteticos
    if n == 1:
        print('')
        compra_generica.facturarmercaderia()
    elif n == 2:
        print('')
        compra_generica.mostrar_factura()
    elif n == 3:
        print('gracias por usar el programa')
        print('-------------------------------------------------------------')
    else:
        print('NUMERO NO VALIDO. Intente nuevamente')