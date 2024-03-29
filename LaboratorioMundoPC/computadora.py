from LaboratorioMundoPC.monitor import Monitor
from LaboratorioMundoPC.raton import Raton
from LaboratorioMundoPC.teclado import Teclado


class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self._id_computadora = Computadora.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f"""
        {self._nombre}: {self._id_computadora},
        Monitor: {self._monitor},
        Teclado: {self._teclado},
        Raton: {self._raton},
        """


if __name__ == '__main__':

    teclado1 = Teclado("HP", "USB")
    raton1 = Raton("HP", "USB")
    monitor1 = Monitor("DELL", 27)
    computadora1 = Computadora("HP", monitor1, teclado1, raton1)
    print(computadora1)
