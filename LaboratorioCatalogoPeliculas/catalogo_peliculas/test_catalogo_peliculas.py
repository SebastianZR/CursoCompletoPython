from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas

opcion = None
while opcion != 4:
    try:
        print("""
        Bienvenido.
        Opciones:
        1. Agregar pelicula
        2. Listar peliculas
        3. Remover peliculas
        4. Salir
        """)
        opcion = int(input('Escribe una opcion(1-4):\n'))
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
    catalogoPeliculas = CatalogoPeliculas()
    if opcion == 1:
        nombre_pelicula = input('Escribe el nombre de la pelicula: ')
        pelicula = Pelicula(nombre_pelicula)
        catalogoPeliculas.agregar_pelicula(pelicula)
        print("Pelicula Agregada :) ")
    elif opcion == 2:
        catalogoPeliculas.listar_peliculas()
    elif opcion == 3:
        catalogoPeliculas.eliminar_peliculas()
    else:
        print("Opcion invalida intenta de denuevo")
else:
    print("Salimos del programa ...")
