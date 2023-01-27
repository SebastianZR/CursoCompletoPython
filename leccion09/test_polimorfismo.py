from Empleado import Empleado
from leccion09.Gerente import Gerente


def imprimir_detalles(objeto):
    print(objeto)


empleado = Empleado("Juan", 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, "Sistemas")
imprimir_detalles(gerente)
