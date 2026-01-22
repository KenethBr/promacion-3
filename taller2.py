"""
Calcula el area de una pared, cuantos litros necesita para pintarse
y cuanto cuesta en total para pintarla
"""


def dimensiones():
    # Variables que se reciben por el usuario
    alto = float(input("Digite el alto: "))
    ancho = float(input("Digite el ancho: "))

    # Guardamos en variables los resultados de las operaciones
    area = alto * ancho
    litrosRequeridos = area / 10
    costoTotal = litrosRequeridos * 15

    # Se imprimen los resultados
    print("El área es de:", area, "m2")
    print("Se requieren:", litrosRequeridos, "litros")
    print("Se debe pagar un total de:", costoTotal)


dimensiones()

"""
Verifica quién tiene más edad, si tienen la misma edad
y si ambos son mayores de 18 años
"""


def comaprarEdad():
    # Varibles ingresadas por el usuario
    edad1 = int(input("Digite la primera edad: "))
    edad2 = int(input("Digite la segunda edad: "))
    # mayor = max(edadUno, edadDos) //Otra forma de sacar el mayor de dos numeros
    # print(f"{mayor} es mayor") //imprime el mayor de la función max()
    print(edad1, "es mayor") if edad1 > edad2 else print(edad2, "es mayor")  # imprime el mayor
    print("Las edades", edad1, "y", edad2, "son iguales") if edad1 == edad2 \
        else print("Las edades", edad1, "y", edad2, "son diferentes")  # Imprime si son iguales las edades
    print("Ambos son mayores de edad.") if edad1 >= 18 and edad2 >= 18 else print("Al menos uno es menor de edad.")


comaprarEdad()

"""
Determina si un estudiante puede acceder a una beca según
su promedio, recursos y si fue voluntario.
"""


def becas():
    # Entrada de datos por el usuario
    promedio = float(input("Digite el promedio: "))
    # .lower() cambia a minuscula lo escrito por el usuario
    esEscasosRecursos = input("¿Eres de escasos recursos? (si/no): ").lower() == "si"
    # == "si" pregunta si lo que escribio el usuario es igual a lo que esta escrito entre comillas es igual, si
    # es igual, retorna true, si no, false
    esVoluntario = input("¿Fuiste voluntario? (si/no): ").lower() == "si"

    # Guarda como true o false si promedio es mayor o igual a lo pedido y si el true las varibles anteriores
    condicion_a = (promedio >= 4.0 and esEscasosRecursos)
    condicion_b = (promedio >= 3.5 and esVoluntario)

    # pregunta si es alguna de las condiciones se cumplen, si alguna se cumple, entra en el prime if, si no,
    # entra en el else
    if condicion_a or condicion_b:
        print("Accediste a la beca")
    else:
        print("Lo siento, no accediste a la beca")


becas()
