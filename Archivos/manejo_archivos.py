try:
    archivo = open("prueba.txt", "w")
    archivo.write('Agregamos informacion al archivo \n')
    archivo.write('Adios popo')
except Exception as e:
    print(e)
finally:
    archivo.close()