'''Se realizará un modulo de un sistema de cuentas diarias,
 que llevará a cabo el registro de las ventas diarias,
 no se sabe cuantos clientes se atenderán, al final del día
 se genera la cantidad de ventas, la cantidad de clientes atendidos,
 y el promedio de la venta del día.'''


def cuentas_diarias():
    daily_sales = 0
    client_count = 0

    while True:
        try:
            sale = float(input("Ingrese una venta o 0 para terminar: "))
            if sale == 0:
                break
            daily_sales += sale
            client_count += 1

            option = input("Desea agregar otra venta? (s/n): ").lower()
            if option == "n":
                break
        except:
            print("Valor incorrecto")

    if client_count > 0:
        average_sales = daily_sales / client_count
        print(f"Total de ventas {daily_sales:.2f}")
        print(f"Total de ventas {client_count}")
        print(f"Total de ventas {average_sales:.2f}")
    else:
        print("No se registraron ventas el día de hoy.")


cuentas_diarias()