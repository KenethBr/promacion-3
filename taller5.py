#Escribe un programa en Python que solicite al usuario un número entero entre 1 y 10.
#Luego, utiliza un bucle for para imprimir la tabla de multiplicar de ese número hasta el 10.

num = int(input("Ingrese un numero del 1 al 10: "))
#Se realiza un for para iterar del 1 al 10 para se se multiplique por el numero elegido por el usuario
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

