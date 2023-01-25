def factorial(n):
    if n == 1:
        return 1
    else :
        return n*factorial(n-1)

def imprimir_numero_recursivo(n):
    if n == 1 :
        print(1)
    else:
        print(n)
        imprimir_numero_recursivo(n-1)
def pago_impuestos():
    pago_sin_impuesto = int(input("Proporcione el pago sin impuesto: "))
    impuesto= int(input("Proporcione el monto del impuesto: "))
    return pago_sin_impuesto+(pago_sin_impuesto*(impuesto/100))



