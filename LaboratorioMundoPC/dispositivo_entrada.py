class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    def __str__(self):
        return f"Dispositivo [Entrada:{self.tipo_entrada} , Marca:{self.marca}]"
