resultado = None
a = 2
b = 1
try:
    resultado = a/b
except ZeroDivisionError as zd:
    print(f"Ocurrio un error: {zd}")
except TypeError as te:
    print(f"Ocurrio un error: {te}")

print(f"resultado: {resultado}")
print("Continuamos....")