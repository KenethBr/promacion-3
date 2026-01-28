def ventas():
    # Contador para preguntar por el # de la venta
    count = 0
    totalVenta = 0  # Se inicializa en 0 para poder sumarle un valores
    # recorre 5 veces para preguntar por la venta
    for ventas in range(1, 6):
        count += 1  # Incrementa el contador en 1
        totalVenta += float(input(f"Ingrese la venta #{count}: "))  # Asigna y suma

    promedioVentas = totalVenta / 5  # operación para sacar el promedio

    if promedioVentas >= 677:  # condicional para manejar si es mayor o menor al promedio (677.00)
        print(f"El promedio de venta de hoy: '{promedioVentas}' es mayor al promedio diario (677.00)")
    else:
        print(f"El promedio de venta de hoy: '{promedioVentas}' es menor al promedio diario (677.00)")


ventas()


def cambioEuros():  # funcion para convertir a euros
    # Declaración de variables tipo float
    tasaDolar = 1.21
    tasaColones = 738.59
    tasaLempiras = 29.16
    tasaPesosColombianos = 4314.00

    nombre = input("Ingrese su nombre: ")
    opcion = int(input("¿Qué moneda desea convertir a euros?\n"  # Menú
                       "1. Dolar\n"
                       "2. Colones\n"
                       "3. Lempiras\n"
                       "4. Pesos Colombianos\n"))

    # Se ingresa el monto deseado
    monto = float(input("Ingrese el monto de la moneda que desea convertir a Euros: "))
    # condicional para manejar casos
    if opcion == 1:
        totalConvertido = monto / tasaDolar  # operación para sacar el total ya convertido a euros
        print(
            f"Serñor(a) {nombre} su monto de: US${monto:.2f} equivalen a €{totalConvertido:.2f}")  # mostrar en pantalla
    elif opcion == 2:
        totalConvertido = monto / tasaColones
        print(
            f"Serñor(a) {nombre} su monto de: ₡{monto:.2f} equivalen a €{totalConvertido:.2f}")  # .2 se usa para mostrar solo dos decimales
    elif opcion == 3:
        totalConvertido = monto / tasaLempiras
        print(f"Serñor(a) {nombre} su monto de: L{monto:.2f} equivalen a €{totalConvertido:.2f}")
    elif opcion == 4:
        totalConvertido = monto / tasaPesosColombianos
        print(f"Serñor(a) {nombre} su monto de: COP${monto:.2f} equivalen a €{totalConvertido:.2f}")
    else:
        print("Opcion invalida")  # Manejo de error


cambioEuros()
