from LaboratorioMundoPC.computadora import Computadora
from LaboratorioMundoPC.monitor import Monitor
from LaboratorioMundoPC.orden import Orden
from LaboratorioMundoPC.raton import Raton
from LaboratorioMundoPC.teclado import Teclado

if __name__ == '__main__':

    teclado1 = Teclado("HP", "USB")
    raton1 = Raton("HP", "USB")
    monitor1 = Monitor("HP", 27)
    computadora1 = Computadora("HP", monitor1, teclado1, raton1)

    teclado2 = Teclado("APPLE", "USB")
    raton2 = Raton("APPLE", "USB")
    monitor2 = Monitor("APPLE", 27)
    computadora2 = Computadora("APPLE", monitor2, teclado2, raton2)

    teclado3 = Teclado("LENOVO", "USB")
    raton3 = Raton("LENOVO", "USB")
    monitor3 = Monitor("LENOVO", 27)
    computadora3 = Computadora("LENOVO", monitor3, teclado3, raton3)

    computadoras1 = [computadora1, computadora2 , computadora3]

    teclado4 = Teclado("ACER", "USB")
    raton4 = Raton("ACER", "USB")
    monitor4 = Monitor("ACER", 24)
    computadora4 = Computadora("ACER", monitor4, teclado4, raton4)


    orden1 = Orden(computadoras1)
    print(orden1)
    orden1.agregar_computadora(computadora4)
    print(orden1)

