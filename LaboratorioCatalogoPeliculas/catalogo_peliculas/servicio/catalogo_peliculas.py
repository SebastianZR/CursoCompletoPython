import os


class CatalogoPeliculas:
    ruta_archivo = "peliculas.txt"

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, "a") as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        try:
            with open(cls.ruta_archivo, "r") as archivo:
                print("Catalago de peliculas".center(50, '-'))
                for linea in archivo:
                    print(f"- {linea}")
        except Exception:
            print(f"No hay arachivo {cls.ruta_archivo}")


    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f"Archivo eliminado {cls.ruta_archivo}")
