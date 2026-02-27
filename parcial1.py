# Ejercicio 1

def ComprarFruta():
    fruits = {
        "guineos": 1.35,
        "manzanas": 0.80,
        "narajas": 0.70,
        "mandarinas": 0.60
    }
    total_compra = 0
    print("*" * 40)
    print("Bienvenid@ a la Frutería Python, S.A!")
    print("*" * 40)
    while True:
        print("Tenemos las siguientes frutas disponibles en nuestro inventario:")

        for key, value in fruits.items():
            print(f"{key}: ${value:.2f} *lb")

        fruta_comprada = input("¿Qué fruta deseas comprar? ")

        if fruta_comprada in fruits:
            compra = float(input(f"El precio por libra es de ${fruits[fruta_comprada]}, ¿cuantas libras deseas?\n"))
            print(f"Tu compra de {fruta_comprada} es de ${compra * fruits[fruta_comprada]:.2f}")
            total_compra += compra * fruits[fruta_comprada]
            print(f"Total de compras: ${total_compra:.2f}")
        else:
            print("Lo siento, no tenemos esa fruta en nuestro inventario o no escribiste bien.")
            print("-" * 40)

        print("¿desea comprar otra fruta? (s/n)")
        if input().lower() == "s":
            continue
        else:
            print("-" * 40)
            print(f"Su total de compras es de: ${total_compra:.2f} dolares")
            print("Gracias por su compra, vuelva pronto!")


ComprarFruta()


# Ejercicio 2

def Cdt():
    print("Bienvenid@ a la CDT, S.A!")
    print("-" * 30)

    while True:
        bank_account = float(input("Ingrese el saldo que quiera depositar (El valor debe ser mayor a $5000,00): "))
        if bank_account > 5000:
            years = int(input("A cuantos años quiere establecer su inversión: "))
            total_intereses = (bank_account * 0.05) * years
            print(f"Los intereses en {years} años son de: ${total_intereses:.2f}")
            print(f"El saldo final es de: ${bank_account + total_intereses:.2f}")
            break
        elif bank_account <= 5000:
            print("ERROR: El valor de a depositar en la cuenta debe ser mayor a $5000.")
            print("-" * 30)

Cdt()
