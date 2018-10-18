# Autor: Jesús Emmanuel Alcalá Nava
# Descripción: Este programa encuentra el mayor número de una lista y hace divisiones

#Función para hecer las divisiones
def dividir():
    print("Hacer divisiones")
    dividendo = int(input("Dividendo:"))
    divisor = int(input("Divisor: "))
    dividendo1 = dividendo
    cociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente += 1
    print("%d / %d = %d, sobra %d" % (dividendo1, divisor, cociente, dividendo))

#Función para encontrar el mayor número
def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor")
    opcion = -2
    mayor = -2
    while opcion != -1:
        opcion = int(input("Teclea un número [-1 para salir]: "))
        if opcion > mayor:
            mayor = opcion
        else:
            pass
    if mayor != -1:
        print("El mayor es:", mayor)
    else:
        print("No hay valor mayor")


def main():
    accion = -1
    while accion != 3:
        print("""Misión 07. Ciclos while
Autor: Jesús Emmanuel Alcalá Nava
Matrícula: A01376766
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")
        accion = int(input("Teclea tu opción: "))
        if accion == 1:
            dividir()
        elif accion == 2:
            encontrarMayor()
        elif accion != 1 and accion != 2 and accion != 3:
            print("ERROR, teclea 1, 2 o 3")
    print("Gracias por usar este programa, regresa pronto.")
main()