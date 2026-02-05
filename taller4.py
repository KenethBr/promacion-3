'''
El salario semanal se calcula en base a las horas que trabajo el empleado en la semana.
Si las horas trabajadas superan las 40 horas, el pago por hora extra es el doble.
Ejemplo: 50 horas trabajadas en una semana, 10 horas se pagan al doble del precio de hora trabajada.
Debe ingresar el nombre del empleado, la cantidad de horas trabajadas en la semana, la rata por hora.

'''


def calcular_horas_trabajadas():
    try:
        nombre = input("Ingresa el nombre del empleado: ")
        horas_trabajadas = int(input("Ingrese la horas trabajadas: "))
        rata_hora = float(input("Ingrese la rata por hora: "))
        if horas_trabajadas > 40:
            pago_extra = horas_trabajadas - 40
            pago_extra = pago_extra * 2
            total = pago_extra * rata_hora
            total += 40 * rata_hora
            print(f"Hola, {nombre}\n"
                  f"Horas trabajadas: {horas_trabajadas} \n"
                  f"Pago total: ${total}")
        elif horas_trabajadas <= 40:
            total = horas_trabajadas * rata_hora
            print(f"Hola, {nombre}\n"
                  f"Horas trabajadas: {horas_trabajadas} \n"
                  f"Pago total: ${total}")
    except ValueError:
        print("Error: Ingresaste letras en un campo que requiere números (Horas o Rata).")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


calcular_horas_trabajadas()

'''
2.	La farmacia XYZ, desea contar con un programa que calcule el 10% de descuento 
a los precios de los medicamentos para los jubilados.
'''


def calcular_precios_xyz():
    try:
        medicamente_uno = float(input("Ingrese el valor del medicamento: "))
        jubilado = input("¿Es jubilado? (si/no): ").lower().strip()

        if jubilado == "si":
            medicamente_uno = medicamente_uno - (medicamente_uno * 0.10)
            print(f"Descuento del 10%, total: ${medicamente_uno}")
        elif jubilado == "no":
            print(f"El precio del medicamente es: ${medicamente_uno}", )
        else:
            print("Valor incorrecto")
    except ValueError:
        print("Error: Ingresaste letras en un campo que requiere números (Horas o Rata).")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


calcular_precios_xyz()
