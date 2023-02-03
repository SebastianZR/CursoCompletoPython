archivo = open('prueba.txt', 'r')
#Leer algunos caracteres
#print(archivo.read(5))
#Leer lineas completas
#print(archivo.readline())
#iterar en el archivo
#for linea in archivo:
#    print(linea)

# Leer lineas
# Acceder a una linea de la lista
#print(archivo.readlines()[2])

# Abrimos un nuevo archivo
# "a" sirve para anexar informacion

archivo2 = open('copia.txt', 'a')
archivo2.write(archivo.read())
archivo2.close()
archivo.close()
