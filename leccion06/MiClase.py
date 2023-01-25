class Miclase:
    variable_clase = 'Valor variable clase'
    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia

        
print(Miclase.variable_clase)
miClase = Miclase("Valor variable de instancia")
print(miClase.variable_instancia)
