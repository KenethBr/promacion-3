#print() permite mostrar en pantalla lo que escribamos o pongamos
print("Hello, world!")
print("-"*28)
#numero entero
numberInt = 21
#numero flotante
numberFloat = 2.2
#cadena de texto
cadena = "Hello, world!"
print(cadena, numberInt)
print("-"*28)
#Lista de paises
paises = ["Panama", "Colombia","Mexico", "USA", "España", "Argentina"]
#for para recorrer desde la posición 0 hasta la 5
for pais in range(0,5):
    #imprime la posición cada que se ejecuta
    print(paises[pais])

print("-"*28)
#Diccionario Clave : Valor
auto = {
    "marca" : "Toyota",
    "año" : 2020,
    "color" : "Gris"
}

#imprime el valor de color
print(auto["color"])